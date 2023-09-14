from obstacle import Obstacle
from collision import CollisionDetector
from utils import Node
from constants import TR, TURN_PADDING
import math


class Turn_Simulator:
    def __init__(self,padding, iter_theta = 5,collision_detector :CollisionDetector= None):
        self.padding = padding 
        self.iter_theta = iter_theta
        self.ellipse_a, self.ellipse_b = TR["90 Turn"]
        self.collison_detector = collision_detector

    def _returnMeta (self, currentNode:Node, turn_where="forward-right"):
        
        x, y, theta =currentNode.x, currentNode.y, currentNode.theta
        st, dir = turn_where.split("-")
        center = {
            0: {
                "forward-left": lambda x,y: (x, y+self.ellipse_a),
                "forward-right": lambda  x,y: (x, y-self.ellipse_a),
                "backward-left": lambda x,y: (x, y+self.ellipse_b),
                "backward-right": lambda x,y: (x, y-self.ellipse_b)
            },
            180: {
                "forward-left": lambda x,y: (x, y-self.ellipse_a),
                "forward-right": lambda  x,y: (x, y+self.ellipse_a),
                "backward-left": lambda x,y: (x, y-self.ellipse_b),
                "backward-right": lambda x,y: (x, y+self.ellipse_b)
            },
            90: {
                "forward-left": lambda x,y: (x-self.ellipse_a, y),
                "forward-right": lambda  x,y: (x+self.ellipse_a, y),
                "backward-left": lambda  x,y: (x-self.ellipse_b, y),
                "backward-right": lambda  x,y: (x+self.ellipse_b, y),
            },
            270: {
                "forward-left": lambda x,y: (x+self.ellipse_a, y),
                "forward-right": lambda  x,y: (x-self.ellipse_a, y),
                "backward-left": lambda  x,y: (x+self.ellipse_b, y),
                "backward-right": lambda  x,y: (x-self.ellipse_b, y),
            }
        }

        axes = {
            0: {
                "forward":(self.ellipse_b, self.ellipse_a),
                "backward":((self.ellipse_a, self.ellipse_b))
                },
            180: { 
                "forward": (self.ellipse_b, self.ellipse_a),
                "backward":(self.ellipse_a, self.ellipse_b)

                },
            90: {
                "forward":(self.ellipse_a, self.ellipse_b),
                "backward":(self.ellipse_b, self.ellipse_a)
                },
            270: {
                "forward":(self.ellipse_a, self.ellipse_b),
                "backward":(self.ellipse_b, self.ellipse_a)
                }

        }

        simulate_angles = {
            0: {
                "forward-left": (-90,0),
                "forward-right": (90,0),
                "backward-left":  (270,180),
                "backward-right": (90, 180)
            },
            180: {
                "forward-left": (90, 180),
                "forward-right": (270,180),
                "backward-left": (90,0),
                "backward-right": (-90,0)
            },
            90: {
                "forward-left": (0,90),
                "forward-right": (180,90),
                "backward-left": (0,-90),
                "backward-right": (180,270)
            },
            270: {
                "forward-left": (180,270),
                "forward-right": (0,-90),
                "backward-left": (180,90),
                "backward-right": (0,90)
            }
        }

        next_theta = {
            0: {
                "forward-left": 90,
                "forward-right": 270,
                "backward-left": 270,
                "backward-right": 90
            },
            180: {
                "forward-left": 270,
                "forward-right": 90,
                "backward-left": 90,
                "backward-right": 270
            },
            90: {
                "forward-left": 180,
                "forward-right": 0,
                "backward-left": 0,
                "backward-right": 180
            },

            270: {
                "forward-left": 0,
                "forward-right": 180,
                "backward-left": 180,
                "backward-right": 0
            }

        }

        return center[theta][turn_where](x,y), axes[theta][st], simulate_angles[theta][turn_where], next_theta[theta][turn_where]




    def checkTurn(self, currentNode:Node, turn_where = "forward-right"):    
        center, sides, simulate_angles, next_theta = self._returnMeta(currentNode, turn_where)  
        h,k = center
        a,b = sides
        open_angle, close_angle = simulate_angles
        #print(a,b)
        #print(open_anlge,close_angle)

        if(open_angle>close_angle):
            iter_theta = -self.iter_theta
        else :
            iter_theta = self.iter_theta
        
        for theta in range(open_angle, close_angle+(iter_theta//abs(iter_theta)), iter_theta):
            #print(theta)
            x = round(a*math.cos(math.radians(theta)) + h,2)
            y = round(b*math.sin(math.radians(theta)) + k,2)
            

            intermediate_state = Node("DUMMY", x, y, currentNode.theta)
            #print(self.padding)
            if theta != open_angle and theta != close_angle:
                padding = self.padding
            else:
                padding = 0
            
            #print(padding)
            if not self.collision_detector.checkStateIsValid(intermediate_state, padding) :
                # print(intermediate_state.x, intermediate_state.y)
                return False, None
            
            
        intermediate_state.theta = next_theta
        intermediate_state.x = round(intermediate_state.x)
        intermediate_state.y= round(intermediate_state.y)
        # print(intermediate_state.x, intermediate_state.y)
        return True, intermediate_state



def test (theta):
    #Test 0
    currentNode = Node("STATE", 15, 135, theta =theta)  
    obstacle_list = [Obstacle("A",200,135,90)]

    turn_sim = Turn_Simulator(iter_theta=5, collision_detector=CollisionDetector(obstacle_list))

    print ("FORWARD RIGHT")
    print(turn_sim.checkTurn(currentNode, turn_where= "forward-right"))

    print ("FORWARD LEFT")
    print(turn_sim.checkTurn(currentNode, turn_where= "forward-left"))

    print ("BACKWARD RIGHT")
    print(turn_sim.checkTurn(currentNode, turn_where= "backward-right"))

    print ("BACKWARD LEFT")
    print(turn_sim.checkTurn(currentNode, turn_where= "backward-left"))



if __name__ == "__main__":
    #test(0)
    test(90)
    #test(180)
    #test(270)