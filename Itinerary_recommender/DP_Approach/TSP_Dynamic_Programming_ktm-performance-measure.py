#!/usr/bin/env python
# coding: utf-8

# # Solving TSP with Dynamic Programming

# ### Import the required libraries

# In[1]:


import sys
import copy
import numpy as np 
import pandas as pd
from matplotlib import pyplot as plt


# In[2]:


top_dests_ktm=pd.read_csv("../../Datasets/destinations_of_kathmandu_updated_with_latlong.csv")
print(top_dests_ktm.head())


# In[3]:


# select the first 95 destinations as they're the destinations having the latitude and longitude currently
top_dests_ktm=top_dests_ktm[:95]
print(top_dests_ktm.tail())


# In[4]:


# let's just pick n=10 for now for better visualization
n=25 #graph size
top_n_dests=top_dests_ktm[:n]
print(top_n_dests)


# In[5]:


# since we'll be dealing only with latitude and longitude at the moment
# only filter those columns along with the title
print(top_dests_ktm[['title','latitude','longitude']])


# In[6]:


# also meanwhile let's create a matrix called 'graph' to store the weights for each edges
graph=np.zeros((n,n))

def create_graph():

    # iterators to iterate through the graph
    i=0
    j=0

    for lat,long in zip(top_n_dests['latitude'].astype(float),top_n_dests['longitude'].astype(float)):
        j=0
        for another_lat,another_long in zip(top_n_dests['latitude'].astype(float),top_n_dests['longitude'].astype(float)):
            #edge weight(Euclidean distance)
            distance_between_the_places=np.sqrt((lat-another_lat)**2+(long-another_long)**2)
            #print(distance_between_the_places)

            #and store it in the 'graph' matrix
            graph[i][j]=distance_between_the_places
            #increment j 
            j+=1

        #increment i
        i+=1


# In[7]:


create_graph()
print(graph)


# In[8]:


# input matrix containing cost
matrix = graph
# input data points
data = list(range(1,n+1))


# In[9]:


# initializing necessary parameters
all_sets = []
g = {}
p = []
starting_node=1


# In[10]:


def main():
    """
        Main function
    """
    
    route=[] #to store the final route
    
    for x in range(1, n):
        g[x + 1, ()] = matrix[x][0]
    
    # minimum cost
    min_cost=get_minimum(starting_node, tuple(range(2,n+1)))
#     print("Miniumum cost: ",min_cost)
#     print('\n\nSolution to TSP: {1, ', end='')
    
    route.append(1) #append the starting node
    
    solution = p.pop()
#     print(solution[1][0], end=', ')
    route.append(solution[1][0])
    for x in range(n - 2):
        for new_solution in p:
            if tuple(solution[1]) == new_solution[0]:
                solution = new_solution
                print(solution[1][0], end=', ')
                route.append(solution[1][0])
                break
#     print('1}')
    route.append(1)#append the ending node (same as starting node)
#     print(route)
    return route


# In[11]:


def get_minimum(k, a):
    """
        Get the minimum cost
    """
    if (k, a) in g:
        # Already calculated Set g[%d, (%s)]=%d' % (k, str(a), g[k, a]))
        return g[k, a]

    values = []
    all_min = []
    for j in a:
        set_a = copy.deepcopy(list(a))
        set_a.remove(j)
        all_min.append([j, tuple(set_a)])
        result = get_minimum(j, tuple(set_a))
        values.append(matrix[k-1][j-1] + result)

    # get minimun value from set as optimal solution for
    g[k, a] = min(values)
    p.append(((k, a), all_min[values.index(g[k, a])]))

    return g[k, a]


# In[ ]:


if __name__ == '__main__':
    import time
    t_in=time.time()
    route=main()
    t_out=time.time()
    print(route)


# In[ ]:


#cross-checking the total cost
total_cost=0 #initialize total cost to 0
for i in range(0,len(route)-1):
    total_cost=total_cost+matrix[route[i]-1][route[i+1]-1]
print(total_cost)


# In[ ]:


for i in route:
    print(top_n_dests.iloc[i-1]["title"],end='')
    print("--->",end='')


# In[ ]:


#actual distance given by Vincenty distance using more accurate ellipsoidal models such as WGS-84 than Haversine
import geopy.distance
total_distance=0 #total actual distance

for i in range(len(route)-1):
    coords_1 = (top_n_dests.iloc[route[i]-1]["latitude"],top_n_dests.iloc[route[i]-1]["longitude"])
    coords_2 = (top_n_dests.iloc[route[i+1]-1]["latitude"],top_n_dests.iloc[route[i+1]-1]["longitude"])
    
    #names of destinations connected
    src=top_n_dests.iloc[route[i]-1]["title"]
    dest=top_n_dests.iloc[route[i+1]-1]["title"]
    distance=geopy.distance.geodesic(coords_1, coords_2).km
    print (f'{str(src)+"->"+str(dest)}',distance)
    total_distance=total_distance+distance

print("Total distance(km): ",total_distance)
print(t_out-t_in)


# In[ ]:




