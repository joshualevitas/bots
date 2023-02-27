import random 

import pyrosim.pyrosim as pyrosim


length = 1
width = 1
height = 1

x = 0
y = 0
z = 0.5

def create_world():
    pyrosim.Start_SDF("boxes.sdf")

    pyrosim.Send_Cube(name="Box", pos=[5,5,5] , size=[length ,height ,width ])

    pyrosim.End()

def create_robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5] , size=[length ,height ,width ])
    pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , 
        type = "revolute", position = [1,0,1])
    pyrosim.Send_Cube(name="BackLeg", pos=[-.5,0,-.5] , size=[length ,height ,width ])
    pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , 
    type = "revolute", position = [2,0,1])
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-.5] , size=[length ,height ,width ])
    pyrosim.End()


def Generate_Body():
   pyrosim.Start_URDF("body.urdf")
   pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5] , size=[length ,height ,width ])
   pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , 
       type = "revolute", position = [1,0,1])
   pyrosim.Send_Cube(name="BackLeg", pos=[-.5,0,-.5] , size=[length ,height ,width ])
   pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , 
   type = "revolute", position = [2,0,1])
   pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-.5] , size=[length ,height ,width ])
   pyrosim.End()


def Generate_Brain():
   pyrosim.Start_NeuralNetwork("brain.nndf")

   pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
   pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
   pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
   sensors = [0,1,2]

   pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
   pyrosim.Send_Motor_Neuron( name = 4, jointName = "Torso_FrontLeg")
   motors = [3,4]

   for sensor in sensors: 
    for motor in motors: 
        pyrosim.Send_Synapse( sourceNeuronName = sensor , targetNeuronName = motor, weight = random.uniform(-1,1) )
   
   pyrosim.End()


create_world()
Generate_Body()
Generate_Brain()


