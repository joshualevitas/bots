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
        pass
        # os.system("python3 simulate.py " + directorgui + " " + str(self.myID) + " &")
        # while not os.path.exists("fitness{}.txt".format(self.myID)):
            # time.sleep(0.01)
        # with open("fitness{}.txt".format(self.myID),'r') as f:
            # self.fitness = float(f.read())

    def Create_World(self):
       pyrosim.Start_SDF("boxes.sdf")
       pyrosim.Send_Cube(name="Box", pos=[5,5,5] , size=[length ,height ,width ])
       pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[length ,height ,width ])

        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , 
            type = "revolute", position = [0,0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[-.33,0.5,0] , size=[0.2,1,0.2])

        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , 
            type = "revolute", position = [0,-.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[-.33,-0.5,0] , size=[0.2,1,0.2])

        pyrosim.Send_Joint( name = "Torso_FrontLeg2" , parent= "Torso" , child = "FrontLeg2" , 
            type = "revolute", position = [0,0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg2", pos=[.33,0.5,0] , size=[0.2,1,0.2])

        pyrosim.Send_Joint( name = "Torso_BackLeg2" , parent= "Torso" , child = "BackLeg2" , 
            type = "revolute", position = [0,-.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeg2", pos=[.33,-0.5,0] , size=[0.2,1,0.2])

        pyrosim.Send_Joint( name = "Torso_FrontLeg3" , parent= "Torso" , child = "FrontLeg3" , 
            type = "revolute", position = [0,0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg3", pos=[0,0.5,0] , size=[0.2,1,0.2])

        pyrosim.Send_Joint( name = "Torso_BackLeg3" , parent= "Torso" , child = "BackLeg3" , 
            type = "revolute", position = [0,-.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeg3", pos=[0,-0.5,0] , size=[0.2,1,0.2])
        
        # pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , 
        #     type = "revolute", position = [0.5,0,1], jointAxis = "0 1 0")
        # pyrosim.Send_Cube(name ="LeftLeg", pos = [0.5,0,0],size=[1,0.2,0.2])

        pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , 
            type = "revolute", position = [-0.5,0,1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name ="RightLeg", pos = [-0.5,0,0],size=[1,0.2,0.2])
        

        pyrosim.Send_Joint( name = "FrontLeg_FrontLegBottom" , parent= "FrontLeg" , child = "FrontLegBottom" , 
            type = "revolute", position = [0,1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name ="FrontLegBottom", pos = [-.33,0,-.5],size=[0.2,0.2,1])

        pyrosim.Send_Joint( name = "BackLeg_BackLegBottom" , parent= "BackLeg" , child = "BackLegBottom" , 
           type = "revolute", position = [0,-1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name ="BackLegBottom", pos = [-.33,0,-.5],size=[0.2,0.2,1])

        pyrosim.Send_Joint( name = "FrontLeg_FrontLegBottom2" , parent= "FrontLeg2" , child = "FrontLegBottom2" , 
            type = "revolute", position = [0,1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name ="FrontLegBottom2", pos = [.33,0,-.5],size=[0.2,0.2,1])

        pyrosim.Send_Joint( name = "BackLeg_BackLegBottom2" , parent= "BackLeg2" , child = "BackLegBottom2" , 
           type = "revolute", position = [0,-1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name ="BackLegBottom2", pos = [.33,0,-.5],size=[0.2,0.2,1])

        pyrosim.Send_Joint( name = "FrontLeg_FrontLegBottom3" , parent= "FrontLeg3" , child = "FrontLegBottom3" , 
            type = "revolute", position = [0,1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name ="FrontLegBottom3", pos = [0,0,-.5],size=[0.1,0.1,1])

        pyrosim.Send_Joint( name = "BackLeg_BackLegBottom3" , parent= "BackLeg3" , child = "BackLegBottom3" , 
           type = "revolute", position = [0,-1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name ="BackLegBottom3", pos = [0,0,-.5],size=[0.1,0.1,1])
        
        # pyrosim.Send_Joint( name = "LeftLeg_LeftLegBottom" , parent= "LeftLeg" , child = "LeftLegBottom" , 
        #     type = "revolute", position = [1,0,0], jointAxis = "0 1 0")
        # pyrosim.Send_Cube(name ="LeftLegBottom", pos = [0,0,-.5],size=[0.2,0.2,1])

        pyrosim.Send_Joint( name = "RightLeg_RightLegBottom" , parent= "RightLeg" , child = "RightLegBottom" , 
           type = "revolute", position = [-1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name ="RightLegBottom", pos = [0,0,-.5],size=[0.2,0.2,1])

        # pyrosim.Send_Joint( name = "RightLeg_RightLegBlock" , parent= "RightLeg" , child = "RightLegBlock" , 
        #    type = "revolute", position = [-1,0,0], jointAxis = "0 1 0")
        # pyrosim.Send_Cube(name="RightLegBlock", pos=[0,0,-.5] , size=[.1,.66,.66])
    

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain{}.nndf".format(self.myID))
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "RightLeg")
        pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "FrontLegBottom")
        pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "BackLegBottom")
        pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "RightLegBottom")
        # pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "RightLegBottom")
        
        pyrosim.Send_Sensor_Neuron(name = 13 , linkName = "BackLeg2")
        pyrosim.Send_Sensor_Neuron(name = 14 , linkName = "FrontLeg2")
        pyrosim.Send_Sensor_Neuron(name = 15 , linkName = "BackLegBottom2")
        pyrosim.Send_Sensor_Neuron(name = 16 , linkName = "FrontLegBottom2")

        pyrosim.Send_Sensor_Neuron(name = 21 , linkName = "FrontLegBottom3")
        pyrosim.Send_Sensor_Neuron(name = 22 , linkName = "BackLegBottom3")
        pyrosim.Send_Sensor_Neuron(name = 23 , linkName = "BackLeg3")
        pyrosim.Send_Sensor_Neuron(name = 24 , linkName = "FrontLeg3")

        pyrosim.Send_Motor_Neuron( name = 7 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 8, jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 9, jointName = "Torso_RightLeg" )
        pyrosim.Send_Motor_Neuron( name = 10, jointName = "FrontLeg_FrontLegBottom")
        pyrosim.Send_Motor_Neuron( name = 11, jointName = "BackLeg_BackLegBottom")
        pyrosim.Send_Motor_Neuron( name = 12, jointName = "RightLeg_RightLegBottom")
        # pyrosim.Send_Motor_Neuron( name = 13, jointName = "RightLeg_RightLegBottom")

        pyrosim.Send_Motor_Neuron( name = 17 , jointName = "Torso_BackLeg2")
        pyrosim.Send_Motor_Neuron( name = 18, jointName = "Torso_FrontLeg2")
        pyrosim.Send_Motor_Neuron( name = 19, jointName = "FrontLeg_FrontLegBottom2")
        pyrosim.Send_Motor_Neuron( name = 20, jointName = "BackLeg_BackLegBottom2")

        pyrosim.Send_Motor_Neuron( name = 25 , jointName = "Torso_BackLeg3")
        pyrosim.Send_Motor_Neuron( name = 26, jointName = "Torso_FrontLeg3")
        pyrosim.Send_Motor_Neuron( name = 27, jointName = "FrontLeg_FrontLegBottom3")
        pyrosim.Send_Motor_Neuron( name = 28, jointName = "BackLeg_BackLegBottom3")


        


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
