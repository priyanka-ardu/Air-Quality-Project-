import pandas as pd
import config

def load_air_quality_data(filepath):
    # df = pd.read_csv(config.DATA_FILE)
    df = pd.read_csv(filepath)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df.columns = df.columns.str.strip().str.lower()
    print("📑 Columns in dataset:", df.columns.tolist())
    return df

if __name__ == "__main__":
    df = load_air_quality_data()
    print(df.head())
