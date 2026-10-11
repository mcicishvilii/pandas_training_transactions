from features import schema_cleanup,windowing_and_feature_engineering

def main():
    print(schema_cleanup.deduplicate_and_join())
    print(windowing_and_feature_engineering.window_and_engineer_features())

if __name__ == "__main__":
    main()