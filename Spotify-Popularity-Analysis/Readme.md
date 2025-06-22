# 🎧 Spotify Popularity Analysis

A data-driven exploration and modeling project to analyze what makes Spotify tracks popular. Powered by Kaggle data and audio features from the Spotify API.

---

## 🧠 Table of Contents

1. [Project Overview](#project-overview)  
2. [Datasets](#datasets)  
3. [Setup](#setup)  
4. [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)  
5. [Feature Engineering & Modeling](#feature-engineering--modeling)  
6. [Results](#results)  
7. [Conclusions & Insights](#conclusions--insights)  
8. [Usage Guide](#usage-guide)  
9. [Future Work](#future-work)  
10. [Contact & License](#contact--license)

---

## Project Overview

- **Goal**: Uncover patterns in audio features that correlate with a track’s popularity and build models to predict a song’s hit potential.
- **Approach**: Data cleaning → EDA → Feature engineering → Model training & evaluation.

---

## Datasets

- **Kaggle – Ultimate Spotify Tracks DB**  
  Full dataset (~200K+ tracks) with audio features and metadata.
- **Kaggle – Artists & Top Charts Data**  
  Used for labeling and contextual benchmarking (e.g., Top 50 / Top 100 lists).

Data sources and licensing details are linked in the notebooks.

---

## Setup

1. **Clone repository**:  
   ```bash
   git clone https://github.com/Prakhar1802/Spotify-Popularity-Analysis.git
   cd Spotify-Popularity-Analysis
2. **Create virtual environment & install dependencies**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

## 📊 Exploratory Data Analysis (EDA)

Performed data profiling to:

- ✅ Detect missing values and duplicates  
- 📈 Analyze distribution of key audio features: `danceability`, `energy`, `valence`, etc.  
- 🔗 Investigate correlations among features and with popularity  
- 📆 Visualize popularity across release years, genres, and artist/follower counts  

📁 **Notebook**: [`notebooks/1_EDA.ipynb`](notebooks/1_EDA.ipynb)

---

## ⚙️ Feature Engineering & Modeling

- 🏷️ Created a binary target (`popular` vs `unpopular`) based on a popularity threshold (e.g., ≥ 58 or using top chart reference).
- 🔢 One-hot encoded categorical features: `key`, `mode`, `time_signature`.
- ⚖️ Addressed class imbalance with SMOTE/oversampling techniques.
- ✂️ Split dataset into train/test sets with appropriate scaling.
- 🤖 Trained and tuned multiple models:
  - Dummy Classifier (baseline)
  - Logistic Regression *(best recall)*
  - Random Forest
  - XGBoost *(best accuracy/F1)*
  - (Optional) Neural networks / CNNs on spectrogram features (see [Future Work](#future-work))

📁 **Notebook**: [`notebooks/2_modeling.ipynb`](notebooks/2_modeling.ipynb)

---

## 📈 Results

| Model               | Recall | Precision | F₁-Score | Accuracy |
|---------------------|--------|-----------|----------|----------|
| Dummy Classifier    | 0.50   | —         | —        | ~0.50    |
| Logistic Regression | 0.66   | 0.68      | 0.67     | 0.69     |
| Random Forest       | 0.60   | 0.71      | 0.65     | 0.73     |
| XGBoost             | 0.66   | 0.70      | 0.68     | 0.74     |

- 🥇 **Best recall**: Logistic Regression (~0.66)  
- 🥈 **Best accuracy & F₁-score**: XGBoost (~0.74)

📌 **Top Predictive Features**:
- Loudness
- Energy
- Danceability
- Valence
- Explicitness

📁 See notebook for:  
📊 Confusion matrices • 🧮 Feature importance plots • 📉 ROC curves

---

## 💡 Conclusions & Insights

- 🎶 **Audio features** like loudness, energy, and danceability significantly influence popularity.
- 🔞 **Explicitness** showed moderate impact — varies by genre.
- 👤 **Artist popularity** and **playlist inclusion** were strong **non-audio predictors**.
- ⚠️ **Limitation**: Audio features alone cap F₁ around ~0.70 — richer metadata improves results.
