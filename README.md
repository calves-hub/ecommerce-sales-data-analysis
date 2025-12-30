# E-commerce Sales Data Analysis

## Overview

This project analyzes e-commerce sales data to uncover business insights related to revenue trends, customer behavior, discount effectiveness, and sales forecasting.
The goal is to simulate a real-world data analyst workflow — from raw data cleaning to insight generation and predictive modeling.

## Business Questions Answered

* How do sales evolve over time (monthly & yearly trends)?
* Which customer segments generate the most revenue?
* Do discounts meaningfully impact sales volume?
* Can we forecast future sales based on historical data?

## Dataset

* **Source:** Public e-commerce sales dataset
* **Data types:** Order dates, revenue, discounts, customer IDs, product categories
* **Granularity:** Transaction-level data

## Tools & Technologies

* **Python** (pandas, numpy)
* **Data Visualization:** matplotlib, seaborn
* **Machine Learning:** scikit-learn
* **Time Series Forecasting:** statsmodels (ARIMA)
* **Environment:** Jupyter Notebook

## Project Structure

```
ecommerce-sales-data-analysis/
│
├── data/                # Raw and processed datasets
├── notebooks/           # Exploratory analysis and modeling notebooks
├── src/                 # Reusable Python modules (cleaning, features, models)
├── requirements.txt     # Project dependencies
└── README.md
```

## Key Analysis & Insights

### Sales Trends

* Monthly sales show clear seasonality patterns
* Revenue growth is uneven, with peaks aligned to promotional periods

### Customer Segmentation

* Customers were clustered using behavioral features
* Identified distinct customer groups with different spending patterns
* High-value customers account for a disproportionate share of revenue

### Discount Impact

* Discounts correlate with increased sales volume
* Excessive discounting does not always lead to proportional revenue gains

### Sales Forecasting

* Time series modeling applied to monthly sales data
* Forecasts provide directional insight rather than exact predictions
* Suitable for high-level planning and trend estimation

## Model Evaluation

* Clustering evaluated using inertia and silhouette trends
* Forecast accuracy assessed with error metrics (e.g. RMSE where applicable)
* Models prioritize interpretability over complexity

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/calves-hub/ecommerce-sales-data-analysis.git
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the notebooks in the `notebooks/` folder.

## Key Takeaways

This project demonstrates:

* End-to-end data analysis workflow
* Business-oriented thinking beyond visualization
* Practical use of machine learning and forecasting
* Clean, modular Python code organization

## Next Improvements

* Add automated tests for data preprocessing
* Improve forecasting with Prophet or advanced models
* Build an interactive dashboard (Power BI / Tableau / Streamlit)

---

📌 *This project is intended for portfolio and learning purposes.*
