import pandas as pd
import re

# Load dataset
df = pd.read_csv("data/policyholder_data.csv")

# Basic checks
total_records = len(df)
missing_values = df.isnull().sum().sum()
duplicate_records = df.duplicated().sum()

# Email validation
email_pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

invalid_emails = df[
    ~df["Email"].fillna("").str.match(email_pattern)
]

# Age validation
invalid_age = df[
    (df["Age"] < 18) |
    (df["Age"] > 100)
]

# Premium validation
invalid_premium = df[
    df["Annual_Premium"] <= 0
]

# Date validation
df["Parsed_Date"] = pd.to_datetime(
    df["Policy_Start_Date"],
    errors="coerce"
)

invalid_dates = df[
    df["Parsed_Date"].isna()
]

# -----------------------------
# Data Quality Score
# -----------------------------

issues = (
    missing_values +
    duplicate_records +
    len(invalid_emails) +
    len(invalid_age) +
    len(invalid_premium) +
    len(invalid_dates)
)

score = max(
    0,
    round(
        100 - ((issues / total_records) * 100)
    )
)

# -----------------------------
# Report Output
# -----------------------------

print("=" * 60)
print("POLICYHOLDER DATA VALIDATION REPORT")
print("=" * 60)

print(f"Total Records: {total_records}")
print(f"Missing Values: {missing_values}")
print(f"Duplicate Records: {duplicate_records}")
print(f"Invalid Emails: {len(invalid_emails)}")
print(f"Invalid Age Records: {len(invalid_age)}")
print(f"Invalid Premium Records: {len(invalid_premium)}")
print(f"Invalid Date Records: {len(invalid_dates)}")

print("\n" + "=" * 60)
print(f"DATA QUALITY SCORE: {score}/100")
print("=" * 60)
