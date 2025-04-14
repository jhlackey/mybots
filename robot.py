import pybullet as p
import math
import constants
import constants as c
import numpy
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import random
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os

class ROBOT:
    def __init__(self, sensors, motors, solutionID):
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)  # robotid
         # This will create a neural network (self.nn), and add any neurons and synapses to it from brain.nndf.
        self.solutionID = solutionID
        # testing to find num joints
        # num_joints = p.getNumJoints(self.robotId)
        # print(f"Number of joints in robot: {num_joints}")

        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        # self.motors = {}

        self.nn = NEURAL_NETWORK("brain" + str(solutionID) + ".nndf") # Step 39
        os.system("rm brain" + str(solutionID) + ".nndf")


    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            # print(linkName)
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, timestep):
        for sensor in self.sensors.keys():
            self.sensors[sensor].Get_Value(timestep)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            # print(jointName)
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, timestep):
        for neuronName in self.nn.Get_Neuron_Names(): # Step 57
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName).encode("utf-8")
                desiredAngle = self.nn.Get_Value_Of(neuronName) * constants.motorJointRange
                # print(self.motors)
                self.motors[jointName].Set_Value(self.robotId, desiredAngle)
                jointName = jointName.decode('utf-8')
                # print(jointName, neuronName, desiredAngle)

        # for motor in self.motors.values():
        #     motor.Set_Value(self.robotId, timestep)
    #
    # def Save_Values(self, filepath, arr):
    #     numpy.save(filepath, arr)

    def Think(self):
        self.nn.Update()
        # self.nn.Print()

    def Get_Fitness(self):
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
        basePosition = basePositionAndOrientation[0]
        xPosition = basePosition[0]
        yPosition = basePosition[1]
        zPosition = basePosition[2]

        # stateOfLinkZero = p.getLinkState(self.robotId,0)
        # positionOfLinkZero = stateOfLinkZero[0]
        # xCoordinateOfLinkZero = positionOfLinkZero[0]

        # There is a potential problem here however: search.py may try to read in fitness before simulate.py has finished writing to it.
        # So, back in robot.py, write fitness into a file called tmpID.txt instead of fitnessID.txt
        f = open("tmp"+ self.solutionID + ".txt", mode="w")
        os.system("mv tmp" +  self.solutionID + ".txt fitness" +  self.solutionID + ".txt")
        fitness =  xPosition if zPosition >= 1.35 else 100
        fitness = fitness if abs(yPosition) < 2.5 else 100
        f.write(str(fitness))
        # f.write(str((2 * zPosition) * xPosition))
        f.close()
        # print('executed get_fitness in robot.py')

