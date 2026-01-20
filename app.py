import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    responce = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=875aff1eb2621fa99092b6fa7bbe8dcb&language=en-US'.format(movie_id))
    data = responce.json()
    return ("https://image.tmdb.org/t/p/w500/" + data['poster_path'])

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[
        1:6]

    recommended_movies = []
    movie_poster = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        movie_poster.append(fetch_poster(movie_id))
    return recommended_movies, movie_poster

movies_list = pickle.load(open("movies.pkl", "rb"))
movies = pd.DataFrame(movies_list)
similarity = pickle.load(open("similarity.pkl", "rb"))

st.title('Movie_recommender_system')

selected_movie_name = st.selectbox(
    'Please select a movie to get recommendations for',
    movies['title'].values,
    index = None,
    placeholder="Enter a movie..."
)

if st.button('Get recommendations'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(posters[0])
        st.text(names[0])
    with col2:
        st.image(posters[1])
        st.text(names[1])
    with col3:
        st.image(posters[2])
        st.text(names[2])
    with col4:
        st.image(posters[3])
        st.text(names[2])
    with col5:
        st.image(posters[4])
        st.text(names[4])
