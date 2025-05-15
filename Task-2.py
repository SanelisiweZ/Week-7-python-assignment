# Basic statistics
print("\n📈 Descriptive statistics:")
print(df.describe())

# Group by species and compute mean
print("\n📊 Average values per species:")
print(df.groupby('species').mean())

# Example insight
print("\n🔍 Insight: On average, 'virginica' has the longest petal length.")
