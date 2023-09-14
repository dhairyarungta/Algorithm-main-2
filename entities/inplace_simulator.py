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
    
    