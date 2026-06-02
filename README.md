# Data-Validation-Pipeline

## Overview

This project simulates an enterprise data onboarding workflow used by insurance and financial organizations to validate policyholder records before loading them into internal reporting and analytics platforms.

The solution automatically identifies data quality issues including missing values, duplicate records, invalid email addresses, unrealistic ages, invalid premium amounts, and incorrect date formats.

## Business Problem

Organizations receive customer and policy data from multiple business units and external systems.

Poor-quality data can lead to:

* Reporting inaccuracies
* Compliance risks
* Failed system integrations
* Operational inefficiencies

This project addresses these challenges through automated validation and reporting.

## Features

### Data Quality Checks

* Missing Value Detection
* Duplicate Record Detection
* Email Validation
* Age Validation
* Premium Validation
* Date Validation

### Reporting

* Automated Validation Reports
* Data Quality Summary Metrics
* Structured Output Generation

## Technology Stack

* Python
* Pandas
* NumPy
* OpenPyXL

## Dataset

The project uses a simulated policyholder onboarding dataset containing:

* Policy Information
* Customer Demographics
* Premium Details
* Policy Start Dates

The dataset intentionally includes quality issues to demonstrate validation capabilities.

## Folder Structure

```text
data/
src/
reports/
screenshots/
```

## Future Enhancements

* Data Quality Score
* Interactive Dashboard
* Automated Email Notifications
* Cloud Deployment

## Author

Nikith Krishna G
