import pandas as pd

df = pd.read_csv("data/policyholder_data.csv")

report = {
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
}

report_df = pd.DataFrame(report)

report_df.to_excel(
    "reports/data_quality_report.xlsx",
    index=False
)

print("Report Generated Successfully")
