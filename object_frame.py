from frame import Frame

class Object_Frame:
    
    c = 3e8
    
    def __init__(self,velocity:float=0,frame:Frame = Frame()):
        self._velocity = velocity # with respect to frame
        self._frame = frame # frame of object
        
    def rest_velocity(self) -> float:
        u = self._velocity
        v = self._frame._velocity
        return (u+v)/(1+ (u*v)/(self.c*self.c))
    
    @property
    def velocity(self):
        return self._velocity
    
    @velocity.setter
    def velocity_update(self,new_vel:float = 0):
        self._velocity = new_vel