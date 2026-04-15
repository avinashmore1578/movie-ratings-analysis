import streamlit as st
import pandas as pd

df = pd.read_csv("data/movies.csv")

st.title("🎬 Movie Ratings Dashboard")

# Show dataset
st.subheader("Dataset Preview")
st.dataframe(df.head())

# Top movies
st.subheader("🔥 Top 10 Movies")
top_movies = df.sort_values(by='Rating', ascending=False).head(10)
st.dataframe(top_movies)

# Rating distribution
st.subheader("📊 Rating Distribution")
st.bar_chart(df['Rating'])

# Genre filter (advanced 🔥)
st.subheader("🎭 Filter by Genre")

genre = st.text_input("Enter Genre (e.g. Action, Drama)")

if genre:
    filtered = df[df['Genre'].str.contains(genre, case=False, na=False)]
    st.write(filtered.head())