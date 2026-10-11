from features import schema_cleanup,windowing_and_feature_engineering
import pandas as pd

def final_merge():
    customers = schema_cleanup.deduplicate_and_join()
    transactions = windowing_and_feature_engineering.window_and_engineer_features()

    return pd.merge(transactions, customers, on="applicant_id", how="left")