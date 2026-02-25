# Data Summary Report

## Overview
This document provides a comprehensive summary of the customer analytics dataset used in the Exploratory Data Analysis (EDA) mini-project. It includes key statistics, data structure insights, missing value handling, duplicate removal, and correlation analysis. The dataset contains 255 customer records with 14 features related to demographics, income, shopping behavior, and engagement.

## Dataset Description
The `customer_analytics.csv` file contains customer information with the following columns:
- **CustomerID**: Unique identifier for each customer (int64)
- **Age**: Customer's age in years (int64)
- **Gender**: Customer's gender (Male/Female) (object)
- **City**: City of residence (object)
- **Education**: Education level (Bachelors/Masters/PhD) (object)
- **MaritalStatus**: Marital status (Single/Married) (object)
- **AnnualIncome**: Annual income in currency units (float64)
- **SpendingScore**: Spending score (0-100 scale) (int64)
- **YearsEmployed**: Years of employment (int64)
- **PurchaseFrequency**: Number of purchases per month (int64)
- **OnlineVisitsPerMonth**: Number of online visits per month (int64)
- **ReturnedItems**: Number of returned items (int64)
- **PreferredDevice**: Preferred shopping device (Laptop/Desktop/Mobile/Tablet) (object)
- **LastPurchaseAmount**: Amount of last purchase (int64)

## Data Structure Summary
### Basic Info
- **Total Records**: 255
- **Total Columns**: 14
- **Data Types**:
  - Integer (int64): 8 columns (CustomerID, Age, SpendingScore, YearsEmployed, PurchaseFrequency, OnlineVisitsPerMonth, ReturnedItems, LastPurchaseAmount)
  - Float (float64): 1 column (AnnualIncome)
  - Object (string): 5 columns (Gender, City, Education, MaritalStatus, PreferredDevice)
- **Memory Usage**: Approximately 28.0 KB

### Sample Data (First 5 Rows)
| CustomerID | Age | Gender | City      | Education | MaritalStatus | AnnualIncome | SpendingScore | YearsEmployed | PurchaseFrequency | OnlineVisitsPerMonth | ReturnedItems | PreferredDevice | LastPurchaseAmount |
|------------|-----|--------|-----------|-----------|---------------|--------------|---------------|---------------|-------------------|----------------------|---------------|-----------------|-------------------|
| 1001       | 49  | Male   | Pune      | Masters   | Single        | 82953.0      | 66            | 23            | 19                | 9                    | 2             | Laptop          | 3944              |
| 1002       | 44  | Male   | Pune      | PhD       | Single        | 60610.0      | 56            | 22            | 1                 | 23                   | 3             | Desktop         | 3885              |
| 1003       | 42  | Male   | Mumbai    | Bachelors | Single        | 35501.0      | 44            | 18            | 10                | 29                   | 3             | Laptop          | 3247              |
| 1004       | 36  | Female | Mumbai    | Masters   | Married       | 99312.0      | 36            | 10            | 12                | 21                   | 3             | Mobile          | 2028              |
| 1005       | 23  | Male   | Pune      | Masters   | Married       | 46980.0      | 56            | 1             | 18                | 9                    | 3             | Tablet          | 1100              |

## Statistical Summary
### Descriptive Statistics
| Column              | Count | Mean       | Std        | Min   | 25%   | 50%   | 75%   | Max    |
|---------------------|-------|------------|------------|-------|-------|-------|-------|--------|
| CustomerID          | 255   | 1126.94    | 72.40      | 1001  | 1064.5| 1128  | 1190.5| 1250   |
| Age                 | 255   | 37.73      | 9.77       | 21    | 29    | 38    | 46    | 54     |
| AnnualIncome        | 243   | 74499.90   | 43939.86   | 16062 | 56353 | 69629 | 84030.5| 474327 |
| SpendingScore       | 255   | 45.72      | 17.87      | 5     | 34.5  | 47    | 57.5  | 95     |
| YearsEmployed       | 255   | 14.68      | 9.65       | 1     | 6     | 15    | 23    | 34     |
| PurchaseFrequency   | 255   | 11.57      | 7.08       | 1     | 5     | 11    | 18    | 24     |
| OnlineVisitsPerMonth| 255   | 16.08      | 7.91       | 3     | 10    | 16    | 23    | 29     |
| ReturnedItems       | 255   | 1.86       | 1.41       | 0     | 1     | 2     | 3     | 4      |
| LastPurchaseAmount  | 255   | 2795.07    | 1328.77    | 566   | 1542  | 2705  | 4001  | 4996   |

**Key Insights from Statistics:**
- Average customer age: 37.7 years (range: 21-54)
- Average annual income: ~$74,500 (highly variable, std: $43,940)
- Average spending score: 45.7 out of 100
- Average years employed: 14.7 years
- Average purchase frequency: 11.6 per month
- Average online visits: 16.1 per month
- Average returned items: 1.9 per customer
- Average last purchase: $2,795

## Data Quality Assessment
### Missing Values
| Column       | Missing Count | Percentage |
|--------------|---------------|------------|
| CustomerID   | 0             | 0.00%      |
| Age          | 0             | 0.00%      |
| Gender       | 0             | 0.00%      |
| City         | 0             | 0.00%      |
| Education    | 12            | 4.71%      |
| MaritalStatus| 0             | 0.00%      |
| AnnualIncome | 12            | 4.71%      |
| SpendingScore| 0             | 0.00%      |
| YearsEmployed| 0             | 0.00%      |
| PurchaseFrequency| 0         | 0.00%      |
| OnlineVisitsPerMonth| 0     | 0.00%      |
| ReturnedItems| 0             | 0.00%      |
| PreferredDevice| 0          | 0.00%      |
| LastPurchaseAmount| 0        | 0.00%      |

**Handling Missing Values:**
- **Education**: 12 missing values filled with mode ("Bachelors")
- **AnnualIncome**: 12 missing values filled with median ($69,629)
- All other columns had no missing values

### Duplicate Records
- **Duplicates before cleaning**: 5 records
- **Duplicates after cleaning**: 0 records
- **Action taken**: Removed all duplicate rows to ensure data integrity

## Correlation Analysis
### Correlation Matrix
| Variable             | CustomerID | Age | AnnualIncome | SpendingScore | YearsEmployed | PurchaseFrequency | OnlineVisitsPerMonth | ReturnedItems | LastPurchaseAmount |
|----------------------|------------|-----|--------------|---------------|---------------|-------------------|----------------------|---------------|-------------------|
| CustomerID           | 1.00       | -0.04| -0.04       | 0.07          | -0.02         | -0.08             | -0.03                | 0.02          | -0.03             |
| Age                  | -0.04      | 1.00| -0.05       | -0.01         | 0.98          | 0.10              | -0.03                | -0.05         | 0.09              |
| AnnualIncome         | -0.04      | -0.05| 1.00        | -0.40         | -0.06         | -0.04             | 0.10                 | -0.12         | -0.02             |
| SpendingScore        | 0.07       | -0.01| -0.40       | 1.00          | -0.02         | 0.01              | -0.07                | 0.06          | 0.03              |
| YearsEmployed        | -0.02      | 0.98| -0.06       | -0.02         | 1.00          | 0.07              | -0.05                | -0.05         | 0.11              |
| PurchaseFrequency    | -0.08      | 0.10| -0.04       | 0.01          | 0.07          | 1.00              | -0.04                | 0.08          | -0.07             |
| OnlineVisitsPerMonth | -0.03      | -0.03| 0.10        | -0.07         | -0.05         | -0.04             | 1.00                 | -0.07         | 0.01              |
| ReturnedItems        | 0.02       | -0.05| -0.12       | 0.06          | -0.05         | 0.08              | -0.07                | 1.00          | 0.02              |
| LastPurchaseAmount   | -0.03      | 0.09| -0.02       | 0.03          | 0.11          | -0.07             | 0.01                 | 0.02          | 1.00              |

**Key Correlations:**
- **Strong Positive**: Age ↔ YearsEmployed (0.98) - Older customers tend to have more years of employment
- **Strong Negative**: AnnualIncome ↔ SpendingScore (-0.40) - Higher income customers tend to have lower spending scores
- **Moderate Positive**: Age ↔ LastPurchaseAmount (0.09), YearsEmployed ↔ LastPurchaseAmount (0.11)
- **Weak/Moderate**: Most other correlations are weak (< 0.10 in absolute value)

## Data Distribution Insights
### Categorical Variables Summary
| Variable       | Unique Values | Most Common | Count | Percentage |
|----------------|---------------|-------------|-------|------------|
| Gender         | 2             | Male        | 135   | 52.9%      |
| City           | 7             | Bangalore   | 52    | 20.4%      |
| Education      | 3             | Bachelors   | 108   | 42.4%      |
| MaritalStatus  | 2             | Single      | 131   | 51.4%      |
| PreferredDevice| 4             | Laptop      | 68    | 26.7%      |

### Numerical Variables Ranges
| Variable             | Min  | Max   | Range | Mean   | Median |
|----------------------|------|-------|-------|--------|--------|
| Age                  | 21   | 54    | 33    | 37.7   | 38     |
| AnnualIncome         | 16062| 474327| 458265| 74499.9| 69629  |
| SpendingScore        | 5    | 95    | 90    | 45.7   | 47     |
| YearsEmployed        | 1    | 34    | 33    | 14.7   | 15     |
| PurchaseFrequency    | 1    | 24    | 23    | 11.6   | 11     |
| OnlineVisitsPerMonth | 3    | 29    | 26    | 16.1   | 16     |
| ReturnedItems        | 0    | 4     | 4     | 1.9    | 2      |
| LastPurchaseAmount   | 566  | 4996  | 4430  | 2795.1 | 2705   |

## Conclusion
The dataset is clean and ready for analysis after handling missing values and removing duplicates. Key characteristics include a balanced age distribution, diverse income levels, and varied customer behaviors. The correlation analysis reveals some expected relationships (age-employment) and interesting patterns (income-spending inverse relationship) that warrant further investigation in the full EDA report.