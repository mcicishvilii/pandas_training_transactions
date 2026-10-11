import pandas as pd
import json
import numpy as np

csv_data = """ applicant_id ,full_name,submission_date,monthly_income,education_level,employment_status
APP001, Giorgi Beridze ,2025-09-01,2500.0,Bachelor,Employed
APP002, Nino Kalandadze,09/02/2025,,Master,Employed
APP001, Giorgi Beridze ,2025-09-03,2500.0,Bachelor,Employed
APP003, Levan Jishkariani,2025-09-04,1200.0,High School,Unemployed
APP004, Mariam Lomidze,09/05/2025,4200.0,PhD,Employed
APP005, Irakli Mgeladze,09/06/2025,,Bachelor,Self-Employed
APP006, Salome Kankia,09/07/2025,3100.0,Master,Employed
APP002, Nino Kalandadze,2025-09-08,1800.0,Master,Employed
"""

with open('applications.csv', 'w', encoding='utf-8') as f:
    f.write(csv_data.strip())

json_data = [
    {"applicant_id": "APP001", "credit_profile": {"bureau_score": 720, "past_defaults": 0, "hard_inquiries": 1}},
    {"applicant_id": "APP002", "credit_profile": {"bureau_score": 580, "past_defaults": 2, "hard_inquiries": 4}},
    {"applicant_id": "APP003", "credit_profile": {"bureau_score": 640, "past_defaults": 1, "hard_inquiries": 2}},
    {"applicant_id": "APP004", "credit_profile": {"bureau_score": 790, "past_defaults": 0, "hard_inquiries": 0}},
    {"applicant_id": "APP005", "credit_profile": {"bureau_score": 550, "past_defaults": 3, "hard_inquiries": 5}},
    {"applicant_id": "APP006", "credit_profile": {"bureau_score": 710, "past_defaults": 0, "hard_inquiries": 1}}
]

with open('bureau_scores.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent=2)

np.random.seed(42)

# Let's bump up rows to 35,000 to comfortably cover a full year across 6 applicants with realistic spacing
n_rows = 35000 
app_ids = [f"APP00{np.random.randint(1, 7)}" for _ in range(n_rows)]

# Generate random timestamps spread across a full 365-day period
start_date = pd.to_datetime('2025-10-11')
end_date = pd.to_datetime('2026-10-11')

# Random seconds between start and end date
random_seconds = np.random.randint(0, int((end_date - start_date).total_seconds()), size=n_rows)
timestamps = start_date + pd.to_timedelta(random_seconds, unit='s')

amounts = np.random.exponential(scale=150.0, size=n_rows)
# Inject outliers
amounts[np.random.choice(n_rows, 150)] = np.random.uniform(5000, 20000, 150)

terminals = np.random.choice(['Tbilisi Central', 'Batumi Mall', 'Kutaisi Station', 'Online Gateway'], size=n_rows)
categories = np.random.choice(['Retail', 'Groceries', 'Utilities', 'Travel'], size=n_rows)

tx_df = pd.DataFrame({
    'transaction_id': [f"TX{i:05d}" for i in range(n_rows)],
    'applicant_id': app_ids,
    'timestamp': timestamps,
    'amount': amounts,
    'terminal_location': terminals,
    'category': categories
})

# Since randomized timestamps will be out of order, sort them cleanly from the start!
tx_df = tx_df.sort_values(by=['applicant_id', 'timestamp']).reset_index(drop=True)

tx_df.to_parquet('ledger_transactions.parquet', index=False)
print("Full-year dataset generated and sorted successfully!")