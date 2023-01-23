
import pyrosim.pyrosim as pyrosim
import numpy as np

class SENSOR:
    def __init__(self, ln) -> None:
        self.ln = ln
        self.values = np.zeros(1000)
    
    def Get_Value(self,t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.ln)

    def Save_Values(self):
        np.save('data/{self.ln}_sensor.npy', self.values)