from features import risk_scoring


def main():
    risk_scoring.final_merge().to_csv(
        "files/output/enriched_risk_output.csv", index=False
    )


if __name__ == "__main__":
    main()
