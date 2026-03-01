import pandas as pd

df = pd.read_csv('Telco_customer_churn.csv')
cat_cols = ['Gender', 'Senior Citizen', 'Partner', 'Dependents', 'Phone Service', 
            'Multiple Lines', 'Internet Service', 'Online Security', 'Online Backup', 
            'Device Protection', 'Tech Support', 'Streaming TV', 'Streaming Movies', 
            'Contract', 'Paperless Billing', 'Total Charges']

print("Unique values for categorical columns:")
for col in cat_cols:
    if col in df.columns:
        print(f"\n{col}:")
        print(df[col].unique()[:20]) # Limit for Total Charges
    else:
        print(f"\n{col} NOT FOUND in CSV")

print("\nPayment Method (original):")
if 'Payment Method' in df.columns:
    print(df['Payment Method'].unique())
