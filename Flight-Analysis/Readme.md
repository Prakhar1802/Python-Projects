# ✈️ Flight Analysis

Analyze and model flight pricing data to uncover trends, optimize routes, and predict future fares.

---

## 📌 Project Overview

The Flight Analysis project aims to:

- Scrape flight pricing data for given origins, destinations, and dates
- Explore and visualize fare patterns over time, airlines, and routes
- Develop predictive models to estimate future flight prices

---

## 🧩 Data Collection & Processing

- Used `scrape.py` with tools like Selenium/Requests to collect fare data
- Captured flight info: `origin`, `destination`, `date`, `airline`, `price`
- Cleaned and standardized data (timestamps, missing handling)

**Notebook**: `notebooks/1_DataCollection.ipynb`

---

## 🔍 Exploratory Data Analysis (EDA)

Performed EDA to:

- Examine fare distribution by airline, date, route
- Visualize price trends and seasonality over time
- Detect anomalies and outlier pricing events
- Compare weekday vs weekend pricing patterns

**Notebook**: `notebooks/2_EDA.ipynb`

---

## 🤖 Modeling & Prediction

Built regression models to forecast flight prices:

- Feature engineering: date parts, route dummies, airline encoding
- Models: Linear Regression, Random Forest, XGBoost
- Evaluated using MAE, RMSE, R² with train/test split

**Notebook**: `notebooks/3_Modeling.ipynb`

---

## 📈 Results

| Model               | MAE     | RMSE    | R² Score  |
|---------------------|---------|---------|-----------|
| Linear Regression   | —       | —       | —         |
| Random Forest       | —       | —       | —         |
| XGBoost             | —       | —       | —         |

🏆 *Best model:* [Model name] — with MAE of __ and R² of __.

---

## 🚀 How to Run

1. **Clone the repo**
   ```bash
   git clone https://github.com/Prakhar1802/Flight-Analysis.git
   cd Flight-Analysis

2. Create a Virtual Enviroment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt


🔮 **Future Scope**
- Integrate time-series forecasting or ensemble modeling (Prophet, LSTM)
- Expand scraping to include additional providers (Kayak, Skyscanner)
- Add fare prediction dashboard (Flask/Streamlit)
- Automate scheduled scraping and model retraining pipeline
- Use SHAP/LIME for model interpretability
