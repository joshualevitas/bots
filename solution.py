import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random
import time

class SOLUTION:
    def __init__(self, id):
        self.weights = np.random.rand(3,2)
        self.weights = self.weights * 2 - 1
        self.myId = id
    
    def set_id(self, id):
        self.myId = id

    def Start_Simulation(self, directOrGui):
        os.system("python3 simulate.py " + directOrGui + " " + str(self.myId) + " 2&>1 &")

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness{}.txt".format(self.myId)):
            time.sleep(0.01)
        with open("fitness{}.txt".format(self.myId),'r') as f:
            self.fitness = float(f.read()) 
            # print(self.fitness)
        os.system("rm fitness{}.txt".format(self.myId)) 
        
    def evaluate(self, directOrGui):
        self.create_world()
        self.create_body()
        self.create_brain()
        os.system("python3 simulate.py " + directOrGui + " " + str(self.myId) + " &")
        
        f = open("fitness" + str(self.myId) + ".txt", "r")
        self.fitness = float(f.read())
        print(self.fitness)
        f.close()

    def create_world(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[10,0,.5] , size=[1,1,1])
        pyrosim.End()

    def create_body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5] , size=[1,1,1])
        pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg", type = "revolute", position = [1,0,1])
        pyrosim.Send_Cube(name="BackLeg", pos=[-.5,0,-.5] , size=[1,1,1])
        pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg", type = "revolute", position = [2,0,1])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-.5] , size=[1,1,1])
        pyrosim.End()

    def create_brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myId) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        

        pyrosim.Send_Motor_Neuron(name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name = 4 , jointName = "Torso_FrontLeg")
        

        for r in [0,1,2]:
            for c in [0,1]:
                pyrosim.Send_Synapse(sourceNeuronName = r, targetNeuronName = c + 3, weight = self.weights[r][c])

        pyrosim.End()

    def mutate(self):
        r = random.randint(0, 2)
        c = random.randint(0, 1)
        self.weights[r,c] = random.random() * 2 - 1
        
