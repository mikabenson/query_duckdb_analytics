# 🛒 US Retail Sales Analysis & 2026 Forecasting

> End-to-end analysis of 13 years of US monthly retail sales (2010–2022): which industries drive revenue, how they behaved through COVID-19, when they peak, and what 2026 could look like.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-data%20wrangling-150458?logo=pandas)
![scikit-learn](https://img.shields.io/badge/scikit--learn-gradient%20boosting-F7931E?logo=scikit-learn&logoColor=white)
![statsmodels](https://img.shields.io/badge/statsmodels-SARIMA-4B8BBE)

---

## 📌 Project Overview

Retail leaders need to know **where revenue comes from, how stable it is, and when demand peaks** so they can allocate capital, inventory and marketing effectively. This project answers those questions with exploratory analysis of monthly retail sales across **12 industries and 58 business categories**, then extends the analysis into **time-series and machine-learning forecasts for 2026**.

| | |
|---|---|
| **Records** | 9,048 monthly observations |
| **Period** | January 2010 – December 2022 |
| **Granularity** | Month × NAICS business category (58 kinds of business, grouped into 12 industries) |
| **Metric** | Sales (in thousands of US dollars) |

---

## 🔑 Key Findings

**1. Automotive dominates revenue.**
Median monthly sales: Automotive (~$67.5M) leads Food & Beverage (~$47.5M), Restaurants & Bars (~$26.0M), Health & Personal Care (~$23.8M) and Fuel & Gasoline (~$16.7M). The top four business categories by total revenue all belong to Automotive, together about **$51.2B, or 26.5%** of sales across all categories.

**2. Industries reacted to COVID-19 very differently.**

| Industry | Pattern | Evidence |
|---|---|---|
| **Automotive** | Dipped in 2020, then surged | ~$4.5M in 2020 → over $5.6M in 2022 |
| **Food & Beverage** | Steady, pandemic-proof | ~$2.0M (2010) → over $3.2M (2022), no visible 2020 decline |
| **Restaurants & Bars** | Sharp drop, strong recovery | ~$2.2M (2019) → $1.8M (2020) → $2.5M (2022) |

**3. Seasonality is industry-specific.**
In 2022, Automotive peaked in **Q2**, Restaurants & Bars in **Q3**, and Food & Beverage, Home Goods & Electronics and General Merchandise in **Q4**. Home Goods & Electronics grew about **51% from Q1 to Q4** in 2020 (~$338K → ~$510K).

**4. Food & Beverage is the most dependable baseline.**
Quarterly sales stayed in a tight band with very low volatility, which makes it a defensive anchor during economic shocks.

---

## 💡 Business Recommendations

1. **Automotive:** Invest in dealer inventory and parts supply-chain optimization, given the post-2020 acceleration.
2. **Food & Beverage:** Treat it as the core defensive hedge in downturns, given its near-linear growth.
3. **Restaurants & Bars:** Build flexible operations (e.g. hybrid delivery models) to absorb sudden demand shocks.
4. **Home Goods & Electronics:** Plan inventory capital around the Q3–Q4 surge.

---

## 🔮 2026 Forecasting

Two complementary approaches forecast monthly sales through December 2026:

| Model | Approach | Highlights |
|---|---|---|
| **SARIMA** | Seasonal ARIMA `(1,1,1)(1,1,1,12)` with log variance stabilization | Classical baseline with confidence intervals |
| **Gradient Boosting** | `GradientBoostingRegressor` on year-over-year log growth | Recursive monthly forecasts; lag, rolling and calendar features |

Both are written as reusable **object-oriented pipelines** (`prepare_data → train_and_validate → fit_production → predict_future`). Models are validated on a time-ordered 80/20 holdout using **MAPE** and **RMSE**, then refit on 100% of the history before forecasting.

> **Results:** _add your validation MAPE / RMSE and the 2026 total for each model here._

---

## 🧰 Tech Stack

- **Python:** pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Forecasting:** statsmodels (SARIMAX), scikit-learn (GradientBoostingRegressor)
- **Environment:** Jupyter Notebook

---

## 🔬 Methodology

1. **Data inspection:** shape, dtypes, duplicates, unique values, memory usage.
2. **Cleaning:** 261 missing `sales` values (2.9%) imputed with the median, which is robust to outliers.
3. **Univariate analysis:** sales distribution (right-skewed).
4. **Bivariate analysis:** median and total sales by industry; long-run trends for the top 5 industries.
5. **Seasonality:** months mapped to quarters, with peak quarter per industry for each year (2018–2022).
6. **Business-level ranking:** top 10 business categories by revenue and market share.
7. **Forecasting:** SARIMA and gradient boosting pipelines, validated and projected to 2026.

---

## 📁 Repository Structure

```
├── data/
│   └── us_monthly_retail_sales_wrangled.csv
├── notebooks/
│   └── retail_analysis.ipynb
├── src/
│   ├── sarima_sales_forecast_2026.py
│   └── gb_sales_forecast_2026_simple.py
├── outputs/
│   └── sales_forecast_2026.csv
└── README.md
```

## ▶️ Getting Started

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
pip install pandas numpy matplotlib seaborn statsmodels scikit-learn jupyter
jupyter notebook notebooks/retail_analysis.ipynb
```

---

## ⚠️ Limitations & Next Steps

- The data ends in December 2022, so 2026 forecasts are 4 years out and carry wide uncertainty.
- Business categories follow the NAICS hierarchy (e.g. 441 ⊃ 4411 ⊃ 44111), so summing across all categories double-counts; share figures are indicative.
- Planned: add 2023–2025 data, external drivers (CPI, interest rates), and a SARIMA + gradient boosting ensemble.

## 👤 Author

**<Your Name>**: Data Analyst
[LinkedIn](https://linkedin.com/in/your-profile) · [GitHub](https://github.com/your-username) · your.email@example.com
