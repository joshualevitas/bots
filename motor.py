
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import constants as c

class MOTOR:
    def __init__(self, jn) -> None:
        self.jointName = jn
        self.motor_values = np.linspace(0 , 2 * np.pi, 100)
        self.Prepare_to_Act()

    def Prepare_to_Act(self):
        self.amplitude = c.amplitude
        self.frequency = c.frequency
        self.phaseOffset = c.phaseOffset

        if self.jointName == 'Torso_BackLeg':
            self.frequency = self.frequency / 2 

        self.motor_values = self.amplitude * np.sin(self.frequency*self.motor_values+self.phaseOffset)

    def Set_Value(self,robotId,t):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotId,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = self.motor_values[t],
            maxForce = c.max_force)
    
    def Save_Values(self):
        numpy.save('data/{self.jointName}Motor.npy',self.motor_values)

