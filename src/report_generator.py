import pandas as pd

df = pd.read_csv("data/policyholder_data.csv")

report = pd.DataFrame({
    "Metric": [
        "Total Records",
        "Missing Values",
        "Duplicate Records"
    ],
    "Value": [
        len(df),
        df.isnull().sum().sum(),
        df.duplicated().sum()
    ]
})

report.to_excel(
    "reports/data_quality_report.xlsx",
    index=False
)

print("Data Quality Report Generated")
