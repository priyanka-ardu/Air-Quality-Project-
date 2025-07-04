# Air Quality Analysis for Kanjurmarg

## 📌 Project Overview

This project explores air quality levels in the Kanjurmarg area of Mumbai, known for high pollution due to nearby industrial activity and dense traffic. Inspired by the [Oizom Kanjurmarg Case Study](https://oizom.com/wp-content/uploads/2021/11/Kanjurmarg-Case-Study.pdf), this project uses simulated air quality data to perform a preliminary analysis of pollutant levels and identify pollution trends.

## 🎯 Objectives

- Simulate hourly air quality data for PM2.5, PM10, NO₂, and SO₂.
- Perform descriptive statistical analysis.
- Visualize pollutant trends over time.
- Identify days and periods with high pollution levels.
- Provide actionable insights for future monitoring using real-time APIs like [OpenAQ API v3](https://docs.openaq.org/).

## 📊 Tech Stack

- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Seaborn**

## 📂 Project Structure

kanjurmarg-air-quality-project/

├── data/

│ └── simulated_air_quality_data.csv

├── notebooks/

│ └── air_quality_analysis.ipynb

├── src/

│ └── data_ingestion.py

│ └── data_analysis.py

│ └── data_visualization.py

├── outputs/

│ └── figures/

│ └── pm25_trend.png

├── README.md

├── main.py

├── requirements.txt

├── config.txt

└── .gitignore


## 📈 Sample Insights

- Time-series plots of PM2.5 levels across June 2024.
- Highlighted exceedance of WHO limits.
- Identified peak pollution hours.
- (Optional extension) Comparison between weekday and weekend air quality.

## 🗂️ Data Source

- **Simulated Data**: Custom-generated data resembling hourly pollutant concentrations.


## 📌 Future Scope

- Replace simulated data with real-time OpenAQ API data.
- Integrate AQI (Air Quality Index) calculation.
- Build an alert system for high-pollution hours.

## ✅ Installation

```bash
pip install -r requirements.txt
python main.py


