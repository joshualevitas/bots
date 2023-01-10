import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

length = 1
width = 1
height = 1

x = 0
y = 0
z = .5

# pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
# pyrosim.Send_Cube(name="Box2", pos=[x+1,y,z+1] , size=[length,width,height])

for x_ in range(3):
    for y_ in range(3):
        for i in range(10):
            f = .9**i
            pyrosim.Send_Cube(name="Box", pos=[x+x_,y+y_,z+i] , size=[f*length,f*width,f*height])
    


pyrosim.End()