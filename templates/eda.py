import pandas as pd

# Load dataset
df = pd.read_csv("data/creditcard.csv")

# Display dataset shape
print("Dataset Shape:", df.shape)

# Display first 5 rows
print("\nFirst 5 Rows:\n")
print(df.head())

# Display columns
print("\nColumns:\n")
print(df.columns)

# Dataset info
print("\nDataset Information:\n")
print(df.info())

# Check null values
print("\nNull Values:\n")
print(df.isnull().sum())

# Fraud vs Safe transactions
print("\nClass Distribution:\n")
print(df['Class'].value_counts())

# Percentage distribution
print("\nClass Percentage:\n")
print(df['Class'].value_counts(normalize=True) * 100)

# Basic statistics
print("\nDataset Statistics:\n")
print(df.describe())
