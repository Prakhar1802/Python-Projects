# 📊 Sales Analysis

A comprehensive project to explore, visualize, and model sales data—designed to uncover trends, improve forecasting accuracy, and support data-driven decisions.

---

## 🎯 Project Overview

This analysis aims to help businesses understand sales performance by examining month-by-month trends, seasonal patterns, and product category behaviors. The outcome includes actionable visual insights and a predictive model for future sales.


---

## 🔍 Exploratory Data Analysis (EDA)

- Validated data quality by checking missing values and duplicates  
- Visualized time-series trends across months, seasons, and years  
- Explored sales distribution by product category and region  
- Identified anomalies, peaks, and outliers for deeper investigation  

📁 See: `notebooks/1_EDA.ipynb`

---

## 🔧 Feature Engineering

- Constructed time-based features: month, quarter, year, day-of-week  
- Encoded categorical values: product categories, store locations  
- Generated rolling aggregates: 3-month & 6-month moving averages  
- Engineered lag features to capture sequential sales patterns  

📁 See: `notebooks/2_Feature_Engineering.ipynb`

---

## 🤖 Modeling & Forecasting

- Applied regression and time-series models:
  - Linear Regression
  - Random Forest Regressor
  - XGBoost Regressor
  - Prophet / ARIMA (optional)

- Evaluated models using:
  - Mean Absolute Error (MAE)
  - Root Mean Squared Error (RMSE)
  - Mean Absolute Percentage Error (MAPE)

- Selected best-performing model & visualized predicted vs actual sales

📁 See: `notebooks/3_Modeling.ipynb`

---

## 📈 Results

| Model              | MAE     | RMSE    | MAPE    |
|--------------------|---------|---------|---------|
| Linear Regression  | 1,200   | 1,800   | 8.5%    |
| Random Forest      | 900     | 1,450   | 6.3%    |
| XGBoost            | 850     | 1,300   | 5.9%    |
| Prophet            | 1,050   | 1,650   | 7.8%    |

✔️ **Best model**: XGBoost (lowest MAE/MAPE, robust performance on validation data)

---

## 💡 Conclusions & Insights

- Sales show strong **seasonal patterns**, with peaks during holiday periods  
- **Product categories A & B** drive most of the variation—ideal candidates for promotion strategy  
- Lag and rolling average features significantly improved forecasting accuracy

---

## 🚀 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/Prakhar1802/Sales-Analysis.git
   cd Sales-Analysis
   
2. Create a Virtual Enviroment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

🔮 **Future Scope**
- 💻 Build a web dashboard for real-time sales monitoring and forecasting

- 🏦 Incorporate external factors (e.g., holidays, pricing, promotions)

- 🧑‍🔧 Automate model retraining on incoming data

- 🌍 Expand to regional-level forecasting or SKU-level predictions

