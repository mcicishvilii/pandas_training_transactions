from features import schema_cleanup, windowing_and_feature_engineering
import pandas as pd
import numpy as np


def final_merge():
    customers = schema_cleanup.deduplicate_and_join()
    transactions = windowing_and_feature_engineering.window_and_engineer_features()

    merged_df = pd.merge(customers, transactions, on="applicant_id", how="left")

    condition_1 = merged_df["credit_profile.bureau_score"] < 600
    condition_2 = merged_df["rolling_velocity"] > 20


    merged_df["risk_tier"] = np.where(
        (condition_1) & (condition_2), "High Risk", "Standard"
    )

    return merged_df
