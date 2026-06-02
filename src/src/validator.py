import pandas as pd
import re

# Load Dataset
df = pd.read_csv("data/policyholder_data.csv")

print("=" * 60)
print("POLICYHOLDER DATA VALIDATION REPORT")
print("=" * 60)

total_records = len(df)

missing_values = df.isnull().sum().sum()

duplicate_records = df.duplicated().sum()

email_pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

invalid_emails = df[
    ~df["Email"].fillna("").str.match(email_pattern)
]

invalid_age = df[
    (df["Age"] < 18) |
    (df["Age"] > 100)
]

invalid_premium = df[
    df["Annual_Premium"] <= 0
]

df["Parsed_Date"] = pd.to_datetime(
    df["Policy_Start_Date"],
    errors="coerce"
)

invalid_dates = df[
    df["Parsed_Date"].isna()
]

print(f"\nTotal Records: {total_records}")
print(f"\nMissing Values: {missing_values}")
print(f"\nDuplicate Records: {duplicate_records}")
print(f"\nInvalid Emails: {len(invalid_emails)}")
print(f"\nInvalid Age Records: {len(invalid_age)}")
print(f"\nInvalid Premium Records: {len(invalid_premium)}")
print(f"\nInvalid Date Records: {len(invalid_dates)}")

print("\nValidation Completed Successfully")
