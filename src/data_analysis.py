import pandas as pd

def calculate_summary_statistics(df, pollutants):
    """Compute summary statistics for given pollutants."""
    summary = df[pollutants].describe()
    return summary


def calculate_daily_average(df, pollutants):
    """Compute daily average pollutant concentrations."""
    df['date'] = df['timestamp'].dt.date
    daily_avg = df.groupby('date')[pollutants].mean().reset_index()
    return daily_avg


def detect_pollution_peaks(df, pollutants, threshold_dict):
    """Identify timestamps where pollutant levels exceed thresholds."""
    peaks = {}
    for pollutant in pollutants:
        threshold = threshold_dict.get(pollutant, None)
        if threshold:
            peaks[pollutant] = df[df[pollutant] > threshold][['timestamp', pollutant]]
    return peaks
