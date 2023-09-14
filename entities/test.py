from typing import List
from obstacle import Obstacle  
from math import pi
from utils import Node
from heapq import heapify, heappush, heappop
from obstacle import TripPlanner    

#testing 
#test 1

startNode = Node("START", 80, 60, 90)
goalNode = Node("GOAL", 80, 85, 90)

obs = [Obstacle("2", 140, 85, 0)]
path = []

algo = TripPlanner(path, obs)

