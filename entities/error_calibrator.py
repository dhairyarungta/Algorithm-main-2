from copy import deepcopy
from typing import final
from utils import Node
from collision import CollisionDetector
import math

class Error_Calibrator:
    def __init__(self,collision_detector:CollisionDetector)
        self.calibration_count = 0
        self.collision_detector = collision_detector
        self.error_delta_init = 3   
        self.progress = 1
        self.error_delta_constant = 10

    def _calcError(self):
        
