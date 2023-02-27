# # # I did something to my a6.py file and now it is not working. I am not sure what I did, but I was unable to fix it.
# # # I was able to build my a7 on top of a friend's (austin p.) a6 instead. Much of the original files are similar except for 
# # # the ones related to this assignment (i.e. solution)

# import numpy 
# import random 
# import os 
# import time
# import copy
# import pyrosim.pyrosim as pyrosim
# from simulate import simulate

# import constants as c 
# length = 1
# width = 1
# height = 1

# x = 0
# y = 0
# z = 0.5

# class SOLUTION():
#     def __init__(self, nextAvailableID) -> None:
#         self.myID = nextAvailableID
#         self.fitness = 0
#         self.Create_World()
#         self.idNum = 0 
#         self.links = []
#         self.joints = []
#         self.numSensorsNeurons = 0 
#         self.numMotorNeurons = 0
        
#         self.joints_ = []
#         self.links_ = []
#         self.parts = []


#         self.Create_Body()
#         self.weights = numpy.random.rand(self.numSensorsNeurons,self.numMotorNeurons)
#         self.weights = self.weights * 2 - 1
#         self.Create_Brain()
       
       

#     def Start_Simulation(self, directorgui):
#         print(self.myID)
#         simulate(directorgui, str(self.myID), self.links, self.joints)

#     def Wait_For_Simulation_To_End(self):
#         while not os.path.exists("fitness{}.txt".format(self.myID)):
#             time.sleep(0.01)
#         with open("fitness{}.txt".format(self.myID),'r') as f:
#             self.fitness = float(f.read()) 
#         os.system("rm fitness{}.txt".format(self.myID))

#     def Evaluate(self, directorgui):
#         self.Start_Simulation(directorgui)

#     def Create_World(self):
#        pyrosim.Start_SDF("boxes.sdf")
#        pyrosim.End()


#     def Create_Body(self):
#         pyrosim.Start_URDF("body.urdf")
#         random_sensor = random.randint(0,1)
#         depth = random.random() + 0.01
#         width = random.random() * 2 + 0.01 
#         height = random.random() + 0.01 
        
#         # prevs = [depth, width, height]
#         prev_width = width
#         prev_depth = depth 
#         prev_height = height 

#         prev_direction = 1

#         if random_sensor:
#             self.links.append("Torso")
#             pyrosim.Send_Cube(name="Torso", pos=[0,0,0.5] , size=[depth, width, height], color="green",rgba = ["0","1.0","0","1,0"])
#             self.parts.append([0, {'name': "Torso", 'pos':[0,0,0.5],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)],'color': "green", 'rgba': ["0","1.0","0","1,0"]}])

#         else:
#             pyrosim.Send_Cube(name="Torso", pos=[0,0,0.5] , size=[depth, width, height])
#             self.parts.append([1,{'name': "Torso", 'pos':[0,0,0.5],'size': [copy.copy(depth) ,copy.copy(width) ,copy.copy(height)]}])

        
#         random_num_blocks = random.randint(1,10)
#         parent = "Torso"
#         joint_num = 0
#         self.numMotorNeurons = random_num_blocks 
        
#         for i in range (random_num_blocks):
#             random_sensor = random.randint(0,1)
         
#             depth = random.random() + 0.01 
#             width = random.random() * 2 + 0.01 
#             height = random.random() + 0.01 


#             block_name = "Block" + str(joint_num)
#             joint_name = parent + "_" + block_name

#             type = 'revolute'
        
#             path = random.randint(1,3)

#             random_axis = random.randint(1,20)
#             axis = ''
#             if random_axis == 1 or random_axis > 6:
#                 axis = '1 0 0'
#             elif random_axis == 2:
#                 axis = '0 1 0'
#             elif random_axis == 3:
#                 axis = '0 0 1'
#             elif random_axis == 4: 
#                 axis = '1 1 0'
#             elif random_axis == 5: 
#                 axis = '1 0 1'
#             elif random_axis == 6:
#                 axis = '0 1 1'

#             if path == 1:
#                 if i == 0:
#                     pyrosim.Send_Joint(name = joint_name   , parent= parent , child = block_name , 
#                         type = type, position = [0,prev_width/2,0.5], jointAxis= axis)
#                     self.parts.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
#                             'position':[0,copy.copy(prev_width)/2,0.5], 'jointAxis':axis}])
                    
#                     if random_sensor:
#                         pyrosim.Send_Cube(name = block_name, pos= [0,width/2,0],size = [depth,width,height],color="green",rgba = ["0","1.0","0","1,0"])
#                         self.parts.append([0,{'name': block_name, 'pos':[0,copy.copy(width)/2,0],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)],'color': "green", 'rgba': ["0","1.0","0","1,0"]}])
#                     else:
#                         pyrosim.Send_Cube(name = block_name, pos= [0,width/2,0],size = [depth,width,height])
#                         self.parts.append([1,{'name': block_name, 'pos':[0,copy.copy(width)/2,0],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)]}])
#                 else:
#                     if prev_direction == 2:
#                         pyrosim.Send_Joint(name = joint_name , parent= parent , child = block_name , 
#                             type = type, position = [prev_depth/2,prev_width/2,0], jointAxis= axis)
#                         self.parts.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
#                                                     'position':[copy.copy(prev_depth)/2,copy.copy(prev_width)/2,0], 'jointAxis':axis}])
#                     elif prev_direction == 3:
#                         pyrosim.Send_Joint(name = joint_name , parent= parent , child = block_name , 
#                         type = type, position = [0,prev_width/2,prev_height/2], jointAxis= axis)
#                         self.parts.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
#                                                     'position':[0,copy.copy(prev_width)/2,copy.copy(prev_height)/2], 'jointAxis':axis}])
#                     else:
#                         pyrosim.Send_Joint(name = joint_name , parent= parent , child = block_name , 
#                         type = type, position = [0,prev_width/2,0], jointAxis= axis) 
#                         self.parts.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
#                                                  'position':[0,copy.copy(prev_width)/2,0], 'jointAxis':axis}])  
#                     if random_sensor:
#                         pyrosim.Send_Cube(name = block_name, pos= [0,width/2,0],size = [depth,width,height],color="green",rgba = ["0","1.0","0","1,0"])
#                         self.parts.append([0,{'name': block_name, 'pos':[0,copy.copy(width)/2,0],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)],'color': "green", 'rgba': ["0","1.0","0","1,0"]}])
#                     else:
#                         pyrosim.Send_Cube(name = block_name, pos= [0,width/2,0],size = [depth,width,height])
#                         self.parts.append([1,{'name': block_name, 'pos':[0,copy.copy(width)/2,0],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)]}])
#             elif path == 2:
#                 if i == 0:
#                     pyrosim.Send_Joint(name = joint_name   , parent= parent , child = block_name , 
#                         type = type, position = [prev_depth/2,0,0.5], jointAxis= axis)
#                     self.parts.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
#                                                 'position':[copy.copy(prev_depth)/2,0,0.5], 'jointAxis':axis}])
#                     if random_sensor:
#                         pyrosim.Send_Cube(name = block_name, pos= [depth/2,0,0],size = [depth,width,height],color="green",rgba = ["0","1.0","0","1,0"])
#                         self.parts.append([0,{'name': block_name, 'pos':[copy.copy(depth)/2,0,0],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)],'color': "green", 'rgba': ["0","1.0","0","1,0"]}])
#                     else:
#                         pyrosim.Send_Cube(name = block_name, pos= [depth/2,0,0],size = [depth,width,height])
#                         self.parts.append([1,{'name': block_name, 'pos':[copy.copy(depth)/2,0,0],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)]}])
#                 else:
#                     if prev_direction == 1:
#                         pyrosim.Send_Joint(name = joint_name , parent= parent , child = block_name , 
#                             type = type, position = [prev_depth/2,prev_width/2,0], jointAxis= axis)
#                         self.parts.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
#                                                     'position':[copy.copy(prev_depth)/2,copy.copy(prev_width)/2,0], 'jointAxis':axis}])
#                     elif prev_direction == 3:
#                         pyrosim.Send_Joint(name = joint_name , parent= parent , child = block_name , 
#                             type = type, position = [prev_depth/2,0,prev_height/2], jointAxis= axis)
#                         self.parts.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
#                                                     'position':[copy.copy(prev_depth)/2,0,copy.copy(prev_height)/2], 'jointAxis':axis}])
#                     else:
#                         pyrosim.Send_Joint(name = joint_name , parent= parent , child = block_name , 
#                             type = type, position = [prev_depth,0,0], jointAxis= axis) 
#                         self.parts.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
#                                                     'position':[copy.copy(prev_depth),0,0], 'jointAxis':axis}])                      
#                     if random_sensor:
#                         pyrosim.Send_Cube(name = block_name, pos= [depth/2,0,0],size = [depth,width,height],color="green",rgba = ["0","1.0","0","1,0"])
#                         self.parts.append([0,{'name': block_name, 'pos':[copy.copy(depth)/2,0,0],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)],'color': "green", 'rgba': ["0","1.0","0","1,0"]}])
#                     else:
#                         pyrosim.Send_Cube(name = block_name, pos= [depth/2,0,0],size = [depth,width,height])
#                         self.parts.append([1,{'name': block_name, 'pos':[copy.copy(depth)/2,0,0],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)]}])
#             elif path == 3:
#                 if i == 0:
#                     pyrosim.Send_Joint(name = joint_name   , parent= parent , child = block_name , 
#                         type = type, position = [0,0,0.5 + prev_height / 2], jointAxis= axis)
#                     self.parts.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
#                                                 'position':[0,0,0.5 + copy.copy(prev_height) / 2], 'jointAxis':axis}])
#                     if random_sensor:
#                         pyrosim.Send_Cube(name = block_name, pos= [0,0,height/2],size = [depth,width,height],color="green",rgba = ["0","1.0","0","1,0"])
#                         self.parts.append([0,{'name': block_name, 'pos':[0,0,copy.copy(height)/2],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)],'color': "green", 'rgba': ["0","1.0","0","1,0"]}])
#                     else:
#                         pyrosim.Send_Cube(name = block_name, pos= [0,0,height/2],size = [depth,width,height])
#                         self.parts.append([1,{'name': block_name, 'pos':[0,0,copy.copy(height)/2],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)]}])
#                 else:
#                     if prev_direction == 1:
#                         pyrosim.Send_Joint(name = joint_name , parent= parent , child = block_name , 
#                             type = type, position = [0,prev_width/2,prev_height/2], jointAxis= axis)
#                         self.parts.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
#                                                     'position':[0,copy.copy(prev_width)/2,copy.copy(prev_height)/2], 'jointAxis':axis}])
#                     elif prev_direction == 2:
#                         pyrosim.Send_Joint(name = joint_name , parent= parent , child = block_name , 
#                          type = type, position = [prev_depth/2,0,prev_height/2], jointAxis= axis)
#                         self.parts.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
#                                                     'position':[copy.copy(prev_depth)/2,0,copy.copy(prev_height)/2], 'jointAxis':axis}])
#                     else: 
#                         pyrosim.Send_Joint(name = joint_name , parent= parent , child = block_name , 
#                         type = type, position = [0,0,prev_height], jointAxis= axis)
#                         self.parts.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
#                                                 'position':[0,0,copy.copy(prev_height)], 'jointAxis':axis}])
#                     if random_sensor:
#                         pyrosim.Send_Cube(name = block_name, pos= [0,0,height/2],size = [depth,width,height],color="green",rgba = ["0","1.0","0","1,0"])
#                         self.parts.append([0,{'name': block_name, 'pos':[0,0,copy.copy(height)/2],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)],'color': "green", 'rgba': ["0","1.0","0","1,0"]}])
#                     else:
#                         pyrosim.Send_Cube(name = block_name, pos= [0,0,height/2],size = [depth,width,height])
#                         self.parts.append([1,{'name': block_name, 'pos':[0,0,copy.copy(height)/2],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)]}])                
            
        

#             parent = block_name
#             prev_width = width
#             prev_depth = depth
#             prev_height = height
#             prev_direction = path
#             joint_num +=1

#             if random_sensor:
#                 self.links.append(block_name)
#                 self.numSensorsNeurons +=1

#             self.joints.append(joint_name)
#             self.links_.append([prev_width, prev_depth, prev_height,prev_direction,joint_num,parent])

       

#         pyrosim.End()

#     def create_body_helper(self,prev_width, prev_depth, prev_height,prev_direction,joint_num,parent):
#         depth = random.random() + 0.01 
#         width = random.random() * 2 + 0.01 
#         height = random.random() + 0.01 
#         direction = random.randint(1,3)
#         block_name = "Block" + str(joint_num)
#         joint_name = parent + "_" + block_name
#         random_axis = random.randint(1,20)
#         axis = ''
#         if random_axis == 1 or random_axis > 6:
#             axis = '1 0 0'
#         elif random_axis == 2:
#             axis = '0 1 0'
#         elif random_axis == 3:
#             axis = '0 0 1'
#         elif random_axis == 4: 
#             axis = '1 1 0'
#         elif random_axis == 5: 
#             axis = '1 0 1'
#         elif random_axis == 6:
#             axis = '0 1 1'
#         type = 'revolute'
#         # floating = random.randint(0,10) % 10 == 0
#         # if floating: 
#             # type = 'floating'
#         if direction == 1:
#             if prev_direction == 2:
#                 self.pieces.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
#                                             'position':[copy.copy(prev_depth)/2,copy.copy(prev_width)/2,0], 'jointAxis':axis}])
#             elif prev_direction == 3:
#                 self.pieces.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
#                                             'position':[0,copy.copy(prev_width)/2,copy.copy(prev_height)/2], 'jointAxis':axis}])
#             else:
#                 self.pieces.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
#                                          'position':[0,copy.copy(prev_width)/2,0], 'jointAxis':axis}])  
#             self.pieces.append([1,{'name': block_name, 'pos':[0,copy.copy(width)/2,0],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)]}])
#         elif direction == 2:
#             if prev_direction == 1:
#                 self.pieces.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
#                                             'position':[copy.copy(prev_depth)/2,copy.copy(prev_width)/2,0], 'jointAxis':axis}])
#             elif prev_direction == 3:
#                 self.pieces.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
#                                             'position':[copy.copy(prev_depth)/2,0,copy.copy(prev_height)/2], 'jointAxis':axis}])
#             else:
#                 self.pieces.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
#                                             'position':[copy.copy(prev_depth),0,0], 'jointAxis':axis}])                      
#             self.pieces.append([1,{'name': block_name, 'pos':[copy.copy(depth)/2,0,0],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)]}])
#         elif direction == 3:
#             if prev_direction == 1:
#                 self.pieces.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
#                                             'position':[0,copy.copy(prev_width)/2,copy.copy(prev_height)/2], 'jointAxis':axis}])
#             elif prev_direction == 2:
#                 self.pieces.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
#                                             'position':[copy.copy(prev_depth)/2,0,copy.copy(prev_height)/2], 'jointAxis':axis}])
#             else: 
#                 self.pieces.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
#                                         'position':[0,0,copy.copy(prev_height)], 'jointAxis':axis}])
#             self.pieces.append([1,{'name': block_name, 'pos':[0,0,copy.copy(height)/2],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)]}])                
#         else:
#             print(direction)
#             exit()
    
#         parent = block_name
#         prev_width = width
#         prev_depth = depth
#         prev_height = height
#         prev_direction = direction
#         joint_num +=1
#         self.unclaimedJoints.append(joint_name)
#         self.lastlinks.append([prev_width, prev_depth, prev_height,prev_direction,joint_num,parent])

#     def Create_Brain(self):
#         pyrosim.Start_NeuralNetwork("brain{}.nndf".format(self.myID))
#         for link in self.links: 
#             pyrosim.Send_Sensor_Neuron(name = self.idNum , linkName = link)
#             self.idNum +=1 


#         for joint in self.joints:
#             pyrosim.Send_Motor_Neuron( name = self.idNum , jointName = joint)
#             self.idNum +=1
    


#         for currentRow in range(self.numSensorsNeurons): 
#          for currentColumn in range(self.numMotorNeurons): 
#              pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn + self.numSensorsNeurons, weight = self.weights[currentRow][currentColumn] )
        
#         pyrosim.End()

#     def Mutate(self):
#         row = random.randint(0,2)
#         column = random.randint(0,1)
#         self.weights[row][column] =  random.random() * 2 - 1

    
#     def Set_ID(self, ID):
#         self.myID = ID

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
        self.pieces = []
        self.unclaimedJoints = []
        self.lastlinks = []

        self.Create_Body()
        self.weights = numpy.random.rand(self.numSensorsNeurons,self.numMotorNeurons)
        self.weights = self.weights * 2 - 1
        self.Create_Brain()
        
    def Start_Simulation(self,directorgui):
        # print('Weights for this round are:', self.weights)
        print("Running simulate")
        # os.system("python3 simulate.py " + directorgui + " " + str(self.myID) + " 2&>1 &")
        simulate(directorgui,str(self.myID),self.links,self.joints)
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
        pyrosim.Start_URDF("body{}.urdf".format(self.myID))
        random_sensor = random.randint(0,10)
        depth = random.random() + 0.01
        width = random.random() * 2 + 0.01 
        height = random.random() + 0.01 
        prev_width = width
        prev_depth = depth 
        prev_height = height 
        prev_direction = 1
        if random_sensor % 2 == 0:
            self.links.append("Torso")
            self.numSensorsNeurons +=1
            pyrosim.Send_Cube(name="Torso", pos=[0,0,0.5] , size=[depth ,width ,height ], color="green",rgba = ["0","1.0","0","1,0"])
            self.pieces.append([0,{'name': "Torso", 'pos':[0,0,0.5],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)],'color': "green", 'rgba': ["0","1.0","0","1,0"]}])
        else:
            pyrosim.Send_Cube(name="Torso", pos=[0,0,0.5] , size=[depth ,width ,height ])
            self.pieces.append([1,{'name': "Torso", 'pos':[0,0,0.5],'size': [copy.copy(depth) ,copy.copy(width) ,copy.copy(height)]}])
        
        random_num_blocks = random.randint(1,10)
        print("Randomly decided on ", random_num_blocks, " blocks")
        parent = "Torso"
        joint_num = 0
        self.numMotorNeurons = random_num_blocks 
        for i in range (random_num_blocks):
            random_sensor = random.randint(0,10)
            if random_sensor % 2 == 0:
                random_sensor = True
            else:
                random_sensor = False
            
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
                if i == 0:
                    pyrosim.Send_Joint(name = joint_name   , parent= parent , child = block_name , 
                        type = type, position = [0,prev_width/2,0.5], jointAxis= axis)
                    self.pieces.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
                            'position':[0,copy.copy(prev_width)/2,0.5], 'jointAxis':axis}])
                    
                    if random_sensor:
                        pyrosim.Send_Cube(name = block_name, pos= [0,width/2,0],size = [depth,width,height],color="green",rgba = ["0","1.0","0","1,0"])
                        self.pieces.append([0,{'name': block_name, 'pos':[0,copy.copy(width)/2,0],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)],'color': "green", 'rgba': ["0","1.0","0","1,0"]}])
                    else:
                        pyrosim.Send_Cube(name = block_name, pos= [0,width/2,0],size = [depth,width,height])
                        self.pieces.append([1,{'name': block_name, 'pos':[0,copy.copy(width)/2,0],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)]}])
                else:
                    if prev_direction == 2:
                        pyrosim.Send_Joint(name = joint_name , parent= parent , child = block_name , 
                            type = type, position = [prev_depth/2,prev_width/2,0], jointAxis= axis)
                        self.pieces.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
                                                    'position':[copy.copy(prev_depth)/2,copy.copy(prev_width)/2,0], 'jointAxis':axis}])
                    elif prev_direction == 3:
                        pyrosim.Send_Joint(name = joint_name , parent= parent , child = block_name , 
                        type = type, position = [0,prev_width/2,prev_height/2], jointAxis= axis)
                        self.pieces.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
                                                    'position':[0,copy.copy(prev_width)/2,copy.copy(prev_height)/2], 'jointAxis':axis}])
                    else:
                        pyrosim.Send_Joint(name = joint_name , parent= parent , child = block_name , 
                        type = type, position = [0,prev_width/2,0], jointAxis= axis) 
                        self.pieces.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
                                                 'position':[0,copy.copy(prev_width)/2,0], 'jointAxis':axis}])  
                    if random_sensor:
                        pyrosim.Send_Cube(name = block_name, pos= [0,width/2,0],size = [depth,width,height],color="green",rgba = ["0","1.0","0","1,0"])
                        self.pieces.append([0,{'name': block_name, 'pos':[0,copy.copy(width)/2,0],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)],'color': "green", 'rgba': ["0","1.0","0","1,0"]}])
                    else:
                        pyrosim.Send_Cube(name = block_name, pos= [0,width/2,0],size = [depth,width,height])
                        self.pieces.append([1,{'name': block_name, 'pos':[0,copy.copy(width)/2,0],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)]}])
            elif direction == 2:
                if i == 0:
                    pyrosim.Send_Joint(name = joint_name   , parent= parent , child = block_name , 
                        type = type, position = [prev_depth/2,0,0.5], jointAxis= axis)
                    self.pieces.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
                                                'position':[copy.copy(prev_depth)/2,0,0.5], 'jointAxis':axis}])
                    if random_sensor:
                        pyrosim.Send_Cube(name = block_name, pos= [depth/2,0,0],size = [depth,width,height],color="green",rgba = ["0","1.0","0","1,0"])
                        self.pieces.append([0,{'name': block_name, 'pos':[copy.copy(depth)/2,0,0],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)],'color': "green", 'rgba': ["0","1.0","0","1,0"]}])
                    else:
                        pyrosim.Send_Cube(name = block_name, pos= [depth/2,0,0],size = [depth,width,height])
                        self.pieces.append([1,{'name': block_name, 'pos':[copy.copy(depth)/2,0,0],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)]}])
                else:
                    if prev_direction == 1:
                        pyrosim.Send_Joint(name = joint_name , parent= parent , child = block_name , 
                            type = type, position = [prev_depth/2,prev_width/2,0], jointAxis= axis)
                        self.pieces.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
                                                    'position':[copy.copy(prev_depth)/2,copy.copy(prev_width)/2,0], 'jointAxis':axis}])
                    elif prev_direction == 3:
                        pyrosim.Send_Joint(name = joint_name , parent= parent , child = block_name , 
                            type = type, position = [prev_depth/2,0,prev_height/2], jointAxis= axis)
                        self.pieces.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
                                                    'position':[copy.copy(prev_depth)/2,0,copy.copy(prev_height)/2], 'jointAxis':axis}])
                    else:
                        pyrosim.Send_Joint(name = joint_name , parent= parent , child = block_name , 
                            type = type, position = [prev_depth,0,0], jointAxis= axis) 
                        self.pieces.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
                                                    'position':[copy.copy(prev_depth),0,0], 'jointAxis':axis}])                      
                    if random_sensor:
                        pyrosim.Send_Cube(name = block_name, pos= [depth/2,0,0],size = [depth,width,height],color="green",rgba = ["0","1.0","0","1,0"])
                        self.pieces.append([0,{'name': block_name, 'pos':[copy.copy(depth)/2,0,0],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)],'color': "green", 'rgba': ["0","1.0","0","1,0"]}])
                    else:
                        pyrosim.Send_Cube(name = block_name, pos= [depth/2,0,0],size = [depth,width,height])
                        self.pieces.append([1,{'name': block_name, 'pos':[copy.copy(depth)/2,0,0],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)]}])
            elif direction == 3:
                if i == 0:
                    pyrosim.Send_Joint(name = joint_name   , parent= parent , child = block_name , 
                        type = type, position = [0,0,0.5 + prev_height / 2], jointAxis= axis)
                    self.pieces.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
                                                'position':[0,0,0.5 + copy.copy(prev_height) / 2], 'jointAxis':axis}])
                    if random_sensor:
                        pyrosim.Send_Cube(name = block_name, pos= [0,0,height/2],size = [depth,width,height],color="green",rgba = ["0","1.0","0","1,0"])
                        self.pieces.append([0,{'name': block_name, 'pos':[0,0,copy.copy(height)/2],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)],'color': "green", 'rgba': ["0","1.0","0","1,0"]}])
                    else:
                        pyrosim.Send_Cube(name = block_name, pos= [0,0,height/2],size = [depth,width,height])
                        self.pieces.append([1,{'name': block_name, 'pos':[0,0,copy.copy(height)/2],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)]}])
                else:
                    if prev_direction == 1:
                        pyrosim.Send_Joint(name = joint_name , parent= parent , child = block_name , 
                            type = type, position = [0,prev_width/2,prev_height/2], jointAxis= axis)
                        self.pieces.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
                                                    'position':[0,copy.copy(prev_width)/2,copy.copy(prev_height)/2], 'jointAxis':axis}])
                    elif prev_direction == 2:
                        pyrosim.Send_Joint(name = joint_name , parent= parent , child = block_name , 
                         type = type, position = [prev_depth/2,0,prev_height/2], jointAxis= axis)
                        self.pieces.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
                                                    'position':[copy.copy(prev_depth)/2,0,copy.copy(prev_height)/2], 'jointAxis':axis}])
                    else: 
                        pyrosim.Send_Joint(name = joint_name , parent= parent , child = block_name , 
                        type = type, position = [0,0,prev_height], jointAxis= axis)
                        self.pieces.append([2,{'name':joint_name,'parent':parent,'child':block_name,'type':type,
                                                'position':[0,0,copy.copy(prev_height)], 'jointAxis':axis}])
                    if random_sensor:
                        pyrosim.Send_Cube(name = block_name, pos= [0,0,height/2],size = [depth,width,height],color="green",rgba = ["0","1.0","0","1,0"])
                        self.pieces.append([0,{'name': block_name, 'pos':[0,0,copy.copy(height)/2],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)],'color': "green", 'rgba': ["0","1.0","0","1,0"]}])
                    else:
                        pyrosim.Send_Cube(name = block_name, pos= [0,0,height/2],size = [depth,width,height])
                        self.pieces.append([1,{'name': block_name, 'pos':[0,0,copy.copy(height)/2],'size':[copy.copy(depth) ,copy.copy(width) ,copy.copy(height)]}])                
            
        

            parent = block_name
            prev_width = width
            prev_depth = depth
            prev_height = height
            prev_direction = direction
            joint_num +=1
            if random_sensor:
                self.links.append(block_name)
                self.numSensorsNeurons +=1
            self.joints.append(joint_name)
            self.lastlinks.append([prev_width, prev_depth, prev_height,prev_direction,joint_num,parent])
        # print(self.joints)
        # print(self.links)

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
        self.idNum = 0 
        for link in self.links: 
            pyrosim.Send_Sensor_Neuron(name = self.idNum , linkName = link)
            self.idNum +=1 
            # print("attempted to add link")

        for joint in self.joints:
            pyrosim.Send_Motor_Neuron( name = self.idNum , jointName = joint)
            self.idNum +=1
            # print("attempted to add motor")

        for currentRow in range(self.numSensorsNeurons - 1): 
            for currentColumn in range(self.numMotorNeurons - 1): 
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn + self.numSensorsNeurons, weight = self.weights[currentRow][currentColumn] )
        pyrosim.End()

    def Mutate(self):
        body_or_weights = random.randint(0,100)
        if body_or_weights < 70:
            try:
                row = random.randint(0,self.numSensorsNeurons - 1)
                column = random.randint(0,self.numMotorNeurons - 1)
                val = random.random() * 2 - 1
                self.weights[row][column] =  val 
            except ValueError as e :
                self.Mutate_Body()
        elif body_or_weights >= 70 and body_or_weights < 73:
            self.add_link()
        elif body_or_weights >= 73 and body_or_weights < 75:
            self.remove_link()
        elif body_or_weights >= 75 and body_or_weights < 90:
            self.Mutate_Body()
        elif body_or_weights >= 90 and body_or_weights <= 95:
            self.Remove_Motor_Neuron()
        else:
            self.Add_Motor_Neuron()
        self.Recreate_Body()
        self.Create_Brain()
        
    def Set_ID(self, ID):
        self.myID = ID

    def Recreate_Body(self):
        pyrosim.Start_URDF("body{}.urdf".format(self.myID))
        for piece in self.pieces: 
            if piece[0] == 0:
                link = piece[1]
                pyrosim.Send_Cube(name=link['name'], pos=link['pos'] , size=link['size'], color=link['color'],rgba = link['rgba'])
            elif piece[0] == 1:
                link = piece[1]
                pyrosim.Send_Cube(name=link['name'], pos=link['pos'] , size=link['size'])
            elif piece[0] == 2:
                joint = piece[1]
                pyrosim.Send_Joint(name = joint['name']   , parent= joint['parent'] , child = joint['child'] , 
                                type = joint['type'], position = joint['position'], jointAxis= joint['jointAxis']) 
        pyrosim.End()

    def add_link(self):
        if not self.lastlinks: return 
        last_link = self.lastlinks[-1]
        prev_width = last_link[0]
        prev_depth = last_link[1]
        prev_height = last_link[2]
        prev_direction = last_link[3]
        joint_num = last_link[4]
        parent = last_link[5]
        self.create_body_helper(prev_width,prev_depth,prev_height,prev_direction,joint_num,parent)

    def remove_link(self):
        if not self.pieces:return
        temp = self.pieces.pop()
        if not self.pieces:return
        joint = self.pieces.pop()
        if not self.lastlinks:return
        self.lastlinks.pop()
        if joint[1]['name'] in self.joints:
            self.Remove_Motor_Neuron(joint[1]['name'],False)
        if temp[1]['name'] in self.links:
            self.numSensorsNeurons -=1
            print(self.links)
            print(temp[1]['name'])
            index = self.links.index(temp[1]['name'])
            self.links.remove(temp[1]['name'])
            self.weights = numpy.delete(self.weights,index,axis=0)
      
    def Mutate_Body(self):
        if not self.pieces: return 
        piece_selection = random.randint(0,len(self.pieces) - 1)
        piece = self.pieces[piece_selection]
        if piece[0] == 0:
            sensored_link = piece[1]
            index = self.links.index(sensored_link['name'])
            self.links.remove(sensored_link['name']) 
            self.numSensorsNeurons -=1
            piece[0] = 1
            #Remove sensor 
            self.weights = numpy.delete(self.weights,index,axis=0)
        elif piece[0] == 1:
            unsensored_link = piece[1]
            self.links.append(unsensored_link['name'])
            self.numSensorsNeurons +=1
            piece[0] = 0
            piece[1]['color'] = "green"
            piece[1]['rgba'] = ["0","1.0","0","1,0"]
            #Add Sensor
            temp = numpy.random.rand(1,self.numMotorNeurons)
            self.weights = numpy.append(self.weights,temp,axis=0)
        elif piece[0] == 2:
            random_axis = random.randint(1,20)
            if random_axis == 1 or random_axis > 6:
                piece[1]['jointAxis'] = '0 1 0'
            elif random_axis == 2:
                piece[1]['jointAxis'] = '1 0 1'
            elif random_axis == 3:
                piece[1]['jointAxis'] = '0 0 1'
            elif random_axis == 4: 
                piece[1]['jointAxis'] = '1 0 0'
            elif random_axis == 5: 
                piece[1]['jointAxis'] = '0 1 1'
            elif random_axis == 6:
                piece[1]['jointAxis'] = '1 1 0'
            
    def Remove_Motor_Neuron(self,joint = None,dont_delete = True):
        if joint:
            joint = joint
            index = -1
        else:
            if not self.joints: return
            joint = random.choice(self.joints)
            index = self.joints.index(joint)

        self.joints.remove(joint)
      
        self.weights = numpy.delete(self.weights,index,axis=1)
        if dont_delete:
            self.unclaimedJoints.append(joint)
        self.numMotorNeurons -=1

    def Add_Motor_Neuron(self):
        if not self.unclaimedJoints: return 
        joint = random.choice(self.unclaimedJoints)
        self.numMotorNeurons +=1
        self.joints.append(joint)
        temp = numpy.random.rand(self.numSensorsNeurons,1)
        print(temp)
        print(self.weights)
        self.weights = numpy.append(self.weights,temp,axis=1)
            

