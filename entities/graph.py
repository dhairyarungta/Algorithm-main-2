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
            