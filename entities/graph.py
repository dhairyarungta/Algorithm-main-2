from typing import List
from utils import Node, Edge
from itertools import permutations
import math

class Graph:
    def __init__(self, carNode:Node):
        self.graph = {}
        self.carNode = carNode
        self.nodeMap = {}
        self.nodeMap[self.carNode.key] = carNode

    def _calc_dist(self, src:Node, dest:Node):
        # Using Manhattan distance
        delta_X = abs(src.x - dest.x)
        delta_Y = abs(src.y - dest.y)
        distance = delta_X + delta_Y
        return distance

    def _addEdge(self, src:Node, dest:Node):
        edge = Edge(src, dest, self._calc_dist(src,dest))
        if src.key not in self.graph:
            self.graph[src.key] = [edge]
        
        else:
            self.graph[src.key].append(edge)

    def constructGraph (self, obstacles:List):
        nodeList = [self.carNode]
        
        for obs in obstacles:
            posX, posY , theta = obs.generate_waypoint()
            nodeList.append(Node(obs.key, posX, posY, theta= theta))
            print(f"Waypoint of {obs.key}:{posX}, {posY}, {theta}")
        
        for i in range (len(nodeList)):
            self.nodeMap[nodeList[i].key] = nodeList[i]

            for j in range (i+1, len(nodeList)):
                self._addEdge(nodeList[i], nodeList[j])
                self._addEdge(nodeList[j], nodeList[i])

    def bruteforce(self,):
        # find all permutations and find the shortest one

        nodeList = []
        for item in self.graph:
            if self.nodeMap[item]!= self.carNode and item!=self.carNode.key:
                nodeList.append(self.nodeMap[item])
            
        minPathCost = float("inf")
        min_path_sequence = None 

        for path_sequence in list(permutations(nodeList)):
            pathCost = 0
            path_sequence  = [self.carNode]+list(path_sequence)
            for i in range (1, len(path_sequence)):
                pathCost +=self._calc_dist(paht_sequence[i-1], path_sequence[i])
            
            if pathCost<minPathCost:
                minPathCost = pathCost
                min_path_sequence = path_sequence
            
        return min_path_sequence

    def neartestNeighbour(self,):
        S = self.carNode
        path_sequence = [S]
        traversed = {}

        for item in self.graph:
            traversed[item]=  0
        
        traversed[S.key] = 1

        for i in range (len(self.graph)-1):
            nearestNode = None
            MIN_EDGE = float("inf")
            for edge in self.graph[S.key]:
                if edge.weight <MIN_EDGE and traversed [edge.dest.key]==0
                    MIN_EDGE = edge.weight
                    nearestNode= edge.dest
            

            S = nearestNode
            traversed[S.key] =1
            path_sequence.append(S)

        return path_sequence
    
