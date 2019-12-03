#pseudocode used https://en.wikipedia.org/wiki/A*_search_algorithm
# priority reference https://www.redblobgames.com/pathfinding/a-star/implementation.html
# heapq https://docs.python.org/3.0/library/heapq.html

import heapq 
from math import sqrt

def shortest_path(M,start,goal):
    print("shortest path called")

    closedSet = set()
    openSet = [(fScore, start)] #set ([start])
    cameFrom = {} #empty dictionary
    
    gScore = {x: float('inf') for x in M.intersections.keys()}
    gScore[start] = 0
    
    fScore = {x: float('inf') for x in M.intersections.keys()}

    fScore[start] = heuristic_cost_estimate(M.intersections[start], M.intersections[goal]) #gscore + heuristic

    while openSet: 
        current = heappop(openSet)[1] #min(openSet, key=fScore.get)
        
        if current == goal:
            return reconstruct_path(cameFrom, current)
        
        #openSet.remove(current)
        closedSet.add(current)

        for neighbor in M.roads[current]:
            tentative_gScore = gScore[current] + heuristic_cost_estimate(M.intersections[current], M.intersections[neighbor])
            #if neighbor not in closedSet or tentative_gScore >= gScore[neighbor]:
                            
            heapq.heappush(openSet, (fScore,neighbor))  
            cameFrom[neighbor] = current
            gScore[neighbor] = tentative_gScore
            fScore[neighbor] = gScore[neighbor] + heuristic_cost_estimate(M.intersections[neighbor], M.intersections[goal]) 

    return cameFrom, gScore[current]

def heuristic_cost_estimate(point1, point2):
	x1,y1 = point1
	x2,y2 = point2
	return sqrt((x2-x1)**2 + (y2-y1)**2)

def reconstruct_path(cameFrom, current):
    total_path = [current]
    while current in cameFrom.keys():
        current = cameFrom[current]
        total_path.append(current)
    total_path.reverse()
    return total_path