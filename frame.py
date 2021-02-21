class Frame:
    c = 3e8
    
    def __init__(self,velocity:float = 0):
        if velocity > self.c or velocity < -self.c :
            raise ValueError("Velocity for frame {} exceeds speed limit".format(velocity))
        self._velocity = velocity
        
    def relative_velocity(self,other):
        u = self._velocity
        v = other._velocity
        return (u-v)/(1- (u*v)/(self.c*self.c)) # because assumed positive velocity for all and difference needed