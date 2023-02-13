import numpy 
import pyrosim.pyrosim as pyrosim
import random 
import os 
import time

import constants as c 
length = 1
width = 1
height = 1

x = 0
y = 0
z = 0.5

class SOLUTION():
    def __init__(self, nextAvailableID) -> None:
        self.myID = nextAvailableID
        self.weights = numpy.random.rand(c.numSensorNeurons,c.numMotorNeurons)
        self.weights = self.weights * 2 - 1
        self.fitness = 0
        self.joints = []
        self.links = []
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()

    def Start_Simulation(self,directorgui):
        os.system("python3 simulate.py " + directorgui + " " + str(self.myID) + " 2&>1 &") 

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness{}.txt".format(self.myID)):
            time.sleep(0.01)
        with open("fitness{}.txt".format(self.myID),'r') as f:
            self.fitness = float(f.read()) 
        os.system("rm fitness{}.txt".format(self.myID))

    def Evaluate(self, directorgui):
        self.Start_Simulation(directorgui)
        self.Wait_For_Simulation_To_End()

    def Create_World(self):
       pyrosim.Start_SDF("boxes.sdf")
    #    pyrosim.Send_Cube(name="Box", pos=[5,5,5] , size=[length ,height ,width ])
       pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")

      

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain{}.nndf".format(self.myID))
       
        pyrosim.End()

    def Mutate(self):
        row = random.randint(0,2)
        column = random.randint(0,1)
        self.weights[row][column] =  random.random() * 2 - 1

    
    def Set_ID(self, ID):
        self.myID = ID
