import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import config  # if you're using config.py for POLLUTANTS list etc

# Create output directory if not exists
os.makedirs("outputs/figures", exist_ok=True)


def plot_pm25_trend(df):
    """Plot PM2.5 concentration trend over time."""
    plt.figure(figsize=(12, 6))
    plt.plot(df['timestamp'], df['pm25'], color='crimson')
    plt.title("PM2.5 Trend Over Time")
    plt.xlabel("Timestamp")
    plt.ylabel("PM2.5 Concentration (µg/m³)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("outputs/figures/pm25_trend.png")
    plt.close()

def plot_pollutant_distributions(df):
    pollutants = config.POLLUTANTS  # Ensure config.POLLUTANTS matches your column names (like 'pm25', 'pm10' etc)

    for pollutant in pollutants:
        plt.figure(figsize=(8, 4))
        sns.histplot(df[pollutant], bins=30, kde=True)
        plt.title(f"{pollutant.upper()} Distribution")
        plt.xlabel(pollutant.upper())
        plt.ylabel("Frequency")
        plt.grid(True)
        plt.savefig(f"outputs/figures/{pollutant}_distribution.png")
        plt.close()

def plot_pollutant_distribution(df):
    """Plot distribution of pollutant concentrations."""
    plt.figure(figsize=(12, 6))
    for pollutant in config.POLLUTANTS:
        sns.kdeplot(df[pollutant], label=pollutant)
    plt.title("Pollutant Concentration Distribution")
    plt.xlabel("Concentration (µg/m³)")
    plt.legend()
    plt.tight_layout()
    plt.savefig("outputs/figures/pollutant_distribution.png")
    plt.close()


def plot_correlation_heatmap(df):
    """Plot correlation heatmap between pollutants."""
    corr = df[config.POLLUTANTS].corr()

    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Correlation Between Pollutants")
    plt.tight_layout()
    plt.savefig("outputs/figures/pollutant_correlation_heatmap.png")
    plt.close()
