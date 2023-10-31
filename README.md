# STEAM API proyect

We are asked to take the rol of an MLOps (Machine Learning Operations) Engineer and develop an API with the datasets given:

+ [Datasets](https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj)

# Working process:
 
## ETL

We were given three datasets in a JSON format, with a lot of unnested data. We have to exploit the columns with the unnested data, look for null values, replace them, combina silimar columns with similar data, search and work with duplicated data.
Process in detail:
+ [ETL_process](https://github.com/pablorobba/STEAM_Individual_Proyect/blob/main/1%20-%20ETL_process.ipynb)

## Feature Engineering

First we made the sentiment analysis function just like was asked, and then we preparated the data for the API analysis. We made a csv for every query in the API (two in the case of one query) and cleaned them so the API can work problably.
Further details here:
+ [Feature_Engineering] (https://github.com/pablorobba/STEAM_Individual_Proyect/blob/main/2%20-%20Feature_%20Engineering.ipynb)

## API fuction testing

Here we made the API's functions in a jupyter notebook to taste them easily and to work with them in case of any particular problem while running the API.
The complete work here:
+ [API_function_testing] (https://github.com/pablorobba/STEAM_Individual_Proyect/blob/main/3%20-%20API_function_testing.ipynb)

## API development and deployement

First of all, we made a virtual enviorment, we installed the libraries. Then we chose to work with FastAPI, since it's an easy coding and high performance framework to make APIs. Use the same fuctions that we made in the former process, made a presentation function with and HTML and CSS for the main page and then we run the API locally.
Then we decided to work with Render, as it was sugested. Since it's a service with limitations for free users, we decided to put the API in another repository, yo can find it follow the next hyperlink:
+ [API_Repository] (https://github.com/pablorobba/API_Steam)
For the API live deployement, go to this page: https://steamapi-h3u0.onrender.com/ (maybe it can took a bit enter to the page)

## EDA

Here we explore the dataframe that we cleaned before. We explore the data searching for outliers, relationships with the data and general information of every dataframe. We saved a combined dataframe of the previous three with the most important columns.
Process in detail:
+ [EDA] (https://github.com/pablorobba/STEAM_Individual_Proyect/blob/main/4%20-%20EDA.ipynb)

## Machine learning

Lastly, we made the machine learning model. We decided to make a model that recommends games based on similarities on other games. For this purpose, we use a cosine similarity model, since it works well to analyse text. Based on how it works, we have to do a final csv of the data grouped by the id of the games and with a unique column with all the other text columns combined. Finally, We made a function for an API query with the machine learning model.
More info about the process here:
+ [Machine_Learning] (https://github.com/pablorobba/STEAM_Individual_Proyect/blob/main/5%20-%20Machine_Learning.ipynb)

## Uploading the repo

Since github dont allow to have more than 1 GB of git LFS files, we do not include in the repository the csv made and the original JSON. You can find the JSON's in the hyperlink at the beginning of the readme, download them and run the code to create the same csv that i have in PC.

## Posible upgrades

- Unfortunatly, the Machine learning  query works well locally but doesn't in the live page. This is because of render free acount limitations. Maybe this can be improved with further optimization. The rest of the works  fine.

- The ETL and EDA process were made very quick, so they are not very detailed and they some inconsistencies and repeated code. Possiblily, a more in depth ETL and EDA process could upgrade this work.

- The code in general is a bit messy (especially in the EDA/ETL process), a more neater code could be benefit to comprehend it.

- Make a full documentation of all the things done in the proyect

# Youtube video:

A video explaining briefly the work done (in spanish): 