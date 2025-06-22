# 🚗 Ford Car Price Analysis

Explore and model used Ford car prices to understand key pricing factors and predict future values.

---

## 📌 Project Overview

This project uses historical data from Ford car listings to:

- Identify the most influential features affecting price
- Conduct In‑depth Exploratory Data Analysis (EDA)
- Develop regression models for accurate price predictions


---

## 🔍 Exploratory Data Analysis (EDA)

Key EDA steps performed:

- Checked missing values and duplicates
- Visualized distributions of variables: `year`, `mileage`, `engineSize`, `price`, etc.
- Explored correlations and feature importance
- Identified outliers and potential data issues

**Notebook**: `notebooks/1_EDA.ipynb`

---

## 🛠️ Feature Engineering & Modeling

Data transformation and model development included:

- Encoding categorical features like `transmission`, `fuelType`, `model`
- Handling outliers in `mileage`, `age`, `engineSize`
- Creating derived features: age of car, mileage per year, etc.

**Models trained**:
- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- XGBoost Regressor

**Evaluation Metrics**: R², MAE, RMSE

**Notebooks**:  
- Feature Engineering: `notebooks/2_Feature_Engineering.ipynb`  
- Modeling: `notebooks/3_Modeling.ipynb`

---

## 📈 Results

| Model                  | R² Score | MAE    | RMSE   |
|------------------------|----------|--------|--------|
| Linear Regression      | 0.72     | 1,800  | 2,400  |
| Decision Tree Regressor| 0.78     | 1,500  | 2,100  |
| Random Forest Regressor| **0.85** | 1,200  | 1,900  |
| XGBoost Regressor      | 0.84     | 1,250  | 1,950  |

✔️ **Best Model**: Random Forest Regressor (R² ≈ 0.85)

---

## 🚀 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/Prakhar1802/Ford-price-analysis.git
   cd Ford-price-analysis
2. Create a Virtual Enviroment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

🔮 **Future Scope**
- Enhance models with ensemble methods: stacking, boosting, etc.
- Analyze temporal trends in pricing (e.g., year‑on‑year depreciation)
- Incorporate external market indicators (e.g., fuel prices, interest rates)
- Build a web dashboard for interactive price predictions
