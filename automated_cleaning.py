import pandas as pd
import json

# read data
df_applications = pd.read_csv('applications.csv')
with open('bureau_scores.json') as f:
    raw_bureau_scores = json.load(f)

# normalize collumn names and clean dupplicates
df_bureau_scores = pd.json_normalize(raw_bureau_scores)

clean_applications = df_applications.drop_duplicates()
print(clean_applications.head())

clean_applications.columns = clean_applications.columns.str.replace(' ', '')

# clean applicants


# join two tables
clean_applications_with_scores = df_bureau_scores.set_index("applicant_id").join(clean_applications.set_index("applicant_id"))

# clean_applications_with_scores.head()
