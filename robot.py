import pybullet as p
import pybullet_data
from motor import MOTOR
from sensor import SENSOR
import pyrosim.pyrosim as pyrosim


class ROBOT:
    def __init__(self):
        self.sensors = {}
        self.motors = {}

        self.robotId = p.loadURDF("body.urdf")

        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_to_Act()

    def Prepare_To_Sense(self):
        for ln in pyrosim.linkNamesToIndices:
            self.sensors[ln] = SENSOR(ln)

    def Prepare_to_Act(self):
        for jn in pyrosim.jointNamesToIndices:
            self.motors[jn] = MOTOR(jn)

    def Sense(self, t):
        for s in self.sensors:
            self.sensors[s].Get_Value(t)

    def Act(self, t):
        for m in self.motors:
            self.motors[m].Set_Value(self.robotId, t)