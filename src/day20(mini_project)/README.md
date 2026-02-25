# Mini Project : Exploratory Data Analysis (EDA)

## Overview

This Jupyter notebook (`MiniProject1_EDA.ipynb`) performs exploratory data analysis on customer analytics data. The analysis examines customer behavior, purchasing patterns, demographic details, income levels, shopping activity, and engagement with the company.

## Dataset

The dataset used is `customer_analytics.csv`, which contains information about customers. Each row represents one customer with details on demographics, income, shopping behavior, and engagement metrics.

## Requirements

To run this notebook, you need:

- Python 3.x
- Jupyter Notebook or JupyterLab
- Required Python libraries:
  - pandas
  - matplotlib
  - seaborn

Install the libraries using pip:
```
pip install pandas matplotlib seaborn
```

## How to Run

1. Ensure the dataset file `customer_analytics.csv` is in the same directory as the notebook.
2. Install the required libraries if not already installed.
3. Open the notebook in Jupyter:
   ```
   jupyter notebook MiniProject1_EDA.ipynb
   ```
4. Run the cells sequentially from top to bottom.

## Notebook Contents

The notebook is structured as follows:

1. **Data Loading and Initial Inspection**: Load the dataset and display basic information using `head()`, `info()`, and `describe()`.
2. **Missing Values Analysis**: Check for null values in the dataset.
3. **Data Visualization**:
   - Histograms for distribution analysis
   - Box plots for outlier detection
   - Scatter plots for relationships between variables
   - Correlation heatmap for identifying relationships
4. **Executive Summary**: Key insights from the analysis.

## Key Findings

- Customer spending behavior shows varied patterns not always correlated with income.
- Demographic factors like age and education influence purchasing behavior, suggesting opportunities for customer segmentation.
- The dataset includes customers across a wide income range, indicating diverse purchasing power.

## Outputs

The notebook generates various plots and statistical summaries. Some cells have pre-executed outputs including images (plots) and text summaries.

## Notes

- None of the cells have been executed in the current state; run them to see the outputs.
- Ensure the CSV file path is correct if running in a different environment.