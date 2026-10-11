import pandas as pd
from open import open_file
from constants import constants

def window_and_engineer_features():
    df_transactions = open_file.open_file_and_normalize(constants.LEDGER_TRANSACTIONS_PARQUET)
    mean_amount = df_transactions.groupby("category")["amount"].transform("mean")
    std_amount = df_transactions.groupby("category")["amount"].transform("std")

    upper_limit = mean_amount + (3 * std_amount)
    is_outlier = df_transactions["amount"] > upper_limit
    df_transactions = df_transactions[~is_outlier]

    df_transactions['timestamp'] = pd.to_datetime(df_transactions['timestamp'],format='mixed',dayfirst=True, errors='coerce')
    df_transactions = df_transactions.sort_values(by=['applicant_id', 'timestamp'])

    df_transactions['rolling_volume'] = (
        df_transactions.groupby("applicant_id")
        .rolling('30D', on="timestamp")["amount"]
        .sum()
        .values
    )

    df_transactions['rolling_velocity'] = (
        df_transactions.groupby("applicant_id")
        .rolling('30D', on="timestamp")["amount"]
        .count()
        .values
    )

    return df_transactions

