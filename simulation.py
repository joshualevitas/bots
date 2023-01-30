
import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy as np
import random
import constants as c
from robot import ROBOT
from world import WORLD



class SIMULATION:

    def __init__(self, directOrGui):
        if directOrGui == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)
            
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.robot = ROBOT()
        self.world = WORLD()


    def __del__(self):
        p.disconnect()

    def Run(self):
         for i in range(c.epoch_length):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            time.sleep(1/60)

    def get_fitness(self):
        return self.robot.get_fitness()

    


