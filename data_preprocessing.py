import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("retail_sales_dataset.csv")

# Show first 5 rows
print(df.head())

# Check info
print(df.info())

# Check missing values
print(df.isnull().sum())