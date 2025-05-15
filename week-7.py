import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load the Iris dataset
try:
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    df['species'] = df['species'].map({i: species for i, species in enumerate(iris.target_names)})

    print("✅ Dataset loaded successfully.\n")
except Exception as e:
    print("❌ Failed to load dataset:", e)

# Display the first few rows
print("\n📌 First 5 rows:")
print(df.head())

# Check data types and missing values
print("\n📌 Data types:")
print(df.dtypes)

print("\n📌 Missing values:")
print(df.isnull().sum())

# Clean missing values if any
df = df.dropna()
print("\n✅ Cleaned dataset (dropped missing values if any).")
