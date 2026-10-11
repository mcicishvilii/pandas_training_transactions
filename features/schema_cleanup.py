import pandas as pd
from open import open_file
from constants import constants


def deduplicate_and_join():
    df_applications = open_file.open_file_and_normalize(constants.APPLICATIONS_CSV)
    raw_bureau_scores = open_file.open_file_and_normalize(constants.BUREAU_SCORES_JSON)

    median_dual = df_applications.groupby(["education_level", "employment_status"])[
        "monthly_income"
    ].transform("median")
    median_global = df_applications["monthly_income"].median()

    filled_df_applications = df_applications.assign(
        monthly_income=df_applications["monthly_income"]
        .fillna(median_dual)
        .fillna(median_global)
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
