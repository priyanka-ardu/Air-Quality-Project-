import pandas as pd
import config

# Custom modules
from src.data_ingestion import load_air_quality_data
from src.data_analysis import (
    calculate_summary_statistics,
    calculate_daily_average,
    detect_pollution_peaks
)
from src.data_visualization import (
    plot_pm25_trend,
    plot_pollutant_distribution,
    plot_correlation_heatmap
)

def main():
    # Load data
    df = load_air_quality_data("./data/simulated_air_quality_data.csv")

    # Convert timestamp to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    print(f"\n📑 Columns in dataset: {list(df.columns)}")

    # Perform analysis
    summary_stats = calculate_summary_statistics(df, config.POLLUTANTS)
    print("\n📊 Summary Statistics:\n", summary_stats)

    daily_avg = calculate_daily_average(df, config.POLLUTANTS)
    print("\n📈 Daily Averages (first 5 rows):\n", daily_avg.head())

    # Set pollutant thresholds
    thresholds = {
        'pm25': 90,
        'pm10': 150,
        'no2': 80,
        'so2': 50
    }

    peaks = detect_pollution_peaks(df, config.POLLUTANTS, thresholds)
    for pollutant, peak_df in peaks.items():
        print(f"\n High {pollutant.upper()} readings:\n", peak_df.head())

    # Visualizations
    plot_pm25_trend(df)
    plot_pollutant_distribution(df)
    plot_correlation_heatmap(df)

    print("\n✅ All visualizations saved to 'outputs/figures/'")


if __name__ == "__main__":
    main()
