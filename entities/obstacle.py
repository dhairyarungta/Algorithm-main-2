import math 
from constants import OBS_DIM,FOCUS, WAYPOINT_THETA
# Assumption pos_x, pos_y is the centre of the obstacle 


class Obstacle:
    def __init__(self, key ="", pos_x =0, pos_y =0,pos_image = 0):
        self.key = key
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_image = pos_image #vector 

    
    def generate_waypoint (self,):
        pos_image = math.radians(self.pos_image)
        delta = (OBS_DIM//2 + FOCUS)
        pos_x = self.pos_x + math.cos(pos_image)*delta
        pos_y = self.pos_y + math.sin(pos_image)*delta

        theta = WAYPOINT_THETA[self.pos_image]
        ]return pos_x,pos_y,theta