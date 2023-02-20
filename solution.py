import numpy 
import random 
import os 
import time

import pyrosim.pyrosim as pyrosim

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
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()

    def Start_Simulation(self,directorgui, dont_delete = False):
        os.system("python3 simulate.py " + directorgui + " " + str(self.myID) + " 2&>1 &") 

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness{}.txt".format(self.myID)):
            time.sleep(0.01)
        with open("fitness{}.txt".format(self.myID),'r') as f:
            self.fitness = float(f.read()) 
        os.system("rm fitness{}.txt".format(self.myID))

    def Evaluate(self, directorgui):
        self.Start_Simulation(directorgui)

    def Create_World(self):
       pyrosim.Start_SDF("boxes.sdf")
       pyrosim.Send_Cube(name="Box", pos=[-10,10,1.5] , size=[length ,height ,width ])
       pyrosim.Send_Cube(name="Box1", pos=[-10,10,.5] , size=[length ,height ,width ])
       pyrosim.Send_Cube(name="Box2", pos=[-9,10,.5] , size=[length ,height ,width ])
       pyrosim.Send_Cube(name="Box3", pos=[-9,9,.5] , size=[length ,height ,width ])
       pyrosim.Send_Cube(name="Box4", pos=[-9,11,.5] , size=[length ,height ,width ])
       pyrosim.Send_Cube(name="Box5", pos=[-10,11,.5] , size=[length ,height ,width ])
       pyrosim.Send_Cube(name="Box6", pos=[-10,9,.5] , size=[length ,height ,width ])
       pyrosim.Send_Cube(name="Box7", pos=[-11,11,.5] , size=[length ,height ,width ])
       pyrosim.Send_Cube(name="Box8", pos=[-11,10,.5] , size=[length ,height ,width ])
       pyrosim.Send_Cube(name="Box9", pos=[-11,9,.5] , size=[length ,height ,width ])

       pyrosim.End()

# size = depth, width, height 
    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0,0,3.5] , size=[0.5 ,2 ,2 ])

        pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , 
            type = "revolute", position = [0,-1,2.5], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[0,0,-.5] , size=[.5,.3,1])

        pyrosim.Send_Joint( name = "LeftLeg_LeftLegLower" , parent= "LeftLeg" , child = "LeftLegLower" , 
            type = "revolute", position = [0,0,-1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLegLower", pos=[0,0,-.5] , size=[.5,.3,1])

        pyrosim.Send_Joint( name = "LeftLegLower_LeftFoot" , parent= "LeftLegLower" , child = "LeftFoot" , 
            type = "revolute", position = [0,0,-1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftFoot", pos=[0,0,-.25] , size=[.5,.6,.5])




        pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , 
            type = "revolute", position = [0,1,2.5], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[0,0,-.5] , size=[.5,.3,1])

        pyrosim.Send_Joint( name = "RightLeg_RightLegLower" , parent= "RightLeg" , child = "RightLegLower" , 
            type = "revolute", position = [0,0,-1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLegLower", pos=[0,0,-.5] , size=[.5,.3,1])

        pyrosim.Send_Joint( name = "RightLegLower_RightFoot" , parent= "RightLegLower" , child = "RightFoot" , 
            type = "revolute", position = [0,0,-1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightFoot", pos=[0,0,-.25] , size=[.5,.6,.5])



        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain{}.nndf".format(self.myID))
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "LeftLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "LeftLegLower")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LeftFoot")
        pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "RightLeg")
        pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "RightLegLower")
        pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "RightFoot")

        # pyrosim.Send_Motor_Neuron( name = 7 , jointName = "Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron( name = 7 , jointName = "LeftLeg_LeftLegLower")
        # pyrosim.Send_Motor_Neuron( name = 9 , jointName = "Torso_RightLeg")
        pyrosim.Send_Motor_Neuron( name = 8 , jointName = "RightLeg_RightLegLower")


        for currentRow in range(c.numSensorNeurons): 
         for currentColumn in range(c.numMotorNeurons): 
             pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn + c.numSensorNeurons, weight = self.weights[currentRow][currentColumn] )
        
        pyrosim.End()

    def Mutate(self):
        row = random.randint(0,2)
        column = random.randint(0,1)
        self.weights[row][column] =  random.random() * 2 - 1

    
    def Set_ID(self, ID):
        self.myID = ID
