import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy as np
import random

# end imports
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = np.zeros(100)
frontLegSensorValues = np.zeros(100)
torsoSensorValues = np.zeros(100)

amplitude = np.pi/4
frequency = 1
phaseOffset = 0

targetAngles = np.linspace(0, 2*np.pi, 100)
targetAngles = [amplitude * np.sin(frequency * i + phaseOffset) for i in targetAngles]



for i in range(100):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = "Torso_BackLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = targetAngles[i],
        maxForce = 500)

    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = "Torso_FrontLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = targetAngles[i],
        maxForce = 500)



    

    time.sleep(1/120)

p.disconnect()

np.save("data/backlegsensorvalues.npy", backLegSensorValues)
np.save("data/frontlegsensorvalues.npy", frontLegSensorValues)
