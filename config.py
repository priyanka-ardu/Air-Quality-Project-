import os

# Base directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")
FIGURE_DIR = os.path.join(OUTPUT_DIR, "figures")

# Data file path
DATA_FILE = os.path.join("./",DATA_DIR, "simulated_air_quality_data.csv")

# Columns for pollutants
# POLLUTANTS = ["PM2.5", "PM10", "NO2", "SO2", "CO"]
POLLUTANTS = ['pm25', 'pm10', 'no2', 'so2']
