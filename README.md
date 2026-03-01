# 📞 Telco Customer Churn Prediction App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A premium **Machine Learning** web application built with **Streamlit** to predict customer churn for telecommunication companies. This tool helps businesses identify at-risk customers and implement proactive retention strategies.

---

## 🚀 Key Features

*   **Real-time Predictions**: Instant churn probability using a pre-trained **Decision Tree** pipeline.
*   **Comprehensive Features**: Analysis based on demographics, contract types, service usage, and billing history.
*   **Interactive UI**: Sleek, modern interface with glassmorphism effects and responsive design.
*   **Detailed Insights**: Provides both a binary prediction (Stay/Churn) and a confidence score.

## 🛠️ Tech Stack

- **Core**: Python 3.10
- **Frontend**: [Streamlit](https://streamlit.io/)
- **Machine Learning**: Scikit-Learn (Pipeline, DecisionTreeClassifier)
- **Data Handling**: Pandas, NumPy
- **Styling**: Custom CSS (Vanilla)

## 📊 Dataset Overview

The model is trained on the **Telco Customer Churn** dataset, covering:
- **Demographics**: Gender, Senior Citizen status, Partner, and Dependents.
- **Services**: Phone, Multiple Lines, Internet (DSL/Fiber optic), Online Security, Online Backup, Device Protection, Tech Support, and Streaming.
- **Account Info**: Tenure, Contract type, Paperless Billing, Payment Method, Monthly Charges, and Total Charges.

## ⚙️ Installation & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/telco-churn-prediction.git
cd telco-churn-prediction
```

### 2. Set Up Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install streamlit pandas scikit-learn numpy
```

### 4. Run the Application
```bash
streamlit run app.py
```

## 🧠 Model Pipeline

The application utilizes a serialized `pipe.pkl` which includes:
1.  **Imputation**: Handles missing values in numerical and categorical features.
2.  **Scaling**: Standardizes numerical features (`Tenure Months`, `Monthly Charges`, `CLTV`).
3.  **Encoding**: One-Hot Encoding for categorical variables.
4.  **Classifier**: A tuned `DecisionTreeClassifier` optimized for recall and accuracy.

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improving the UI or model performance, please open an issue or submit a pull request.

---

**Developed with ❤️ by [Babar Ali Khan](https://github.com/your-profile)**
