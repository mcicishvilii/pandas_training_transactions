import pandas as pd
import json

def open_json_and_normalize(file_path):
    with open(file_path) as f:
        raw_json = json.load(f)
        return pd.json_normalize(raw_json)

def open_csv_and_normalize(file_path):
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.replace(' ', '')
    return df

def open_file_and_normalize(file_path):
    if file_path.endswith('.csv'):
        return open_csv_and_normalize(file_path)
    elif file_path.endswith('.json'):
        return open_json_and_normalize(file_path)
    elif file_path.endswith('.parquet'):
        return pd.read_parquet(file_path)
    else:
        raise ValueError("Unsupported file format. Please provide a CSV, JSON, or Parquet file.")