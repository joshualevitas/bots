import numpy 
import random 
import os 
import time

import pyrosim.pyrosim as pyrosim
from simulate import simulate

import constants as c 
length = 1
width = 1
height = 1

x = 0
y = 0
z = 0.5

class RANDOM_SOLUTION():
    def __init__(self, nextAvailableID) -> None:
        self.myID = nextAvailableID
        self.fitness = 0
        self.Create_World()
        self.idNum = 0 
        self.links = []
        self.joints = []
        self.numSensorsNeurons = 0 
        self.numMotorNeurons = 0
        self.Create_Body()
        self.weights = numpy.random.rand(self.numSensorsNeurons,self.numMotorNeurons)
        self.weights = self.weights * 2 - 1
        self.Create_Brain()
       
       

    def Start_Simulation(self,directorgui, dont_delete = False):
        print("Running simulate")
        # os.system("python3 simulate.py " + directorgui + " " + str(self.myID) + " 2&>1 &")
        print(self.myID)
        simulate(directorgui,str(self.myID))
        print("Command executed") 

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
       pyrosim.End()


    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        has_sensor = random.randint(0,1)
        depth = random.random() + 0.01
        width = random.random() + 0.01 
        height = random.random() + 0.01 
        prevs = [depth, width, height]
      
        
        
        if has_sensor:
            self.links.append("Torso")
            pyrosim.Send_Cube(name="Torso", pos=[0,0,0.5] , size=[depth ,width ,height ], color="green",rgba = ["0","1.0","0","1,0"])
        else:
            pyrosim.Send_Cube(name="Torso", pos=[0,0,0.5] , size=[depth ,width ,height ])
        
        random_num_blocks = random.randint(1,10)
        parent = "Torso"
        joint_num = 0
        self.numMotorNeurons = random_num_blocks

        for i in range (random_num_blocks):
            has_sensor = random.randint(0,1)
            path = random.randint(0, 2)
            
            pos = [i/2 if i == path else 0 for i in prevs]
            pos[2] += .5            
    
            depth = random.random() + 0.01 
            width = random.random() + 0.01 
            height = random.random() + 0.01 
            
            block_name = "Block" + str(joint_num)
            joint_name = parent + "_" + block_name

            if i == 0:
                pyrosim.Send_Joint(name = joint_name   , parent= parent , child = block_name , type = type, position = pos, jointAxis= '1 0 0')
                pos[2] -= .5
                if has_sensor:
                    pyrosim.Send_Cube(name = block_name, pos= pos,size = [depth,width,height],color="green",rgba = ["0","1.0","0","1,0"])
                else:
                    pyrosim.Send_Cube(name = block_name, pos= pos,size = [depth,width,height])
           

            else:
                if path == 0:
                    if prev_path == 0:
                        pyrosim.Send_Joint(name = joint_name , parent= parent , child = block_name , 
                        type = type, position = [0,pos[1]/2,0], jointAxis= '1 0 0')
                    elif prev_path == 1:   
                        pyrosim.Send_Joint(name = joint_name , parent= parent , child = block_name , 
                        type = type, position = [pos[0]/2, pos[0]/2,0], jointAxis= '1 0 0')
                    else:
                        pyrosim.Send_Joint(name = joint_name , parent= parent , child = block_name , 
                        type = type, position = [0,pos[1]/2,pos[2]/2], jointAxis= '1 0 0')
       
                    if has_sensor:
                        pyrosim.Send_Cube(name = block_name, pos= [0,width/2,0],size = [depth,width,height],color="green",rgba = ["0","1.0","0","1,0"])
                    else:
                        pyrosim.Send_Cube(name = block_name, pos= [0,width/2,0],size = [depth,width,height])
                
                elif path == 1:
                    if prev_path == 0:
                        pyrosim.Send_Joint(name = joint_name , parent= parent , child = block_name , 
                        type = type, position = [pos[0]/2,pos[1]/2,0], jointAxis= '1 0 0')
                    elif prev_path == 1:   
                        pyrosim.Send_Joint(name = joint_name , parent= parent , child = block_name , 
                        type = type, position = [pos[0]/2,0,pos[2]/2], jointAxis= '1 0 0')
                    else:
                        pyrosim.Send_Joint(name = joint_name , parent= parent , child = block_name , 
                        type = type, position = [0,pos[1]/2,pos[2]/2], jointAxis= '1 0 0')
       
                    if has_sensor:
                        pyrosim.Send_Cube(name = block_name, pos= [depth/2,0,0],size = [depth,width,height],color="green",rgba = ["0","1.0","0","1,0"])
                    else:
                        pyrosim.Send_Cube(name = block_name, pos= [depth/2,0,0],size = [depth,width,height])

                
                else:
                    if prev_path == 0:
                        pyrosim.Send_Joint(name = joint_name , parent= parent , child = block_name , 
                        type = type, position = [0,pos[1]/2,pos[2]/2], jointAxis= '1 0 0')
                    elif prev_path == 1:   
                        pyrosim.Send_Joint(name = joint_name , parent= parent , child = block_name , 
                        type = type, position = [pos[0]/2, 0, pos[2]/2], jointAxis= '1 0 0')
                    else:
                        pyrosim.Send_Joint(name = joint_name , parent= parent , child = block_name , 
                        type = type, position = [0,0,pos[2]/2], jointAxis= '1 0 0')
       
                    if has_sensor:
                        pyrosim.Send_Cube(name = block_name, pos= [0,0, height/2],size = [depth,width,height],color="green",rgba = ["0","1.0","0","1,0"])
                    else:
                        pyrosim.Send_Cube(name = block_name, pos= [0,0,height/2],size = [depth,width,height])
                


            parent = block_name
            prev_path = path
            prevs = [depth, width, height]
            joint_num +=1
            if has_sensor:
                self.links.append(block_name)
                self.numSensorsNeurons +=1
            self.joints.append(joint_name)

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain{}.nndf".format(self.myID))
        for link in self.links: 
            pyrosim.Send_Sensor_Neuron(name = self.idNum , linkName = link)
            self.idNum +=1 
        
        for joint in self.joints:
            pyrosim.Send_Motor_Neuron( name = self.idNum , jointName = joint)
            self.idNum +=1
        

        for currentRow in range(self.numSensorsNeurons): 
         for currentColumn in range(self.numMotorNeurons): 
             pyrosim.Send_Synapse(sourceNeuronName = currentRow , targetNeuronName = currentColumn + self.numSensorsNeurons, weight = self.weights[currentRow][currentColumn])
        
        pyrosim.End()

    def Mutate(self):
        row = random.randint(0,2)
        column = random.randint(0,1)
        self.weights[row][column] =  random.random() * 2 - 1

    
    def Set_ID(self, ID):
        self.myID = ID
