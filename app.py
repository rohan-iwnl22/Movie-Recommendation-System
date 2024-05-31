import streamlit as st
import pickle
import pandas as pd
import requests
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

def find_poster(url):
    response = requests.get(url)
    if response.status_code == 200:
        img = Image.open(BytesIO(response.content))
        return img
    else:
        print(f"Failed to retrieve image. Status code: {response.status_code}")
        return None

def recommend(movie):
    movie_index = movies[movies['Title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movie_list:
        movie_title = movies.iloc[i[0]].Title
        poster_url = movies.iloc[i[0]].Poster
        recommended_movies.append(movie_title)
        recommended_posters.append(poster_url)
    return recommended_movies, recommended_posters
  

st.title("Movie Recommendation System")

selected_movie_name = st.selectbox(
   "!! Have Recommendation for any movie !!",
   movies['Title'].values,
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    cols = st.columns(5)

    for col, name, poster in zip(cols, names, posters):
        with col:
            st.markdown(f"### {name}")
            st.image(poster, use_column_width=True)