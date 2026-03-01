import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load the pipeline
@st.cache_resource
def load_pipe():
    with open('pipe.pkl', 'rb') as f:
        return pickle.load(f)

pipe = load_pipe()

# Page configuration
st.set_page_config(
    page_title="Telco Customer Churn Prediction",
    page_icon="📞",
    layout="wide"
)

# Custom CSS for premium look
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #45a049;
        transform: scale(1.02);
    }
    .prediction-container {
        padding: 20px;
        border-radius: 15px;
        background-color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📞 Telco Customer Churn Prediction")
st.markdown("Predict the probability of a customer leaving the service based on various parameters.")

# Divide inputs into columns
col1, col2, col3 = st.columns(3)

with col1:
    st.header("👤 Demographic Information")
    gender = st.selectbox("Gender", ["Male", "Female"])
    senior_citizen = st.selectbox("Senior Citizen", ["No", "Yes"])
    partner = st.selectbox("Partner", ["No", "Yes"])
    dependents = st.selectbox("Dependents", ["No", "Yes"])

with col2:
    st.header("📄 Service & Contract")
    tenure_months = st.number_input("Tenure Months", min_value=0, max_value=100, value=1)
    phone_service = st.selectbox("Phone Service", ["No", "Yes"])
    multiple_lines = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])
    internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    paperless_billing = st.selectbox("Paperless Billing", ["No", "Yes"])
    payment_method = st.selectbox("Payment Method", [
        "Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"
    ])

with col3:
    st.header("🛠️ Features & Charges")
    online_security = st.selectbox("Online Security", ["No", "Yes", "No internet service"])
    online_backup = st.selectbox("Online Backup", ["No", "Yes", "No internet service"])
    device_protection = st.selectbox("Device Protection", ["No", "Yes", "No internet service"])
    tech_support = st.selectbox("Tech Support", ["No", "Yes", "No internet service"])
    streaming_tv = st.selectbox("Streaming TV", ["No", "Yes", "No internet service"])
    streaming_movies = st.selectbox("Streaming Movies", ["No", "Yes", "No internet service"])
    monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=50.0)
    total_charges = st.number_input("Total Charges", min_value=0.0, value=50.0)
    cltv = st.number_input("CLTV", min_value=0, value=2000)

# Prediction Logic
if st.button("Predict Churn Status"):
    # Prepare Payment dummy columns
    # In feature_names_in_, they are: 'Payment_Electronic check', 'Payment_Mailed check', 'Payment_Bank transfer', 'Payment_Credit card'
    # We map the selected payment method to these dummies
    
    pay_dummy = {
        'Payment_Electronic check': 1 if payment_method == "Electronic check" else 0,
        'Payment_Mailed check': 1 if payment_method == "Mailed check" else 0,
        'Payment_Bank transfer': 1 if "Bank transfer" in payment_method else 0,
        'Payment_Credit card': 1 if "Credit card" in payment_method else 0
    }
    
    # Create the data dictionary in the EXACT order of pipe.feature_names_in_
    input_data = {
        'Gender': gender,
        'Senior Citizen': senior_citizen,
        'Partner': partner,
        'Dependents': dependents,
        'Tenure Months': tenure_months,
        'Phone Service': phone_service,
        'Multiple Lines': multiple_lines,
        'Internet Service': internet_service,
        'Online Security': online_security,
        'Online Backup': online_backup,
        'Device Protection': device_protection,
        'Tech Support': tech_support,
        'Streaming TV': streaming_tv,
        'Streaming Movies': streaming_movies,
        'Contract': contract,
        'Paperless Billing': paperless_billing,
        'Monthly Charges': monthly_charges,
        'Total Charges': str(total_charges), # Convert to string as per our probe
        'CLTV': cltv,
        'Payment_Electronic check': pay_dummy['Payment_Electronic check'],
        'Payment_Mailed check': pay_dummy['Payment_Mailed check'],
        'Payment_Bank transfer': pay_dummy['Payment_Bank transfer'],
        'Payment_Credit card': pay_dummy['Payment_Credit card']
    }
    
    # Create DataFrame
    input_df = pd.DataFrame([input_data])
    
    try:
        # Prediction
        prediction = pipe.predict(input_df)[0]
        prediction_proba = pipe.predict_proba(input_df)[0][1] if hasattr(pipe, 'predict_proba') else None
        
        st.markdown("---")
        st.subheader("Results")
        
        if prediction == 1 or prediction == "Yes":
           st.error(f"Prediction: **This customer is likely to CHURN.**")
        else:
           st.success(f"Prediction: **This customer is likely to STAY.**")
           
        if prediction_proba is not None:
            st.write(f"Confidence (Churn Probability): **{prediction_proba:.2%}**")
            st.progress(prediction_proba)

    except Exception as e:
        st.error(f"Error during prediction: {e}")
        st.info("Ensure all input parameters match the model's expectations.")

st.sidebar.markdown("### About")
st.sidebar.info("This application uses a pre-trained Decision Tree model to predict customer churn for a telecom company.")
st.sidebar.markdown("Created with ❤️ by Babar ALi Khan")
