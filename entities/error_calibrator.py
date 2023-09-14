from copy import deepcopy
from typing import final
from utils import Node
from collision import CollisionDetector
import math

class Error_Calibrator:

    def __init__(self, collision_detector:CollisionDetector):
        self.calibration_count = 0
        self.collision_detector = collision_detector
        self.error_delta_init = 3
        self.progress = 1
        self.error_delta_constant = 10
    
    def _calcError(self):

        error_move = self.error_delta_init + (self.progress*self.calibration_count)
        return min(error_move, self.error_delta_constant)
    
    def _correctForward (self, state: Node, step: float):
        state.x = state.x + int(step*math.cos(math.radians(state.theta)))
        state.y = state.y + int(step*math.sin(math.radians(state.theta)))
        return state

    def _correctBackward (self, state: Node, step: float):
        state.x = state.x - int(step*math.cos(math.radians(state.theta)))
        state.y = state.y - int(step*math.sin(math.radians(state.theta)))
        return state

    def getCorrection(self, final_state: Node):
        forward_step, backward_step = self.error_delta_constant, self.error_delta_constant
        forward_correction = deepcopy(final_state)
        self._correctForward(forward_correction, forward_step)

        if not self.collision_detector.checkStateIsValid(node=forward_correction, padding=0):
            forward_step = self._calcError()
        
        backward_correction = deepcopy(final_state)
        self._correctBackward(backward_correction, backward_step)

        if not self.collision_detector.checkStateIsValid(node=backward_correction, padding=0):
            
            backward_step = self._calcError()
            
        
        self.calibration_count += 1

        return forward_step, backward_step

    
if __name__ == "__main__":
    obstacles = []
    collision_detector = CollisionDetector(obstacles)
    error_calibrator = Error_Calibrator(collision_detector = collision_detector)

    print(error_calibrator.getCorrection(Node("ROB", 185,185, 0)))
    print(error_calibrator.getCorrection(Node("ROB", 185,15, 90)))
    print(error_calibrator.getCorrection(Node("ROB", 15,185, 0)))
    print(error_calibrator.getCorrection(Node("ROB", 15,185, 90)))

    
