import pandas as pd
import numbers as np

df = pd.read_csv("imdb_top250_movies.csv")

result = df.columns
result = df.head()
result = df.head(10)
result = df.tail()
result = df.tail(10)
result = df["Title"]
result = df["Title"].head()
result = df[["Title","imdbRating"]].head()
result = df[["Title","imdbRating"]].tail(7)
result = df[5:10][["Title","imdbRating"]].head()
result = df[df["imdbRating"] >= 8.0 ][["Title","imdbRating"]].head(50)

result = df[(df["Year"] >= 2014 ) & (df["Year"] <= 2015)][["Year","Title"]]


print(result)