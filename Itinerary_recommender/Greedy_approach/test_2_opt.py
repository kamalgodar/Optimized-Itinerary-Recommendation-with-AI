from py2opt.routefinder import RouteFinder

cities_names = ['A', 'B', 'C', 'D']
dist_mat = [[0, 29, 15, 35], [29, 0, 57, 42], [15, 57, 0, 61], [35, 42, 61, 0]]
route_finder = RouteFinder(dist_mat, cities_names, iterations=5)
best_distance, best_route = route_finder.solve()

print(best_distance)
print(best_route)
