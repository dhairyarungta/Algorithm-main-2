class Node:
    
    def __init__(self,key, x, y, theta, parent = None, h = None):
        self.key = key
        self.x = x
        self.y = y
        self.theta = theta
        self.parent = parent
        self.h = h

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.x == other.x and self.y == other.y and self.theta == other.theta
        return False
    
    def __lt__(self, other):
        return self.h < other.h

class Edge :
    def __init__(self, src:Node, dest:Node, weight: float):
        self.src = src
        self.dest = dest
        self.weight = weight