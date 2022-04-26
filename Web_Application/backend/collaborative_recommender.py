#Step 1: Import the Dependencies

import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt

#Step 2: Load the Data
destinations = pd.read_csv("sample_destinations.csv")
ratings=pd.read_csv("sample_user_ratings.csv")

#Step 3: Exploratory Data Analysis
n_ratings = len(ratings)
n_destinations = ratings['destination_id'].nunique() #unique rated destinations
n_users = ratings['user_id'].nunique()

#Destinations with the lowest and highest average rating
mean_rating = ratings.groupby('destination_id')[['rating']].mean()
lowest_rated = mean_rating['rating'].idxmin()
destinations[destinations['destination_id'] == lowest_rated]

highest_rated = mean_rating['rating'].idxmax()
destinations[destinations['destination_id'] == highest_rated]

#Bayesian Average
destination_stats = ratings.groupby('destination_id')[['rating']].agg(['count', 'mean'])
destination_stats.columns = destination_stats.columns.droplevel()

C = destination_stats['count'].mean()
m = destination_stats['mean'].mean()

def bayesian_avg(ratings):
    bayesian_avg = (C*m+ratings.sum())/(C+ratings.count())
    return bayesian_avg

bayesian_avg_ratings = ratings.groupby('destination_id')['rating'].agg(bayesian_avg).reset_index()
bayesian_avg_ratings.columns = ['destination_id', 'bayesian_avg']
destination_stats = destination_stats.merge(bayesian_avg_ratings, on='destination_id')

destination_stats = destination_stats.merge(destinations[['destination_id', 'title']])
destination_stats.sort_values('bayesian_avg', ascending=False).head()

#Destinations with the least Bayesian averages
destination_stats.sort_values('bayesian_avg', ascending=True).head()

#Destinations with the highest Bayesian averages
destination_stats.sort_values('bayesian_avg', ascending=False).head()

#Step 4: Transforming the data
from scipy.sparse import csr_matrix

def create_X(df):
    """
    Generates a sparse matrix from ratings dataframe.
    
    Args:
        df: pandas dataframe
    
    Returns:
        X: sparse matrix
        user_mapper: dict that maps user id's to user indices
        user_inv_mapper: dict that maps user indices to user id's
        destination_mapper: dict that maps destination id's to movie indices
        destination_inv_mapper: dict that maps destination indices to movie id's
    """
    N = df['user_id'].nunique()
    M = df['destination_id'].nunique()

    user_mapper = dict(zip(np.unique(df["user_id"]), list(range(N))))
    destination_mapper = dict(zip(np.unique(df["destination_id"]), list(range(M))))
    
    user_inv_mapper = dict(zip(list(range(N)), np.unique(df["user_id"])))
    destination_inv_mapper = dict(zip(list(range(M)), np.unique(df["destination_id"])))
    
    user_index = [user_mapper[i] for i in df['user_id']]
    destination_index = [destination_mapper[i] for i in df['destination_id']]

    X = csr_matrix((df["rating"], (destination_index, user_index)), shape=(M, N))
    
    return X, user_mapper, destination_mapper, user_inv_mapper, destination_inv_mapper

X, user_mapper, destination_mapper, user_inv_mapper, destination_inv_mapper = create_X(ratings)

sparsity = X.count_nonzero()/(X.shape[0]*X.shape[1])

from scipy.sparse import save_npz

save_npz('user_item_matrix.npz', X)

#Step 5: Finding similar destinations using k-Nearest Neighbours
from sklearn.neighbors import NearestNeighbors

def find_similar_destinations(destination_id, X, k, metric='cosine', show_distance=False):
    """
    Finds k-nearest neighbours for a given destination id.
    
    Args:
        destination_id: id of the destination of interest
        X: user-item utility matrix
        k: number of similar destinations to retrieve
        metric: distance metric for kNN calculations
    
    Returns:
        list of k similar destination ID's
    """
    neighbour_ids = []
    
    destination_ind = destination_mapper[destination_id]
    destination_vec = X[destination_ind]
    k+=1
    kNN = NearestNeighbors(n_neighbors=k, algorithm="brute", metric=metric)
    kNN.fit(X)
    if isinstance(destination_vec, (np.ndarray)):
        destination_vec = destination_vec.reshape(1,-1)
    neighbour = kNN.kneighbors(destination_vec, return_distance=show_distance)
    for i in range(0,k):
        n = neighbour.item(i)
        neighbour_ids.append(destination_inv_mapper[n])
    neighbour_ids.pop(0)
    return neighbour_ids

destination_titles = dict(zip(destinations['destination_id'], destinations['title']))

def recommender(destination_id):
    recommended_places = []
    similar_ids = find_similar_destinations(destination_id, X, k=10)
    for i in similar_ids:
        recommended_places.append(destination_titles[i])
    return recommended_places
    


