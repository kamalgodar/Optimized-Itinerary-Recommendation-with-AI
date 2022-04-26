#Step 1: Import Dependencies
import numpy as np
import pandas as pd
import sklearn

#Step 2: Load the Data
destinations = pd.read_csv("sample_destinations.csv")

#Step 3: Data Cleaning and Exploration

#convert True/False categories to 1/0
converted=destinations.iloc[:,3:12].astype(int)

# drop columns in dataframe 
destinations.drop(destinations.columns[2:12],axis=1,inplace=True)

#concat the converted and original dataframe 
new_df=pd.concat([destinations,converted],axis=1)

new_df.iloc[:,2:12].sum()
#set 'destination_id' as index
new_df.set_index('destination_id',inplace=True)
# drop the 'title' column
new_df.drop(['title'],axis=1,inplace=True)
destination_features=new_df

#Step 4: Building a "Similar Destinations" Recommender Using Cosine Similarity
from sklearn.metrics.pairwise import cosine_similarity
cosine_sim = cosine_similarity(destination_features, destination_features)

from fuzzywuzzy import process

def destination_finder(title):
    all_titles = destinations['title'].tolist()
    closest_match = process.extractOne(title,all_titles)
    return closest_match[0]

destination_idx = dict(zip(destinations['title'], list(destinations.index)))

def get_content_based_recommendations(title_string, n_recommendations=10):
    title = destination_finder(title_string)
    idx = destination_idx[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:(n_recommendations+1)]
    similar_destinations = [i[0] for i in sim_scores]
    places = destinations['title'].iloc[similar_destinations]
    return places.tolist()

# get_content_based_recommendations('phewa taal')





