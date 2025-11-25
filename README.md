# Predicting Stock Price Movements with News Sentiment Analysis

This project analyzes the correlation between financial news sentiment and stock price movements for six major technology companies. It serves as a practical demonstration of data engineering, financial analysis, and natural language processing (NLP) techniques.

## Table of Contents

* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
  * [Running the Analysis](#running-the-analysis)
* [Project Structure](#project-structure)
* [Results](#results)

## About the Project

This project investigates the hypothesis that the sentiment of financial news headlines can be a predictor of daily stock returns. The analysis focuses on six leading technology stocks: Apple (AAPL), Amazon (AMZN), Google (GOOG), Meta (META), Microsoft (MSFT), and NVIDIA (NVDA).

The project involves:
- **Data Engineering:** Cleaning and aligning financial and news datasets.
- **Financial Analysis:** Calculating technical indicators like RSI and MACD, and daily returns.
- **Sentiment Analysis:** Using the VADER lexicon to perform sentiment analysis on news headlines.
- **Correlation Analysis:** Measuring the Pearson correlation between news sentiment and stock returns.

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This project requires Python 3.x and pip.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/your_username/Predicting-news-sentiment-price-movement-.git
   ```
2. Install Python packages
   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Data
plt.savefig('../images/Top 15 News Publishers by Article Count.png')
The project uses two main data sources:
- **News Data:** A CSV file named `raw_analyst_ratings.csv` containing news headlines. This file should be placed in the `data/newsData` directory.
- **Stock Data:** Historical stock price data obtained from Yahoo Finance. The CSV files for each stock should be placed in the `data/yfinance_data/Data` directory.

### Running the Analysis

The analysis can be run using the provided Jupyter notebooks in the `notebooks` directory:
- `EDA.ipynb`: For exploratory data analysis.
- `Quantitative_Analysis.ipynb`: For calculating technical indicators.
- `Correlation.ipynb`: For running the final correlation analysis.




## Project Structure

```
├── .github/workflows
├── images
├── notebooks
├── src
├── .gitignore
├── README.md
└── requirements.txt
```

- **`src/`**: Contains the core Python modules for financial analysis and sentiment analysis.
- **`notebooks/`**: Jupyter notebooks for exploratory analysis and running the main analysis.
- **`images/`**: Contains plots and images generated during the analysis, as well as the final report.


## Results

The analysis revealed a weak to negligible positive correlation between same-day news sentiment and daily stock returns for the analyzed stocks. This suggests that daily returns are influenced more by other market factors than by the aggregated news sentiment of the same day.





