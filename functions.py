import pandas as pd
import numpy as np
import scipy as sp
import pyarrow as pa
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

df_developer = pd.read_csv(r"Api_DataFrame/developer.csv")
df_userdata = pd.read_csv(r"Api_DataFrame/userdata.csv")
df_best_developer_year= pd.read_csv(r"Api_DataFrame/best_developer_year.csv")
df_UserForGenre_genre = pd.read_csv(r"Api_DataFrame/UserForGenre_genre.csv")
df_UserForGenre_year = pd.read_csv(r"Api_DataFrame/UserForGenre_year.csv")
df_developer_reviews_analysis = pd.read_csv(r"Api_DataFrame/developer_reviews_analysis.csv")
grouped_df = pd.read_csv(r"Api_DataFrame/grouped_df.csv")

def presentation():
    '''
    HTML who works as a presentation for the API
    '''
    return '''
<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <title>STEAM Api</title>
    <h1>STEAM Api</h1>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <link rel='stylesheet' type='text/css' media='screen' href='static/css_part.css'>
    <script src='main.js'></script>
</head>
<section>
    <article class = "Access documentation">
        <h2>This is an API made using a STEAM games database</h1>
        <p>You can access to the documentation here <a href="http://127.0.0.1:8000/docs"> Documentation</a></p>
    </article>
</section>
<section>
    <article class = "Contact">
        <h2>My name is Pablo Robba, you can contact me:</h2>
        <p><a href="https://www.linkedin.com/in/pablo-robba-9269a4267/"> <img src="static/Images_for_API/linkedin_logo.png" alt="linkedin_logo"></a>
        <a href="https://github.com/pablorobba"><img src="static/Images_for_API/github-logo.png" alt="github-logo"></a></p>
    </article>
</section>
<body>
    
</body>
</html>
    '''
    
def developer(developer: str):
    """This function shows the number of items and the percentage by year,
    by developer

    Args:
        developer (str): recibe el nombre de una empresa desarrolladora como cadena
    """
    aux = df_developer[["Year", "Total Items", "Percentage of Zero Price", "Developer"]]
    mask = aux.Developer == developer
    aux = df_developer[mask]
    
    years = aux["Year"].values
    num_items = aux["Total Items"].values
    percent_free_content = aux["Percentage of Zero Price"].values
    
    result = {"Year": years.tolist(), "Number of items": num_items.tolist(), "% of Free content": percent_free_content.tolist()}
    return result

def userdata(User_id : str):  
    """This function returns the money spent by the user 
    
        Args: 
            User_id (str): takes for argument his username as a string
    """
    mask = df_userdata["user_id"] == User_id
    df_userdata2 = df_userdata[mask]
    diccionary = {"User id": df_userdata2["user_id"].values[0], 
                  "Money spent": df_userdata2["money_spent"].values[0],
                  "recommendation %": df_userdata2["percentage_reviews"].values[0],
                  "amount of items":df_userdata2["items_count"].values[0]}
    return diccionary

def UserForGenre( genre : str ): 
    """Function that gives the user with more hours played by genre, and his hours played by year
    Args:
        genre (str): genre that you want to ask
    Returns:
        a diccionary with the values
    """
    mask = df_UserForGenre_genre["genre"] == genre      #first mask so we can save the argument given
    df_UserForGenre_genre2 = df_UserForGenre_genre[mask]    
    
    max_value = df_UserForGenre_genre2["playtime_genre"].max()  #to discover the max value
    mask2 = df_UserForGenre_genre2["playtime_genre"] == max_value
    
    df_UserForGenre_genre3 = df_UserForGenre_genre2[mask2]
    user_id = df_UserForGenre_genre3["user_id"].values[0]       # variable made to save the user_id who played most
    mask3 = df_UserForGenre_year["user_id"]  == user_id         #we make a mask with the user id
    df_UserForGenre_year2 = df_UserForGenre_year[mask3]         
    df_UserForGenre_year3 = df_UserForGenre_year2[["year","playtime_year"]]     #create a new df with  the columns we need
    df_UserForGenre_year3 = df_UserForGenre_year3.astype(str)               #put as a str so it dont take the years and the hours as floats, and express them in decimal values
    
    dictionary2 = {f"user with most hour played in the genre,{genre}" : user_id,
                   "hours played": df_UserForGenre_year3.values.tolist(),
                  }
    
    return dictionary2

def best_developer_year( year : int ): 
    """Gives top 3 developers with most recommended games by the users by year given

    Args:
        year (int): 

    Returns:
        diccionary
    """
    mask = df_best_developer_year["year"] == year       #we filter by year first, so we use less memory
    df_bd_year = df_best_developer_year[mask]
    df_bd_year.sort_values(by=["sentiment_analysis","recommend"], #it's sorted by the number of recommend by first
                           ascending=[False, False],               # criteria, and the sentiment analysis as second
                           inplace= True)
    df_bd_year.reset_index(drop = True, inplace= True)
    developer = df_bd_year["developer"]
    dictionary = [{"First": developer[0]},{"Second": developer[1]},{"Third": developer[2]}]
    
    return dictionary

def developer_reviews_analysis(developer : str ):     
    """Acorrding to the developer given returns the developer name and it's reviews (positive/negative)

    Returns:
        dicctionary
    """
    mask = df_developer_reviews_analysis["developer"] == developer
    df_developer_reviews_analysis2 = df_developer_reviews_analysis[mask]
    dev = df_developer_reviews_analysis2.developer.values[0]
    negative =  df_developer_reviews_analysis2["negative reviews"].values[0]
    positive =  df_developer_reviews_analysis2["positive reviews"].values[0]
    string = f"Negative = {negative}, Postive = {positive}"
    dictionary = {dev: [string]}
    
    return dictionary

def find_similar_games(item_id : int):
    """Cosine similarity machine learning enhanced query, 
        gives you 5 games according to the game(id) you give. For instance, Try: 342580"
    Args:
        item_id (int)
    Returns:
        _type_: list
    """
    #list to save the result of the loop
    list_ = []
    #the ML model, which a cosine_similarity
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(grouped_df['combined_columns'])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    cosine_sim_df = pd.DataFrame(cosine_sim, index=grouped_df['item_id'], columns=grouped_df['item_id'])

    
    game_index = grouped_df[grouped_df['item_id'] == item_id].index[0]  #save the index
    
    similar_scores = cosine_sim_df.iloc[game_index]     #make a series with the similar games
    
    similar_games = similar_scores.sort_values(ascending=False)   #order the game
    
    # We dont include the game that we passed (similarity 1.0, the highest one)
    similar_games = similar_games[1:6]
    index = similar_games.index.values      #save the index of the similar games
    for i in index:                             #took the index that we saved, loop them into a mask, use the mask to
        mask = grouped_df["item_id"] == i #save the values in a list and then return it                     
        list_.append(grouped_df[mask].item_name.values[0])
    return list_