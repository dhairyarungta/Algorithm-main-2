from utils import Node
from constants import TR
from collision import CollisionDetector 

bb = TR["Inplace turn"] 
class Inplace_Simulator:
    def __init__(self,collison_detector:CollisionDetector):
        self.height = bb["height"]
        self.width = bb["width"]
        self.st = bb["st"]
        self.side =  bb["side"]
        self.collision_detector =  collison_detector
    
    def returnMeta(self, currentNode:Node, turn = "right"):
        x, y, theta = currentNode.x, currentNode.y, currentNode.theta

        bbcenter = {
            90:{
                "left": lambda x,y: (x+self.side-(self.width//2),y-self.st+(self.height//2)),
                "right": lambda x,y: (x-self.side+(self.width//2),y-self.st+(self.height//2))
            },
            270:{
                "left": lambda x,y: (x-self.side+(self.width//2),y+self.st-(self.height//2)),
                "right": lambda x,y: (x+self.side-(self.width//2),y+self.st-(self.height//2))
            },
            0:{
                "left": lambda x,y: (x-self.st+(self.height//2),y-self.side+(self.width//2)),
                "right": lambda x,y: (x-self.st+(self.height//2),y+self.side-(self.width//2))
            },
            180:{
                "left": lambda x,y: (x+self.st-(self.height//2),y+self.side-(self.width//2)),
                "right": lambda x,y: (x+self.st-(self.height//2),y-self.side+(self.width//2))
            }
        }

        sides = {
            0: (self.height, self.width),
            180: (self.height, self.width),
            90: (self.width, self.height),
            270: (self.width, self.height)
        }

        next_theta = {
            0: {
                "left": 90,
                "right": 270
            },
            180:{
                "left": 270,
                "right": 90
            },
            90: {
                "left": 180,
                "right": 0
            },

            270:{
                "left": 180,
                "right": 0
            }


        }

        return bbcenter[theta][turn](x,y),sides[theta], next_theta[theta][turn]

    def checkTurn(self, currentNode:Node, turn_where="right"):

        bbcentre,sides, next_theta = self.returnMeta(currentNode, turn_where)
        cx,cy =bbcentre
        side_x, side_y = sides

        if self.collision_detector.checkBBisValid(cx,cy,side_x, side_y):
            return True, Node("STATE", currentNode.x, currentNode.y, next_theta)
        
        return False, None

       

