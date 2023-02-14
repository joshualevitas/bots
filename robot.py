import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import math

from sensor import SENSOR
from motor import MOTOR

import constants as c 

import os 

class ROBOT:
    def __init__(self,solutionID) -> None:
        self.solutionID = solutionID
        self.sensors = {}
        self.motors = {}
        self.robotId = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK("brain{}.nndf".format(solutionID))
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_to_Act()
        os.system("rm brain{}.nndf".format(solutionID))
        

    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
    
    def Sense(self,t):
        for sensor in self.sensors:
            self.sensors[sensor].Get_Value(t)

    def Prepare_to_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self,t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                self.motors[jointName].Set_Value(self.robotId,desiredAngle)


    def Think(self):
        self.nn.Update()
        # self.nn.Print()

    def Get_Fitness(self):
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
        basePosition = basePositionAndOrientation[0]
        xCoordinateOfLinkZero = basePosition[0]
        y = basePosition[2]
        z = basePosition[1]

        dist_squared = ((xCoordinateOfLinkZero - (-10))**2 + (z - 10)**2 + (y - 2)**2)
        dist = math.sqrt(dist_squared)
        with open("tmp{}.txt".format(self.solutionID), 'w') as f:
            f.write(str(dist))
        os.system("mv tmp{}.txt fitness{}.txt".format(self.solutionID,self.solutionID))