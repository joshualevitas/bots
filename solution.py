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
        self.id = 0
        self.fitness = 0
        self.joints = []
        self.links = []
        self.sensorNeuronCount = 0
        self.motorNeuronCount = 0
        
        self.Create_World()
        self.Create_Body()

        self.weights = numpy.random.rand(self.sensorNeuronCount, self.motorNeuronCount)
        self.weights = self.weights * 2 - 1

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
        # self.Wait_For_Simulation_To_End()

    def Create_World(self):
       pyrosim.Start_SDF("boxes.sdf")
    #    pyrosim.Send_Cube(name="Box", pos=[5,5,5] , size=[length ,height ,width ])
       pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        dimensions = [random.random() + 0.05 for i in range(3)]
        snake_length = random.randint(2, 10)
        self.motorNeuronCount = snake_length 
        jp = dimensions[1]
        has_sensor = random.randint(0, 1)
        p = "Head"
        if has_sensor:
            pyrosim.Send_Cube(name="Head", pos=[0,0,.5], size=dimensions, color="green", rgba = ["0","1.0","0","1.0"])
        else:
            pyrosim.Send_Cube(name="Head", pos=[0,0,.5], size=dimensions, color="blue")
        
        tmp = .5
        for i in range(snake_length):
            has_sensor = random.randint(0, 1)
            dimensions = [random.random() + 0.05 for i in range(3)]
            cube = "b{}".format(i)
            joint="j_{}".format(i)

            #do stuff
            pyrosim.Send_Joint(name=joint, parent=p, child=cube, type="revolute", jointAxis="1 0 0", position=[0, .5*jp, tmp])
            
            if has_sensor:
                pyrosim.Send_Cube(name=cube, pos=[0,.5*dimensions[1],0], size=dimensions, color="green", rgba = ["0","1.0","0","1.0"])
            else:
                pyrosim.Send_Cube(name=cube, pos=[0,.5*dimensions[1],0], size=dimensions, color="blue")

            tmp = 0
            p = cube

            if has_sensor:
                self.links.append(cube)
                self.sensorNeuronCount +=1

            self.joints.append(joint)



            

        pyrosim.End()
    


    def Create_Brain(self):
        #do different stuff
        pyrosim.Start_NeuralNetwork("brain{}.nndf".format(self.myID))
        for link in self.links: 
            pyrosim.Send_Sensor_Neuron(name = self.id , linkName = link)
            self.id +=1 
            # print("attempted to add link")

        for joint in self.joints:
            pyrosim.Send_Motor_Neuron( name = self.id , jointName = joint)
            self.id+=1
            # print("attempted to add motor")


        for currentRow in range(self.sensorNeuronCount): 
         for currentColumn in range(self.motorNeuronCount): 
             pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn + self.sensorNeuronCount, weight = self.weights[currentRow][currentColumn] )
        
        pyrosim.End()

    def Mutate(self):
        row = random.randint(0,2)
        column = random.randint(0,1)
        self.weights[row][column] =  random.random() * 2 - 1

    
    def Set_ID(self, ID):
        self.myID = ID



