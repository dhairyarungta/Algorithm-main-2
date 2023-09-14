from obstacle import Obstacle
from utils import Node
from constants import OBS_DIM, CAR_DIM

class CollisionDetector :
    def __init__(self,obstacle_list = None):
        self.obstacle_list = obstacle_list
    
    def _checkCollision(self,state:Node, obstacle:Obstacle, padding = 0):
        # bottom right and top left co-ordinates

        l1 = (state.x-(CAR_DIM+padding)//2,state.y+(CAR_DIM+padding)//2)
        l2 = (obstacle.pos_x-OBS_DIM//2,obstacle.pos_y+OBS_DIM//2)

        r1 = (state.x+CAR_DIM+padding//2,state.y-(CAR_DIM+padding)//2)
        r2 = (obstacle.pos_x+OBS_DIM//2,obstacle.pos_y-OBS_DIM//2)


        if(l1[0]>r2[0] or l2[0]>r1[0]):
            return False
        if(r1[1]>l2[1] or r2[1]>l1[1]):
            return False
        
        return True


def _checkBBCollision(self, cx, cy, side_x, side_y, obstacle:Obstacle):
    # bottom right and top left co-ordinates
    l1 = (cx-side_x//2,cy+side_y//2)
    l2 = (obstacle.pos_x-OBS_DIM//2,obstacle.pos_y+OBS_DIM//2) 

    r1 = (cx+side_x//2, cy-side_y//2)
    r2 = (obstacle.pos_x+OBS_DIM//2, obstacle.pos_y-OBS_DIM//2)
    if(l1[0]>r2[0] or l2[0]>r1[0]):
        return False
    if (r1[1]>l2[1] or r2[1]>l1[1]):
        return False
    return True

def checkStateIsValid(self,node:Node,padding = 0):
    # check robot is not outside the arena
    cx , cy, ctheta = node.x, node.y, node.theta

    if(CAR_DIM+padding)//2<=cx<=200 - (CAR_DIM+padding)//2 and  (CAR_DIM+padding)//2<=cy<=200-(CAR_DIM+padding)//2 and ctheta % 90 == 0:
        for obs in self.obstacle_list:
            #check obstacle collision
            if self._checkCollision(node,obs,padding):
                return False    
            
        return True
    return False



def checkBBisValid(self, cx, cy, side_x, side_y):
    if side_x//2<=cx<=200-side_x//2 and side_y//2<=cy<=200-side_y//2:
        for obs in self.obstacle_list:
            #check obstacle collision
            if self._checkBBCollision(cx,cy,side_x,side_y,obs):
                return False
        
        return True

    return False

    