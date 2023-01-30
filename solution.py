import numpy 
import pyrosim.pyrosim as pyrosim
import random 
import os 
import time

length = 1
width = 1
height = 1

x = 0
y = 0
z = 0.5

class SOLUTION():
    def __init__(self, nextAvailableID) -> None:
        self.myID = nextAvailableID
        self.weights = numpy.random.rand(3,2)
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
            # print(self.fitness)
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
        pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5] , size=[length ,height ,width ])
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , 
            type = "revolute", position = [1,0,1])
        pyrosim.Send_Cube(name="BackLeg", pos=[-.5,0,-.5] , size=[length ,height ,width ])
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , 
        type = "revolute", position = [2,0,1])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-.5] , size=[length ,height ,width ])
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain{}.nndf".format(self.myID))
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        sensors = [0,1,2]
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 4, jointName = "Torso_FrontLeg")
        motors = [3,4]
        for currentRow in range(3): 
         for currentColumn in range(2): 
             pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn + 3, weight = self.weights[currentRow][currentColumn] )
        
        pyrosim.End()

    def Mutate(self):
        row = random.randint(0,2)
        column = random.randint(0,1)
        self.weights[row][column] =  random.random() * 2 - 1

    
    def Set_ID(self, ID):
        self.myID = ID