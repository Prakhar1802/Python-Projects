# 🏥 Medical Insurance Cost Prediction

Predicting individual medical insurance charges using healthcare and demographic attributes.

---

## 📌 Project Overview

Health insurance costs depend on several factors like age, sex, BMI, smoking status, and region. This project analyzes these relationships and builds regression models to estimate insurance charges.


---

## 🔍 Exploratory Data Analysis (EDA)

- Checked distribution of attributes: **age**, **sex**, **BMI**, **children**, **smoker**, **region**, **charges**
- Investigated correlations and outliers
- Visualized how smoking and obesity impact insurance costs
- Identified key patterns: smokers with high BMI incur highest charges

**Notebook**: `notebooks/1_EDA.ipynb`

---

## ⚙️ Data Processing & Modeling

- Handled duplicates and missing values  
- Created categorical features via encoding techniques  
- Engineered new features (e.g., BMI categories, interaction terms)

**Models trained**:
- Linear Regression  
- Decision Tree Regression  
- Random Forest Regression  
- Ridge & Lasso Regression  

**Model evaluation metrics**:
- R², MAE, RMSE  
- Hyperparameter optimization with grid search

**Notebook**: `notebooks/2_Preprocessing.ipynb`, `notebooks/3_Modeling.ipynb`

---

## 📈 Results

| Model               | R² Score | MAE      | RMSE     |
|---------------------|----------|----------|----------|
| Linear Regression   | ~0.77    | ~4300    | ~6200    |
| Decision Tree       | ~0.78    | ~2800    | ~6100    |
| Random Forest       | ~0.86    | ~2600    | ~4840    |
| Ridge Regression    | ~0.86    | ~4310    | ~6238    |

🎯 **Best model**: Random Forest (R² ≈ 0.86, RMSE ≈ 4840)

---

## 🚀 How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/Prakhar1802/Medical-Insurance-Cost-Prediction.git
   cd Medical-Insurance-Cost-Prediction
2. Install & Preapre Enviroment
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python src/predict.py --input data/test_samples.csv

---

🔮 **Future Scope**

- Integrate advanced models: Gradient Boosting, XGBoost, Neural Networks

- Add explainability with SHAP or LIME

- Build a user interface (web app or desktop GUI) for real-time predictions

- Expand dataset using external sources or additional socioeconomic features

- Set up automated model retraining pipeline on new data











