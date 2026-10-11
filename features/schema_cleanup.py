import pandas as pd
from open import open_file
from constants import constants


def deduplicate_and_join():
    df_applications = open_file.open_file_and_normalize(constants.APPLICATIONS_CSV)
    raw_bureau_scores = open_file.open_file_and_normalize(constants.BUREAU_SCORES_JSON)

    transformed_income = df_applications.groupby("education_level")[
        "monthly_income"
    ].transform("median")
    filled_df_applications = df_applications.fillna(
        {"monthly_income": transformed_income}
    )

    filled_df_applications["submission_date"] = pd.to_datetime(
        filled_df_applications["submission_date"],
        format="mixed",
        dayfirst=True,
        errors="coerce",
    )
    sorted_applications = filled_df_applications.sort_values(
        by="submission_date", ascending=False
    )
    drop_duplicates_applications = sorted_applications.drop_duplicates(
        subset="applicant_id", keep="first"
    )

    clean_applications_with_scores = raw_bureau_scores.set_index("applicant_id").join(
        drop_duplicates_applications.set_index("applicant_id"), how="inner"
    )

    return clean_applications_with_scores
