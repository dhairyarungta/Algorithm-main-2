from utils import Node
from obstacle
from graph import Graph
from trip_planner import TripPlanner
import math
from copy import deepcopy

def main(input_str = "", args = None):
        # input_str sample ROB:20,20;OBS1:105,105,90;OBS2:155,65,90;OBS3:65,65,270;OBS4:195,105,180;OBS5:130,160,180
        carNode , obstacles = preprocess(input_str = input_str)
        graph = Graph(carNode)
        graph.constructGraph(obstacles)
        best_path = graph.bruteforce()
        greedy_path = graph.neartestNeighbour
        best_path_str = ""
        greedy_path_str = ""

        for item in best_path:
                best_path_str +=f"{item.key}->"
        
        for item in greedy_path:
                greedy_path_str += f"->{item.key}"

        
        print(f"Best path:{best_path_str}")
        print(f"Greedy Path: {greedy_path_str}")

        if args is not None:
                algo = TripPlanner(best_path, obstacles, args.use_inplace, int(args.padding))
        else :
                algo = TripPlanner(best_path, obstacles)
        stm_commands =[]
        android_commands =[]
        for item in best_path:
                item.x=round(item.x)
                item.y = round(item.y)
                print((item.x, item.y))
        
        current = best_path[0]
        path = ""
        corrections = []
        for next in range (1, len(best_path)):
    

def preprocess(input_str):
        
        objects = input_str.split(";")
        obstacles = []
        for item in objects:
                key, pos = item.split(":")
                if key =="ROB":
                        
                    posX, posY = list(map(int,pos.split(",")))
                    carNode = Node(key, posX, posY, theta=90)
                
                else:
                    posX , posY,pos_image = list(map(int,pos.split(",")))
                    print(posX, posY, pos_image)

                    obstacles.appned(Obstacle(key, posX, posY, pos_image))

        return carNode, obstacles
                        