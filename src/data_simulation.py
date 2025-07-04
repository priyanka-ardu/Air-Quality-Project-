import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os
import config

def simulate_air_quality_data(num_records=5000):
    timestamps = pd.date_range(start="2024-06-01", periods=num_records, freq="h")
    
    data = {
        "timestamp": timestamps,
        "PM25": np.random.normal(60, 20, num_records).clip(0),
        "PM10": np.random.normal(100, 30, num_records).clip(0),
        "NO2": np.random.normal(40, 10, num_records).clip(0),
        "SO2": np.random.normal(15, 5, num_records).clip(0),
        "CO": np.random.normal(1, 0.5, num_records).clip(0)
    }
    
    df = pd.DataFrame(data)
    os.makedirs(config.DATA_DIR, exist_ok=True)
    df.to_csv(config.DATA_FILE, index=False)
    print(f"✅ Simulated data saved to {config.DATA_FILE}")

if __name__ == "__main__":
    simulate_air_quality_data()
