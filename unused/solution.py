# # I did something to my a6.py file and now it is not working. I am not sure what I did, but I was unable to fix it.
# # I was able to build my a7 on top of a friend's (austin p.) a6 instead. Much of the original files are similar except for 
# # the ones related to this assignment (i.e. solution)

import numpy 
import random 
import os 
import time
import copy
import pyrosim.pyrosim as pyrosim
from simulate import simulate

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
        self.fitness = 0
        self.Create_World()
        self.idNum = 0 
        self.links = []
        self.joints = []
        self.numSensorsNeurons = 0 
        self.numMotorNeurons = 0
        
        self.joints_ = []
        self.links_ = []
        self.parts = []


        self.Create_Body()
        self.weights = numpy.random.rand(self.numSensorsNeurons,self.numMotorNeurons)
        self.weights = self.weights * 2 - 1
        self.Create_Brain()
       
       

    def Start_Simulation(self, directorgui):
        print(self.myID)
        simulate(directorgui, str(self.myID), self.links, self.joints)

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
        random_sensor = random.randint(0,1)
        depth = random.random() + 0.01
        width = random.random() * 2 + 0.01 
        height = random.random() + 0.01 
        
        # prevs = [depth, width, height]
        prev_width = width
        prev_depth = depth 
        prev_height = height 

        prev_direction = 1

        if random_sensor:
            self.links.append("Torso")
            pyrosim.Send_Cube(name="Torso", pos=[0,0,0.5] , size=[depth, width, height], color="green",rgba = ["0","1.0","0","1,0"])
            self.parts.append([0, {'name': "Torso", 'pos':[0,0,0.5],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)],'color': "green", 'rgba': ["0","1.0","0","1,0"]}])

        else:
            pyrosim.Send_Cube(name="Torso", pos=[0,0,0.5] , size=[depth, width, height])
            self.parts.append([1,{'name': "Torso", 'pos':[0,0,0.5],'size': [copy.copy(depth) ,copy.copy(width) ,copy.copy(height)]}])

        
        random_num_blocks = random.randint(1,10)
        parent = "Torso"
        joint_num = 0
        self.numMotorNeurons = random_num_blocks 
        
        for i in range (random_num_blocks):
            random_sensor = random.randint(0,1)
         
            depth = random.random() + 0.01 
            width = random.random() * 2 + 0.01 
            height = random.random() + 0.01 


            block_name = "Block" + str(joint_num)
            joint_name = parent + "_" + block_name

            type = 'revolute'
        
            path = random.randint(1,3)

            random_axis = random.randint(1,20)
            axis = ''
            if random_axis == 1 or random_axis > 6:
                axis = '1 0 0'
            elif random_axis == 2:
                axis = '0 1 0'
            elif random_axis == 3:
                axis = '0 0 1'
            elif random_axis == 4: 
                axis = '1 1 0'
            elif random_axis == 5: 
                axis = '1 0 1'
            elif random_axis == 6:
                axis = '0 1 1'

            if path == 1:
                if i == 0:
                    pyrosim.Send_Joint(name = joint_name   , parent= parent , child = block_name , 
                        type = type, position = [0,prev_width/2,0.5], jointAxis= axis)
                    self.parts.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
                            'position':[0,copy.copy(prev_width)/2,0.5], 'jointAxis':axis}])
                    
                    if random_sensor:
                        pyrosim.Send_Cube(name = block_name, pos= [0,width/2,0],size = [depth,width,height],color="green",rgba = ["0","1.0","0","1,0"])
                        self.parts.append([0,{'name': block_name, 'pos':[0,copy.copy(width)/2,0],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)],'color': "green", 'rgba': ["0","1.0","0","1,0"]}])
                    else:
                        pyrosim.Send_Cube(name = block_name, pos= [0,width/2,0],size = [depth,width,height])
                        self.parts.append([1,{'name': block_name, 'pos':[0,copy.copy(width)/2,0],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)]}])
                else:
                    if prev_direction == 2:
                        pyrosim.Send_Joint(name = joint_name , parent= parent , child = block_name , 
                            type = type, position = [prev_depth/2,prev_width/2,0], jointAxis= axis)
                        self.parts.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
                                                    'position':[copy.copy(prev_depth)/2,copy.copy(prev_width)/2,0], 'jointAxis':axis}])
                    elif prev_direction == 3:
                        pyrosim.Send_Joint(name = joint_name , parent= parent , child = block_name , 
                        type = type, position = [0,prev_width/2,prev_height/2], jointAxis= axis)
                        self.parts.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
                                                    'position':[0,copy.copy(prev_width)/2,copy.copy(prev_height)/2], 'jointAxis':axis}])
                    else:
                        pyrosim.Send_Joint(name = joint_name , parent= parent , child = block_name , 
                        type = type, position = [0,prev_width/2,0], jointAxis= axis) 
                        self.parts.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
                                                 'position':[0,copy.copy(prev_width)/2,0], 'jointAxis':axis}])  
                    if random_sensor:
                        pyrosim.Send_Cube(name = block_name, pos= [0,width/2,0],size = [depth,width,height],color="green",rgba = ["0","1.0","0","1,0"])
                        self.parts.append([0,{'name': block_name, 'pos':[0,copy.copy(width)/2,0],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)],'color': "green", 'rgba': ["0","1.0","0","1,0"]}])
                    else:
                        pyrosim.Send_Cube(name = block_name, pos= [0,width/2,0],size = [depth,width,height])
                        self.parts.append([1,{'name': block_name, 'pos':[0,copy.copy(width)/2,0],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)]}])
            elif path == 2:
                if i == 0:
                    pyrosim.Send_Joint(name = joint_name   , parent= parent , child = block_name , 
                        type = type, position = [prev_depth/2,0,0.5], jointAxis= axis)
                    self.parts.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
                                                'position':[copy.copy(prev_depth)/2,0,0.5], 'jointAxis':axis}])
                    if random_sensor:
                        pyrosim.Send_Cube(name = block_name, pos= [depth/2,0,0],size = [depth,width,height],color="green",rgba = ["0","1.0","0","1,0"])
                        self.parts.append([0,{'name': block_name, 'pos':[copy.copy(depth)/2,0,0],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)],'color': "green", 'rgba': ["0","1.0","0","1,0"]}])
                    else:
                        pyrosim.Send_Cube(name = block_name, pos= [depth/2,0,0],size = [depth,width,height])
                        self.parts.append([1,{'name': block_name, 'pos':[copy.copy(depth)/2,0,0],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)]}])
                else:
                    if prev_direction == 1:
                        pyrosim.Send_Joint(name = joint_name , parent= parent , child = block_name , 
                            type = type, position = [prev_depth/2,prev_width/2,0], jointAxis= axis)
                        self.parts.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
                                                    'position':[copy.copy(prev_depth)/2,copy.copy(prev_width)/2,0], 'jointAxis':axis}])
                    elif prev_direction == 3:
                        pyrosim.Send_Joint(name = joint_name , parent= parent , child = block_name , 
                            type = type, position = [prev_depth/2,0,prev_height/2], jointAxis= axis)
                        self.parts.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
                                                    'position':[copy.copy(prev_depth)/2,0,copy.copy(prev_height)/2], 'jointAxis':axis}])
                    else:
                        pyrosim.Send_Joint(name = joint_name , parent= parent , child = block_name , 
                            type = type, position = [prev_depth,0,0], jointAxis= axis) 
                        self.parts.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
                                                    'position':[copy.copy(prev_depth),0,0], 'jointAxis':axis}])                      
                    if random_sensor:
                        pyrosim.Send_Cube(name = block_name, pos= [depth/2,0,0],size = [depth,width,height],color="green",rgba = ["0","1.0","0","1,0"])
                        self.parts.append([0,{'name': block_name, 'pos':[copy.copy(depth)/2,0,0],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)],'color': "green", 'rgba': ["0","1.0","0","1,0"]}])
                    else:
                        pyrosim.Send_Cube(name = block_name, pos= [depth/2,0,0],size = [depth,width,height])
                        self.parts.append([1,{'name': block_name, 'pos':[copy.copy(depth)/2,0,0],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)]}])
            elif path == 3:
                if i == 0:
                    pyrosim.Send_Joint(name = joint_name   , parent= parent , child = block_name , 
                        type = type, position = [0,0,0.5 + prev_height / 2], jointAxis= axis)
                    self.parts.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
                                                'position':[0,0,0.5 + copy.copy(prev_height) / 2], 'jointAxis':axis}])
                    if random_sensor:
                        pyrosim.Send_Cube(name = block_name, pos= [0,0,height/2],size = [depth,width,height],color="green",rgba = ["0","1.0","0","1,0"])
                        self.parts.append([0,{'name': block_name, 'pos':[0,0,copy.copy(height)/2],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)],'color': "green", 'rgba': ["0","1.0","0","1,0"]}])
                    else:
                        pyrosim.Send_Cube(name = block_name, pos= [0,0,height/2],size = [depth,width,height])
                        self.parts.append([1,{'name': block_name, 'pos':[0,0,copy.copy(height)/2],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)]}])
                else:
                    if prev_direction == 1:
                        pyrosim.Send_Joint(name = joint_name , parent= parent , child = block_name , 
                            type = type, position = [0,prev_width/2,prev_height/2], jointAxis= axis)
                        self.parts.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
                                                    'position':[0,copy.copy(prev_width)/2,copy.copy(prev_height)/2], 'jointAxis':axis}])
                    elif prev_direction == 2:
                        pyrosim.Send_Joint(name = joint_name , parent= parent , child = block_name , 
                         type = type, position = [prev_depth/2,0,prev_height/2], jointAxis= axis)
                        self.parts.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
                                                    'position':[copy.copy(prev_depth)/2,0,copy.copy(prev_height)/2], 'jointAxis':axis}])
                    else: 
                        pyrosim.Send_Joint(name = joint_name , parent= parent , child = block_name , 
                        type = type, position = [0,0,prev_height], jointAxis= axis)
                        self.parts.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
                                                'position':[0,0,copy.copy(prev_height)], 'jointAxis':axis}])
                    if random_sensor:
                        pyrosim.Send_Cube(name = block_name, pos= [0,0,height/2],size = [depth,width,height],color="green",rgba = ["0","1.0","0","1,0"])
                        self.parts.append([0,{'name': block_name, 'pos':[0,0,copy.copy(height)/2],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)],'color': "green", 'rgba': ["0","1.0","0","1,0"]}])
                    else:
                        pyrosim.Send_Cube(name = block_name, pos= [0,0,height/2],size = [depth,width,height])
                        self.parts.append([1,{'name': block_name, 'pos':[0,0,copy.copy(height)/2],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)]}])                
            
        

            parent = block_name
            prev_width = width
            prev_depth = depth
            prev_height = height
            prev_direction = path
            joint_num +=1

            if random_sensor:
                self.links.append(block_name)
                self.numSensorsNeurons +=1

            self.joints.append(joint_name)
            self.links_.append([prev_width, prev_depth, prev_height,prev_direction,joint_num,parent])

       

        pyrosim.End()

    def create_body_helper(self,prev_width, prev_depth, prev_height,prev_direction,joint_num,parent):
        depth = random.random() + 0.01 
        width = random.random() * 2 + 0.01 
        height = random.random() + 0.01 
        direction = random.randint(1,3)
        block_name = "Block" + str(joint_num)
        joint_name = parent + "_" + block_name
        random_axis = random.randint(1,20)
        axis = ''
        if random_axis == 1 or random_axis > 6:
            axis = '1 0 0'
        elif random_axis == 2:
            axis = '0 1 0'
        elif random_axis == 3:
            axis = '0 0 1'
        elif random_axis == 4: 
            axis = '1 1 0'
        elif random_axis == 5: 
            axis = '1 0 1'
        elif random_axis == 6:
            axis = '0 1 1'
        type = 'revolute'
        # floating = random.randint(0,10) % 10 == 0
        # if floating: 
            # type = 'floating'
        if direction == 1:
            if prev_direction == 2:
                self.pieces.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
                                            'position':[copy.copy(prev_depth)/2,copy.copy(prev_width)/2,0], 'jointAxis':axis}])
            elif prev_direction == 3:
                self.pieces.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
                                            'position':[0,copy.copy(prev_width)/2,copy.copy(prev_height)/2], 'jointAxis':axis}])
            else:
                self.pieces.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
                                         'position':[0,copy.copy(prev_width)/2,0], 'jointAxis':axis}])  
            self.pieces.append([1,{'name': block_name, 'pos':[0,copy.copy(width)/2,0],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)]}])
        elif direction == 2:
            if prev_direction == 1:
                self.pieces.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
                                            'position':[copy.copy(prev_depth)/2,copy.copy(prev_width)/2,0], 'jointAxis':axis}])
            elif prev_direction == 3:
                self.pieces.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
                                            'position':[copy.copy(prev_depth)/2,0,copy.copy(prev_height)/2], 'jointAxis':axis}])
            else:
                self.pieces.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
                                            'position':[copy.copy(prev_depth),0,0], 'jointAxis':axis}])                      
            self.pieces.append([1,{'name': block_name, 'pos':[copy.copy(depth)/2,0,0],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)]}])
        elif direction == 3:
            if prev_direction == 1:
                self.pieces.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
                                            'position':[0,copy.copy(prev_width)/2,copy.copy(prev_height)/2], 'jointAxis':axis}])
            elif prev_direction == 2:
                self.pieces.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
                                            'position':[copy.copy(prev_depth)/2,0,copy.copy(prev_height)/2], 'jointAxis':axis}])
            else: 
                self.pieces.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
                                        'position':[0,0,copy.copy(prev_height)], 'jointAxis':axis}])
            self.pieces.append([1,{'name': block_name, 'pos':[0,0,copy.copy(height)/2],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)]}])                
        else:
            print(direction)
            exit()
    
        parent = block_name
        prev_width = width
        prev_depth = depth
        prev_height = height
        prev_direction = direction
        joint_num +=1
        self.unclaimedJoints.append(joint_name)
        self.lastlinks.append([prev_width, prev_depth, prev_height,prev_direction,joint_num,parent])

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
             pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn + self.numSensorsNeurons, weight = self.weights[currentRow][currentColumn] )
        
        pyrosim.End()

    def Mutate(self):
        if random.random() >= .25:
        
            column = random.randint(0,self.numMotorNeurons - 1)
            row = random.randint(0,self.numSensorsNeurons - 1)
            
            val = random.random() * 2 - 1

            self.weights[row][column] =  val


        if random.random() <= .2:
            self.change_sensors()
        if random.random() <= .05:
            self.add_link()
        if random.random() <= .05:
            self.remove_link()
        
        
        if random.random() < .1:
            if random.random() < .5:
                self.Remove_Motor_Neuron()
            else:
                self.Add_Motor_Neuron()

        self.Recreate_Body()
        self.Create_Brain()

    
    def Set_ID(self, ID):
        self.myID = ID

