import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = {
    "title": ["Inception","Interstellar","The Dark Knight","Avengers","Titanic"],
    "genre": ["sci-fi thriller","sci-fi space","action crime","action superhero","romance drama"]
}

df = pd.DataFrame(data)

cv = CountVectorizer()
matrix = cv.fit_transform(df["genre"])

similarity = cosine_similarity(matrix)

def recommend(movie):
    idx = df[df["title"] == movie].index[0]
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:4]
    for i,_ in scores:
        print(df.iloc[i]["title"])

recommend("Inception")
