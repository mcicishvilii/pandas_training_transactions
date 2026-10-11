import pandas as pd
df_transactions = pd.read_parquet('ledger_transactions.parquet')

mean_amount = df_transactions.groupby("category")["amount"].transform("mean")
std_amount = df_transactions.groupby("category")["amount"].transform("std")


print(mean_amount.head(10))
print(std_amount.head(10))

