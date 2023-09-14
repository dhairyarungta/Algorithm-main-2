
from typing import List
from inplace_simulator import Inplace_Simulator
from collision import CollisionDetector
from turn_simulator import Turn_Simulator
from error_calibrator import Error_Calibrator
from math import pi
from utils import Node
import math
from heapq import heapify, heappush, heappop

# importing the constants 
# ensure delta_st is less than 30 or else the code will break
from constants import DELTA_ST,INPLACE_TURN_WEIGHT, STM_COMMANDS, ANDROID_COMMANDS, TURN_PADDING

# Add instuctions after moving to the co-ordinate 
# make a seperate function for that 

class TripPlanner:

    def __init__(self, path_sequence, obstacles: List, inplace = True, padding = TURN_PADDING):

        self.path_sequence = path_sequence
        self.collision_detector = CollisionDetector(obstacles)
        self.turn_sim = Turn_Simulator(collision_detector = self.collision_detector, iter_theta= 5, padding= padding)
        self.inplace_sim = Inplace_Simulator(collision_detector= self.collision_detector)
        self.obstacles = obstacles
        self.error_calibrator = Error_Calibrator(collision_detector=self.collision_detector)
        self.inplace = inplace

    def _moveForward(self, node:Node):

        return Node(node.key, int(node.x + (DELTA_ST*math.cos(math.radians(node.theta)))), int(node.y + (DELTA_ST*math.sin(math.radians(node.theta)))),node.theta)
    
    def _moveBackward(self, node:Node):

        return Node(node.key, int(node.x - (DELTA_ST*math.cos(math.radians(node.theta)))), int(node.y - (DELTA_ST*math.sin(math.radians(node.theta)))),node.theta)

    def _expandNodeBFS(self,node: Node)-> List:

        states = []


        forward = self._moveForward(node)
        if self.collision_detector.checkStateIsValid(forward):

            states.append(forward)
        
        backward = self._moveBackward(node)
        if self.collision_detector.checkStateIsValid(backward ):

            states.append(backward)

        turns = ["forward-right", "forward-left", "backward-left", "backward-right"]

        for turn in turns:

            flag, next_state = self.turn_sim.checkTurn(currentNode=node, turn_where=turn)
            if flag:
                states.append(next_state)

        # INSERT code for Inplace turns

        inplace_turns = ["left", "right"]
        if self.inplace:
            for turn in inplace_turns:

                flag, next_state = self.inplace_sim.checkTurn(currentNode=node, turn_where=turn)
                if flag:
                    states.append(next_state)

        return states

    def generateInstructions(self, coordinates:  List, device = "stm"):
        if device == "android":
            COMMANDS = ANDROID_COMMANDS
        elif device == "stm":
            COMMANDS = STM_COMMANDS
        instructions = []
        delta = 0
        dummy_pt = f"200 200 -360" # for getting the final forward or reverse
        coordinates.append(dummy_pt)
        for i in range (len(coordinates)-1):
            currentx, currenty, currenttheta = list(map(int,coordinates[i].split(" ")))
            nextx, nexty, nexttheta = list(map(int,coordinates[i+1].split(" ")))
    
            if currenttheta == 0:
            
                if nexttheta == currenttheta:
                    
                    delta += (nextx - currentx)
                    
                    continue

                else:

                    if delta > 0:
                        instructions.append(f"{COMMANDS['F']} {delta}")
                    elif delta < 0:
                        instructions.append(f"{COMMANDS['B']} {-delta}")
                    delta = 0

                    if nexttheta == 90:

                        if nextx > currentx:
                            instructions.append(f"{COMMANDS['FTL']}")
                        if nextx < currentx:
                            instructions.append(f"{COMMANDS['BTR']}")
                        if nextx == currentx and nexty == currenty:
                            instructions.append(f"{COMMANDS['ILEFT']}")
                    
                    if nexttheta == 270:
                    
                        if nextx > currentx:
                            instructions.append(f"{COMMANDS['FTR']}")
                        if nextx < currentx:
                            instructions.append(f"{COMMANDS['BTL']}")
                        if nextx == currentx and nexty == currenty:
                            instructions.append(f"{COMMANDS['IRIGHT']}")
            
            elif currenttheta == 90:
                if nexttheta == currenttheta:
                    
                    delta += (nexty - currenty)
                    continue

                else:

                    if delta > 0:
                        instructions.append(f"{COMMANDS['F']} {delta}")
                    elif delta < 0:
                        instructions.append(f"{COMMANDS['B']} {-delta}")
                    delta = 0

                    if nexttheta == 0:

                        if nextx > currentx:
                            instructions.append(f"{COMMANDS['FTR']}")
                        if nextx < currentx:
                            instructions.append(f"{COMMANDS['BTL']}")
                        if nextx == currentx and nexty == currenty:
                            instructions.append(f"{COMMANDS['IRIGHT']}")
                    
                    if nexttheta == 180:

                        if nextx < currentx:
                            instructions.append(f"{COMMANDS['FTL']}")
                        if nextx > currentx:
                            instructions.append(f"{COMMANDS['BTR']}")
                        if nextx == currentx and nexty == currenty:
                            instructions.append(f"{COMMANDS['ILEFT']}")
            
            elif currenttheta == 180:
                if nexttheta == currenttheta:
                    
                    delta += (currentx - nextx)
                    continue

                else:

                    if delta > 0:
                        instructions.append(f"{COMMANDS['F']} {delta}")
                    elif delta < 0:
                        instructions.append(f"{COMMANDS['B']} {-delta}")
                    delta = 0

                    if nexttheta == 90:

                        if nextx < currentx:
                            instructions.append(f"{COMMANDS['FTR']}")
                        if nextx > currentx:
                            instructions.append(f"{COMMANDS['BTL']}")
                        if nextx == currentx and nexty == currenty:
                            instructions.append(f"{COMMANDS['IRIGHT']}")
                    
                    if nexttheta == 270:

                        if nextx < currentx:
                            instructions.append(f"{COMMANDS['FTL']}")
                        if nextx > currentx:
                            instructions.append(f"{COMMANDS['BTR']}")
                        if nextx == currentx and nexty == currenty:
                            instructions.append(f"{COMMANDS['ILEFT']}")

            elif currenttheta == 270:
                if nexttheta == currenttheta:
                    
                    delta += (currenty - nexty)
                    continue

                else:

                    if delta > 0:
                        instructions.append(f"{COMMANDS['F']} {delta}")
                    elif delta < 0:
                        instructions.append(f"{COMMANDS['B']} {-delta}")
                    delta = 0

                    if nexttheta == 180:

                        if nextx < currentx:
                            instructions.append(f"{COMMANDS['FTR']}")
                        if nextx > currentx:
                            instructions.append(f"{COMMANDS['BTL']}")
                        if nextx == currentx and nexty == currenty:
                            instructions.append(f"{COMMANDS['IRIGHT']}")
                    
                    if nexttheta == 0:

                        if nextx > currentx:
                            instructions.append(f"{COMMANDS['FTL']}")
                        if nextx < currentx:
                            instructions.append(f"{COMMANDS['BTR']}")
                        if nextx == currentx and nexty == currenty:
                            instructions.append(f"{COMMANDS['ILEFT']}")

            
        return instructions
                    

    def _computeManhattan(self,node1: Node, node2: Node):

        #theta_diff = abs(node1.theta - node2.theta)
        x_diff = round(abs (node1.x - node2.x))
        y_diff = round(abs (node1.y - node2.y))

        if x_diff + y_diff == 0:
            return INPLACE_TURN_WEIGHT

        return x_diff + y_diff
    
    def _tracePath(self, stateDict:dict, goalNode: Node):
        gx, gy, gtheta = goalNode.x, goalNode.y, goalNode.theta

        path = []

        if f"{gx} {gy} {gtheta}" not in stateDict:
            return path
        
        else:
            current = f"{gx} {gy} {gtheta}" 

            while (True):

                _, node = stateDict[current]

                path.append(current)

                parent = node.parent

                if parent is None:

                    return path [::-1]
                current = f"{parent.x} {parent.y} {parent.theta}"

        



    def planTripAStar(self, startNode: Node, goalNode: Node):

        # Astar Algorithm with manhattan distance as heuristic

        # A map to represent closed list 

        # A minheap to represent the open list


        closed_list = {}
        open_list = [(0, startNode)]
        stateDetails = {}
        dist_sg = self._computeManhattan(startNode, goalNode)
        startNode.h = dist_sg
        stateDetails[f"{startNode.x} {startNode.y} {startNode.theta}"] = (f"{dist_sg} 0 {dist_sg}", startNode)
        heapify(open_list)

        while (len(open_list) != 0):
            
            f,current = heappop(open_list)
            adj = self._expandNodeBFS(current)
            current_hash = f"{current.x} {current.y} {current.theta}"
            _, gparent, __ = list(map(int,stateDetails[current_hash][0].split(" ")))

            for successor in adj:

                successor.parent = current
                gnew = gparent + self._computeManhattan(successor, current)
                hnew = self._computeManhattan(successor, goalNode)
                fnew = gnew + hnew 
                successor.h = hnew
                successor_hash = f"{successor.x} {successor.y} {successor.theta}"
                if successor == goalNode:
                    # return stateDetails
                    stateDetails[successor_hash] = (f"{fnew} {gnew} {hnew}", successor)
                    print ("Yay!!! We found a solution")
                    path = self._tracePath(stateDetails, goalNode)
                    return path
                elif closed_list.get(successor_hash) == False or closed_list.get(successor_hash) is None:

                    if successor_hash not in stateDetails:
                        heappush(open_list, (fnew, successor))
                        stateDetails[successor_hash] = (f"{fnew} {gnew} {hnew}", successor)
                        
                    else:
                        fold = int(stateDetails[successor_hash][0].split(" ")[0])

                        if fnew < fold:
                            heappush(open_list, (fnew, successor))
                            stateDetails[successor_hash] = (f"{fnew} {gnew} {hnew}", successor)
                elif closed_list.get(successor_hash) == True:
                    fold = int(stateDetails[successor_hash][0].split(" ")[0])

                    if fnew < fold:
                        closed_list[successor_hash] = False
                        heappush(open_list, (fnew, successor))
                        stateDetails[successor_hash] = (f"{fnew} {gnew} {hnew}", successor)

            closed_list [current_hash] = True
        
        # Algo failed which is impossible as Astar is complete 
        print ("Oops! No solution found")
        print(f"No of states searched: {len(closed_list)}")
        #print(current.x, current.y, current.theta)
        return []




    def planTripBFS(self,startNode: Node , goalNode: Node):


        # breadth first search algorithm (Simple and Naive BackTracking)
        
        queue = [[startNode]]
        level = 0
        visited = {}

        while (len(queue) != 0):
            
            path = queue.pop(0)
            

            if len(path) > level:
                level += 1
                print(f"Level: {level}")

            newNode = path[-1]

            if f"{newNode.x}, {newNode.y}, {newNode.theta}" in visited:
                continue

            if newNode == goalNode:
                #print(f"Trip from {startNode.key} to {goalNode.key}: {path}")
                return path
            
            adj = self._expandNodeBFS(newNode)

            #print(adj)

            for item in adj:

                newPath = path [:]
                # if item not in newPath:
                newPath.append(item)

                queue.append(newPath)
            
            visited[f"{newNode.x}, {newNode.y}, {newNode.theta}"] = True

        
        print(f"No of states searched: {len(visited)}")
        print(newNode.x, newNode.y, newNode.theta)
        return []
    
        



            

        


        





        