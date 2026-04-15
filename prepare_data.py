import pandas as pd

# Load datasets
basics = pd.read_csv("data/title.basics.tsv", sep="\t")
ratings = pd.read_csv("data/title.ratings.tsv", sep="\t")

# Keep only movies
basics = basics[basics['titleType'] == 'movie']

# Merge datasets on common column
df = pd.merge(basics, ratings, on='tconst')

# Select useful columns
df = df[['primaryTitle', 'genres', 'averageRating', 'numVotes']]

# Rename columns (clean)
df.columns = ['Title', 'Genre', 'Rating', 'Votes']

# Remove missing values
df = df.dropna()

# Save clean CSV
df.to_csv("data/movies.csv", index=False)

print("✅ Clean dataset created: data/movies.csv")
print(df.head())