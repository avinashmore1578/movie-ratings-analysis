import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("data/movies.csv")

print("Dataset Preview:")
print(df.head())

# Basic stats
print("\n📊 Statistics:")
print("Mean:", df['Rating'].mean())
print("Median:", df['Rating'].median())
print("Mode:", df['Rating'].mode()[0])

# Histogram
plt.figure()
plt.hist(df['Rating'], bins=10)
plt.title("Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.show()

# Boxplot
plt.figure()
sns.boxplot(x=df['Rating'])
plt.title("Rating Boxplot")
plt.show()

# Top movies
top_movies = df.sort_values(by='Rating', ascending=False).head(10)
print("\n🔥 Top 10 Movies:")
print(top_movies[['Title', 'Rating']])