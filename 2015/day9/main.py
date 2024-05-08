# Travelling Salesman Problem 
# https://en.wikipedia.org/wiki/Travelling_salesman_problem
import itertools
import math
import re

def distance(loc1, loc2, distances):
    return distances[loc1 + " to " + loc2]

def total_distance(route, distances):
    return sum(distance(route[i], route[i+1], distances) for i in range(len(route)-1))

def solve_tsp(locations, distances):
    shortest_distance = float('inf')
    shortest_route = None
    for route in itertools.permutations(locations):
        route_distance = total_distance(route, distances)
        if route_distance < shortest_distance:
            shortest_distance = route_distance
            shortest_route = route
    return shortest_distance, shortest_route

def read_input(filename):
    locations = set()
    distances = {}
    with open(filename, 'r') as f:
        for line in f:
            match = re.match(r"(\w+) to (\w+) = (\d+)", line)
            if match:
                loc1, loc2, dist = match.groups()
                locations.add(loc1)
                locations.add(loc2)
                distances[loc1 + " to " + loc2] = int(dist)
                distances[loc2 + " to " + loc1] = int(dist)
    return list(locations), distances

locations, distances = read_input('input.txt')
shortest_distance, shortest_route = solve_tsp(locations, distances)
print("Shortest distance: " + str(shortest_distance))
print("Shortest route: " + " -> ".join(shortest_route))