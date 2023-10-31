from typing import Union
import functions as f
from fastapi import FastAPI
import pandas as pd
import numpy as np
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import scipy as sp
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

grouped_df = pd.read_csv(r"Api_DataFrame/grouped_df.csv")
df_developer = pd.read_csv(r"Api_DataFrame\developer.csv")
df_userdata = pd.read_csv(r"Api_DataFrame\userdata.csv")
df_best_developer_year= pd.read_csv(r"Api_DataFrame/best_developer_year.csv")
df_UserForGenre_genre = pd.read_csv(r"Api_DataFrame/UserForGenre_genre.csv")
df_UserForGenre_year = pd.read_csv(r"Api_DataFrame\UserForGenre_year.csv")
df_developer_reviews_analysis = pd.read_csv(r"Api_DataFrame\developer_reviews_analysis.csv")

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get(path="/", 
         response_class=HTMLResponse,
         tags=["Home"])
def home():
    '''
    Homepage of the api

    Returns:
    HTMLResponse: Show the home page of the API.
    '''
    return f.presentation()

@app.get(path = '/userdata/{user}',tags=["User Consults"], 
         summary="Money spent by the user ", 
         description="This function returns the money spent by the user, For example try: -Zovix-")
def userdata(user : str):  
    return f.userdata(user)

@app.get(path = '/developer/{dev}',tags=["Developer Consults"],
         summary="Number of items and the percentage by year", 
         description="This root shows the number of items and the percentage by year, For example, try: Valve")
def developer(dev : str):
    return f.developer(dev)

@app.get(path = '/UserForGenre/{genre}',tags=["User Consults"],
         summary= 'Hours played by genre, and hours played by year',
         description="Root that gives the user with more hours played by genre, and his hours played by year. For example, try: Action")
def UserForGenre(genre: str):
    return f.UserForGenre(genre)

@app.get(path = '/best_developer_year/{year}',tags=["Developer Consults"],
         summary="top 3 developers with most recommended games by the users by year given",
         description="Gives top 3 developers with most recommended games by the users by year given. For example, try 1998")
def best_developer_year(year: int):
    return f.best_developer_year(year)

@app.get(path = '/developer_reviews_analysis/{dev}',tags=["Developer Consults"],
         summary="Returns the developer name and it's reviews (positive/negative)",
         description="Acorrding to the developer given returns the developer name and it's reviews (positive/negative). For example, Try: Ubisoft")
def developer_reviews_analysis(dev : str):
    return f.developer_reviews_analysis(dev)

@app.get (path="/recommendation_game/{id_game}", tags =["Games Consult"],
          summary="Returns 5 similar games, acording to the one you provided",
          description="cosine similarity machine learning enhanced query, gives you 5 games according to the game(id) you give. For instance, Try: 342580")
def recommendation_game(id_game : int):
    return f.find_similar_games(id_game)