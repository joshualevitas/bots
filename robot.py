import pybullet as p
import pybullet_data
from motor import MOTOR
from sensor import SENSOR
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK


class ROBOT:
    def __init__(self):
        self.sensors = {}
        self.motors = {}
        self.nn = NEURAL_NETWORK("brain.nndf")

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
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(self.robotId, desiredAngle)
           

    def Think(self):
        self.nn.Update()
        # self.nn.Print()


    def get_fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotId,0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]

        f = open("fitness.txt", "w")
        f.write(str(xCoordinateOfLinkZero))
        f.close()