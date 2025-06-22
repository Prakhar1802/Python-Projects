# 🚚 Courier Charges Analysis

A data-driven project to verify courier charges based on package weight and shipping distance.

---

## 📌 Project Overview

This analysis assesses whether the courier partners of an e‑commerce company in India are charging customers fairly based on shipment weight and delivery distance. It includes:

- Detailed EDA
- Statistical verification
- Visual insight into charge distributions vs ground truth

---

## 🧪 Exploratory Data Analysis (EDA)

Conducted initial data review to:

- Check for missing entries and duplicates  
- Profile weight, distance, and charge distributions  
- Identify outliers and inconsistencies  
- Visualize relationships between weight, distance, and charged amount  

(See [`notebooks/1_EDA.ipynb`](notebooks/1_EDA.ipynb) for full analysis.)

---

## 📊 Charge Verification & Analysis

Performed statistical verification to identify pricing anomalies:

- Defined "expected charge" based on courier pricing rules (e.g., ₹X per kg per km)  
- Computed “charged vs expected” across shipments  
- Flagged outliers or mismatches suggesting over- or under-charging  
- Visualized error distributions and supplier-wise patterns  

(See [`notebooks/2_verification.ipynb`](notebooks/2_verification.ipynb))

---

## 📈 Key Findings

- ✅ Most shipments follow expected pricing patterns  
- ⚠️ A small subset (~X%) shows overcharge beyond tolerance  
- 📌 Charge variance often correlates with shipment distance bands or weight classes  
- 🔍 Some couriers consistently deviate, suggesting possible pricing issues

---

## 💬 Visual Insights

You'll find:

- Histograms of charged vs expected amounts  
- Scatter plots of weight × distance with error highlighting  
- Boxplots comparing couriers on overcharge distribution  

Refer to the notebooks for all visualizations.

---

## 🛠️ Getting Started

1. Clone the repo:
   ```bash
   git clone https://github.com/Prakhar1802/Courier-Charges-Analysis.git
   cd Courier-Charges-Analysis
2. Create a Virtual Enviroment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

## 🎯 Future Improvements

Here are some enhancements and next steps planned for the project:

- 🧾 **Automate rule extraction** from courier contracts or price sheets to reduce manual intervention.
- 📊 **Build an interactive dashboard** to flag real-time pricing violations and anomalies.
- 📆 **Scale analysis to multi-year data** to uncover long-term patterns or pricing shifts.
- ➕ **Incorporate additional data** like:
  - Cash on Delivery (COD) charges
  - Pickup/drop locations
  - Shipment types (standard, express, fragile, etc.)

---

## 🤝 Contributing

We welcome your ideas and contributions to improve this project!

To contribute:

1. 🍴 **Fork the repository**  
2. 🛠️ **Create a new feature branch**:
   ```bash
   git checkout -b feature/improve-dashboard
3. 💡 **Make your changes, and be sure to add tests or documentation where relevant**
4. 📩 **Submit a pull request for review**


