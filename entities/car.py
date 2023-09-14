from constants import CAR_DIM

class Car:
    def __init__(self,pos_x = 0, pos_y = 0, pos_theta = 90):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_theta = pos_theta
        self.dimension = CAR_DIM # in cm