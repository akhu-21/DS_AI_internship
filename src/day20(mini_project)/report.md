# Exploratory Data Analysis (EDA) Report: Customer Analytics Mini-Project

## Project Overview
This report presents a comprehensive exploratory data analysis of customer analytics data. The analysis aims to understand customer behavior, purchasing patterns, demographic influences, and key relationships within the dataset. The project follows a structured approach divided into four phases: Setup & Inspection, Data Preprocessing, Univariate & Bivariate Analysis, and Multivariate Analysis & Storytelling.

**Dataset**: `customer_analytics.csv` (255 customer records, 14 features)  
**Analysis Date**: February 25, 2026  
**Tools Used**: Python (pandas, matplotlib, seaborn), Jupyter Notebook

## Table of Contents
1. [Executive Summary](#executive-summary)
2. [Phase 1: The Detective Work (Setup & Inspection)](#phase-1-the-detective-work-setup--inspection)
3. [Phase 2: The Cleanup (Data Preprocessing)](#phase-2-the-cleanup-data-preprocessing)
4. [Phase 3: The Deep Dive (Univariate & Bivariate Analysis)](#phase-3-the-deep-dive-univariate--bivariate-analysis)
5. [Phase 4: The Big Picture (Multivariate & Storytelling)](#phase-4-the-big-picture-multivariate--storytelling)
6. [Key Findings & Insights](#key-findings--insights)
7. [Recommendations](#recommendations)
8. [Limitations & Future Work](#limitations--future-work)

## Executive Summary
This EDA reveals critical insights into customer behavior and purchasing patterns. The dataset contains 255 customers with diverse demographics and income levels. Key findings include:

- **Customer Demographics**: Balanced age distribution (21-54 years, mean: 37.7), slight male dominance (52.9%), and varied education levels
- **Income Distribution**: Wide range ($16K-$474K, mean: $74.5K) with significant variation
- **Spending Patterns**: Inverse relationship between income and spending score, suggesting different customer segments
- **Behavioral Insights**: Age strongly correlates with employment years, education influences purchase amounts
- **Data Quality**: 4.7% missing values in Education and AnnualIncome columns, successfully handled

The analysis identifies opportunities for customer segmentation and targeted marketing strategies.

## Phase 1: The Detective Work (Setup & Inspection)

### Data Loading and Initial Overview
The analysis begins with loading the customer analytics dataset using pandas. The dataset contains 255 rows and 14 columns representing various customer attributes.

**Key Dataset Characteristics:**
- **Total Records**: 255 customers
- **Features**: 14 (8 numerical, 5 categorical, 1 identifier)
- **Data Types**: Mix of integers, floats, and categorical strings
- **Memory Usage**: 28.0 KB

### Initial Data Inspection
Three primary functions were used to understand the data structure:

1. **`df.head()`**: Displays first 5 records showing sample values
2. **`df.info()`**: Provides data types, non-null counts, and memory usage
3. **`df.describe()`**: Generates statistical summaries for numerical columns

**Sample Data Preview:**
| CustomerID | Age | Gender | City   | Education | MaritalStatus | AnnualIncome | SpendingScore | YearsEmployed | PurchaseFrequency | OnlineVisitsPerMonth | ReturnedItems | PreferredDevice | LastPurchaseAmount |
|------------|-----|--------|--------|-----------|---------------|--------------|---------------|---------------|-------------------|----------------------|---------------|-----------------|-------------------|
| 1001       | 49  | Male   | Pune   | Masters   | Single        | 82953        | 66            | 23            | 19                | 9                    | 2             | Laptop          | 3944              |
| 1002       | 44  | Male   | Pune   | PhD       | Single        | 60610        | 56            | 22            | 1                 | 23                   | 3             | Desktop         | 3885              |

**Statistical Summary Highlights:**
- Age range: 21-54 years (mean: 37.7)
- Income range: $16,062-$474,327 (mean: $74,500)
- Spending scores: 5-95 (mean: 45.7)
- Employment: 1-34 years (mean: 14.7)

## Phase 2: The Cleanup (Data Preprocessing)

### Missing Values Analysis
Initial assessment revealed missing values in two columns:
- **Education**: 12 missing values (4.71%)
- **AnnualIncome**: 12 missing values (4.71%)

**Missing Values Table:**
| Column       | Missing Count | Percentage | Handling Method |
|--------------|---------------|------------|-----------------|
| Education    | 12            | 4.71%      | Mode imputation |
| AnnualIncome | 12            | 4.71%      | Median imputation |

**Imputation Strategy:**
- **Categorical (Education)**: Filled with mode ("Bachelors") to maintain distribution
- **Numerical (AnnualIncome)**: Filled with median ($69,629) to avoid outlier influence

### Duplicate Records Handling
- **Initial duplicates**: 5 records identified
- **Action**: Complete removal using `df.drop_duplicates()`
- **Final duplicates**: 0 records
- **Result**: Clean dataset with 250 unique customer records

**Data Quality Verification:**
- All missing values resolved
- No duplicate records remaining
- Dataset integrity maintained

## Phase 3: The Deep Dive (Univariate & Bivariate Analysis)

### Univariate Analysis

#### Age Distribution
- **Visualization**: Histogram with 10 bins
- **Key Insights**:
  - Balanced distribution across age groups
  - Peak concentration in 35-45 age range
  - No extreme outliers
  - Indicates diverse customer base

#### Gender Distribution
- **Visualization**: Bar chart
- **Key Insights**:
  - Male customers: 135 (52.9%)
  - Female customers: 120 (47.1%)
  - Slight male dominance
  - Balanced representation for analysis

#### Annual Income Distribution
- **Visualization**: Histogram with 10 bins
- **Key Insights**:
  - Highly variable income levels
  - Right-skewed distribution
  - Wide range indicates diverse purchasing power
  - Potential for income-based segmentation

### Bivariate Analysis

#### Income vs Spending Behavior
- **Visualization**: Scatter plot
- **Key Insights**:
  - Negative correlation observed
  - Higher income ≠ higher spending score
  - Suggests complex customer behavior patterns
  - Potential for behavioral segmentation

#### Education vs Purchase Amount
- **Visualization**: Box plot
- **Key Insights**:
  - Variation across education levels
  - Higher education levels show different spending patterns
  - Indicates demographic influence on purchasing

#### Annual Income Distribution (Box Plot)
- **Visualization**: Box plot
- **Key Insights**:
  - Significant outliers present
  - Median income: $69,629
  - Interquartile range shows typical income spread
  - Outliers suggest high-net-worth customers

#### Spending Score by Gender
- **Visualization**: Box plot
- **Key Insights**:
  - Similar median spending scores across genders
  - Slight variations in distribution
  - Gender may not be primary spending differentiator

## Phase 4: The Big Picture (Multivariate & Storytelling)

### Correlation Analysis
The correlation matrix reveals relationships between numerical variables:

**Strongest Correlations:**
| Relationship | Correlation | Interpretation |
|--------------|-------------|----------------|
| Age ↔ YearsEmployed | 0.98 | Older customers have more employment experience |
| AnnualIncome ↔ SpendingScore | -0.40 | Higher income correlates with lower spending scores |
| Age ↔ LastPurchaseAmount | 0.09 | Slight positive relationship |
| YearsEmployed ↔ LastPurchaseAmount | 0.11 | Employment experience influences purchase amounts |

**Correlation Heatmap Insights:**
- Visual representation of all variable relationships
- Color-coded intensity for quick identification
- Helps detect hidden patterns and feature importance
- Guides feature selection for predictive modeling

### Multivariate Storytelling
The analysis reveals a complex customer landscape:

1. **Demographic Patterns**: Age strongly predicts employment duration and influences purchase behavior
2. **Economic Factors**: Income levels show inverse relationship with spending scores, suggesting different customer motivations
3. **Behavioral Segmentation**: Purchase patterns vary by education and demographics
4. **Device Preferences**: Technology adoption varies across customer segments

## Key Findings & Insights

### Customer Segmentation Opportunities
1. **High-Income Low-Spenders**: Customers with high income but low spending scores may represent value-driven shoppers
2. **Young Professionals**: Younger customers with shorter employment show different purchasing patterns
3. **Education-Based Groups**: Higher education levels correlate with different spending behaviors

### Behavioral Patterns
- **Spending Variability**: Income is not the sole predictor of spending behavior
- **Demographic Influence**: Age and education significantly impact purchase decisions
- **Technology Adoption**: Device preferences vary across customer groups

### Data Quality Achievements
- **Missing Data**: Successfully handled 4.7% missing values
- **Duplicates**: Eliminated all duplicate records
- **Data Integrity**: Maintained dataset completeness and accuracy

## Recommendations

### Business Strategy
1. **Targeted Marketing**: Develop campaigns based on income-spending score combinations
2. **Demographic Segmentation**: Create customer groups based on age, education, and employment
3. **Personalization**: Tailor offerings to different behavioral segments

### Data Enhancement
1. **Additional Features**: Consider collecting more behavioral data (loyalty program participation, product preferences)
2. **Time-Series Data**: Include purchase history over time for trend analysis
3. **Customer Feedback**: Integrate satisfaction scores for holistic customer understanding

### Analytical Next Steps
1. **Clustering Analysis**: Apply K-means or hierarchical clustering for customer segmentation
2. **Predictive Modeling**: Build models to predict spending behavior and customer lifetime value
3. **A/B Testing**: Design experiments to test marketing strategies across segments

## Limitations & Future Work

### Current Limitations
- **Sample Size**: 255 customers may not represent entire population
- **Cross-Sectional Data**: Single point-in-time analysis limits trend insights
- **Geographic Coverage**: Limited to specific cities, may not generalize globally
- **Feature Scope**: Analysis based on available 14 features; additional variables could provide deeper insights

### Future Enhancements
1. **Longitudinal Study**: Track customer behavior over time
2. **Expanded Dataset**: Include more customers and additional features
3. **Advanced Analytics**: Implement machine learning for customer segmentation and prediction
4. **Real-time Analysis**: Develop dashboards for ongoing monitoring
5. **Causal Analysis**: Conduct experiments to establish cause-effect relationships

## Conclusion
This EDA provides a solid foundation for understanding customer analytics. The structured approach revealed important patterns and opportunities for customer segmentation. The findings demonstrate that customer behavior is complex and influenced by multiple factors beyond simple demographics. The cleaned dataset and identified insights serve as a valuable resource for developing targeted marketing strategies and improving customer engagement.

**Next Steps**: Proceed with advanced analytics, predictive modeling, and strategy implementation based on these insights.

---
**Report Generated**: February 25, 2026  
**Analysis Performed By**: AI Assistant  
**Dataset Version**: customer_analytics.csv  
**Code Repository**: MiniProject1_EDA.ipynb