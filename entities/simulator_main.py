
from utils import Node
from obstacle import Obstacle
from graph import Graph
from trip_planner import TripPlanner
import math
from copy import deepcopy

def main(input_str = "ROB:20,20;OBS1:105,105,90;OBS2:155,65,90;OBS3:65,65,270;OBS4:195,105,180;OBS5:130,160,180"):

    # input_str = input()

    carNode, obstacles = preprocess(input_str= input_str)

    graph = Graph(carNode)
    graph.constructGraph(obstacles)

    best_path = graph.bruteforce()
    greedy_path = graph.nearestNeighbour()
    best_path_str, greedy_path_str = "", ""

    for item in best_path:
        best_path_str += f"{item.key}->"
    
    for item in greedy_path:
        greedy_path_str += f"->{item.key}"

    

    print(f"Best path:{best_path_str}")
    print(f"Greedy Path: {greedy_path_str}")

    algo = TripPlanner(best_path, obstacles)
    stm_commands = []
    android_commands = []
    for item in best_path:

        item.x = round(item.x)
        item.y = round(item.y)
        print((item.x, item.y))

    current = best_path[0]
    path = ""
    number = 0
    for next in range (1,len(best_path)):

        dest = deepcopy(best_path[next])
        
        print("First Try:")
        print(((current.x,current.y), (dest.x,dest.y)))
        trip = algo.planTripAStar(current, dest)
        if len(trip) == 0:
            dest = deepcopy(best_path[next])
            dest.x = dest.x + int(10*math.cos(math.radians(dest.theta)))
            dest.y = dest.y + int(10*math.sin(math.radians(dest.theta)))
            print("Second try:")
            print(((current.x,current.y), (dest.x,dest.y)))
            trip = algo.planTripAStar(current, dest)
            if len(trip) == 0:
                dest = deepcopy(best_path[next])
                dest.x = dest.x - int((10*math.cos(math.radians(dest.theta))))
                dest.y = dest.y - int(10*math.sin(math.radians(dest.theta)))
                print(((current.x,current.y), (dest.x,dest.y)))
                print ("Third Try:")
                trip = algo.planTripAStar(current, dest)
                if len(trip) == 0:
                    continue
        path += f"{dest.key}->"
        stm_instr = algo.generateInstructions(trip, device = "stm")
        stm_commands += stm_instr
        stm_commands.append("CAPTURE 20")
        number += 1
        current = dest

    print(f"Yay! We found {number} obstacles")
    

    return stm_commands


def preprocess(input_str):

    objects = input_str.split(";")

    obstacles = []

    for item in objects:

        key, pos = item.split(":")

        if key == "ROB":

            posX, posY = list(map(int,pos.split(",")))
            carNode = Node(key, posX, posY, theta= 90)
        else:

            posX, posY, pos_image = list(map(int,pos.split(",")))
            print(posX,posY,pos_image)
            
            obstacles.append(Obstacle(key, posX, posY, pos_image))
    return carNode, obstacles 




    






if __name__ == "__main__":

    print(main('ROB:15,15;OBS1:55,75,270;OBS2:125,95,0;OBS3:145,45,90;OBS4:145,155,270;OBS5:55,135,180'))
    #print(main('ROB:15,15;OBS1:15,115,90;OBS2:105,45,0;OBS3:195,15,90;OBS4:135,105,270;OBS5:105,115,180;OBS6:155,145,270;OBS7:75,175,180'))

    #print(main("ROB:15,15;OBS1:125,5,0;OBS2:135,155,270;OBS3:85,5,180;OBS4:145,45,90"))
