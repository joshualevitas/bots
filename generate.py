import pyrosim.pyrosim as pyrosim


def create_world():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[10,0,.5] , size=[1,1,1])
    pyrosim.End()

    return

def create_robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="torso", pos=[1.5,0,1.5] , size=[1, 1, 1])
    pyrosim.Send_Joint(name = "Torso_Leg" , parent= "torso" , child = "front_leg" , type = "revolute", position = [1,0,1])
    pyrosim.Send_Cube(name="front_leg", pos=[-.5,0,-.5] , size=[1, 1, 1])
    pyrosim.Send_Joint(name = "Torso_Leg2" , parent= "torso" , child = "back_leg" , type = "revolute", position = [2.5,0,1])
    pyrosim.Send_Cube(name="back_leg", pos=[0,0,-.5] , size=[1, 1, 1])


    pyrosim.End()
    return

create_world()
create_robot()