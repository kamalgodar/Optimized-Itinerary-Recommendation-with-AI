# Import the libraries 
from tracemalloc import start
import numpy as np 
import pandas as pd

def recommend(places,place_id=1):
    top_dests_ktm=pd.read_csv("../Datasets/final_dest_ktm_with_duplicates_removed.csv")
    top_dests_ktm = top_dests_ktm[top_dests_ktm["title"].isin(places)]

    # select the first 95 destinations as they're the destinations having the latitude and longitude currently
    # top_dests_ktm=top_dests_ktm[:95]

    # let's just pick n=10 for now for better visualization
    n=len(top_dests_ktm) #graph size
    top_n_dests=top_dests_ktm[:n]

    # define a starting point 
    starting_point=1 #Bouddhanath

    duplicate_lat_long = top_n_dests[top_n_dests.duplicated(['latitude','longitude'])]

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

                #and store it in the 'graph' matrix
                graph[i][j]=distance_between_the_places
                #increment j 
                j+=1

            #increment i
            i+=1

    create_graph()

    # Define the initial parameters of ACO
    max_iter=100 #max no of iterations
    ant_no=10 #number of ants 

    #initial pheromone concentration
    tau_0=10*1/(n*np.mean(graph))

    #initial pheromone matrix
    tau = tau_0*np.ones((n,n))
    # print("Initial pheromone matrix (Tau):")
    # print(tau)

    #desirability/quality of each edge,eta
    eta=1/graph #inverse of cost (distance)
    # print("Desirability matrix (Eta):")
    # print(eta)

    rho=0.05 #evaporation rate
    alpha=2 #pheromone exponential parameter
    beta=1 #edge desirabiltu/quality exponential parameter

    # defining a function to create the ant colony 
    def create_colony(graph,node_no,ant_no,tau,eta,alpha,beta,initial_node):
        """
            creates an ant colony
        """
        # create a list called 'colony'
        # inside it, there will be ants ( represented by the indices)
        # each position contains other list called 'tour' that contains
        # the tour completed by each ant
        colony=[[] for _ in range(ant_no)] #size of the colony=no of ants
        
        # Run iterations equal to the number of ants 
        for i in range(ant_no):
            
            # define the initial node
            # we should take it as a parameter actually 
            # but let's take it random for now
            # initial_node=np.random.randint(0,node_no)
            
            # nope we changed our mind 
            initial_node=initial_node
            colony[i].append(initial_node)
            
            # print(colony)
            
            for j in range(node_no-1):
                #to choose the rest of the nodes
                
                #current node is the last node in the list
                current_node=int(colony[i][-1])
                
                #use the following formula to calculate the probability 
                p_all_nodes=(tau[current_node,:]**alpha)*(eta[current_node,:]**beta)
                
                #make the probability of the visited nodes 0
                for node in colony[i]:
                    p_all_nodes[node]=0
                    
                #calculate the final probability
                p=p_all_nodes/np.sum(p_all_nodes)
                
                #select the next node based on roulette wheel
                next_node=roulette_wheel(p)
                
                #append next node to the tour 
                #made by the ant in the colony
                colony[i].append(next_node)
                
            # to complete the tour, 
            # add the initial node to the end as well
            
            colony[i].append(initial_node)
        return colony

    # let's implement the roulette wheel function
    def roulette_wheel(prob_vec):
        """
            Selects the next node based on 
            the cumulative sum of the probabilities 
            in the probability vector
        """
        #cumulative version of the prob_vec (p)
        
        cum_sum_p=np.cumsum(prob_vec)
        
        #choose a random value from 0 to 1
        random_val=np.random.rand()
    #     print("random value:",random_val)
        
        #choose the first index as next_node in the probability vector
        #that has value more or equal to the random_val
        
    #     print("cum sum:",cum_sum_p)
        
        next_node = np.argwhere(cum_sum_p>=random_val)[0][0]
        
        #return the next_node
        return next_node

    def fitness_function(tour,graph):
        """
            calculates the fitness of the tour
            > basically, it's the sum of cost of all edges
            in the tour.
        """
        fitness=0
        
        for i in range(len(tour)-1):
            
            current_node=tour[i] # current node
            next_node=tour[i+1] # next node
            
            # add the cost of current edge (current_node->next_node)
            # to the overall fitness
            
            fitness = fitness + graph[current_node][next_node]
            
        return fitness

    def update_pheromone(tau,colony,fitness_list):
        """
            function to update the pheromone matrix
        """
        node_no=len(colony[1])
        ant_no=len(colony)
        
        for i in range(ant_no):
            # for each ant
            for j in range(node_no-1):
                # for each node in the tour 
                current_node=colony[i][j]
                next_node=colony[i][j+1]
                
                tau[current_node,next_node]=tau[current_node,next_node]+1/fitness_list[i]
                tau[next_node,current_node]=tau[next_node,current_node]+1/fitness_list[i]
        
        return tau

    # Main loop

    best_fitness=np.inf
    best_tour=[]

    for i in range(max_iter):
        # create ant colony
        colony=[] # store it as a list
        colony=create_colony(graph,n,ant_no,tau,eta,alpha,beta,starting_point)
        # print(f"Iteration #{i}:")
        
        # initializing fitness_list
        fitness_list=[0]*ant_no
        
        # calculate the fitness value of all ants
        for ant_i in range(ant_no):
            fitness_list[ant_i]=fitness_function(colony[ant_i],graph)
        
        # find the best ant 
        min_value=np.min(fitness_list)
        min_index=np.argmin(fitness_list) #best ant
        
        if min_value<best_fitness:
            # replace best_fitness even smaller min_value is found
            best_fitness=min_value
            best_tour=colony[min_index] #tour of the best ant
            
        # print("Best fitness: ",best_fitness)
        # print("Best tour: ",best_tour)
        
        # update phermone matrix
        tau=update_pheromone(tau,colony,fitness_list)
        
        # apply evaporation
        tau=(1-rho)*tau

    # display the names of destinations in the last tour
    # print("Best tour obtained:")
    # print(best_tour)

    places = top_n_dests['title'].iloc[best_tour]
    return places.tolist()

    # for i in best_tour:
    #     print(top_n_dests.iloc[i]["title"],end='')
    #     print("--->",end='')

    # #actual distance given by Vincenty distance using more accurate ellipsoidal models such as WGS-84 than Haversine
    # import geopy.distance
    # total_distance=0 #total actual distance

    # for i in range(len(best_tour)-1):
    #     coords_1 = (top_n_dests.iloc[best_tour[i]]["latitude"],top_n_dests.iloc[best_tour[i]]["longitude"])
    #     coords_2 = (top_n_dests.iloc[best_tour[i+1]]["latitude"],top_n_dests.iloc[best_tour[i+1]]["longitude"])
        
    #     #names of destinations connected
    #     src=top_n_dests.iloc[best_tour[i]]["title"]
    #     dest=top_n_dests.iloc[best_tour[i+1]]["title"]
    #     distance=geopy.distance.geodesic(coords_1, coords_2).km
    #     print (f'{str(src)+"->"+str(dest)}',distance)
    #     total_distance=total_distance+distance

    # print("Total distance(km): ",total_distance)

