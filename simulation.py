import random 
import numpy
import time 

import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
        
import constants as c 
from world import WORLD
from robot import ROBOT




class SIMULATION:
    def __init__(self,directOrGUI,solutionID) -> None:
        self.physicsClient = None 
        self.directOrGUI = directOrGUI
        self.solutionID = solutionID
        if directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)
            p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
            p.resetDebugVisualizerCamera(cameraDistance = 6, cameraYaw=30, cameraPitch=-40, cameraTargetPosition=[0,0,0])

        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)

        self.world = WORLD()
        print("World set up")
        self.robot = ROBOT(solutionID)
        print("Simulation set up succesfully")

    def Run(self):
         for i in range(c.num_steps):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            if self.directOrGUI == "GUI":
                time.sleep(c.sleep_time)

    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):
        p.disconnect()