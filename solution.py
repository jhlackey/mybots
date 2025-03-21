import numpy

import constants
import pyrosim.pyrosim as pyrosim
import random
import os
import time

from constants import numSensorNeurons, numMotorNeurons

# from simulate import directOrGUI

length = 1
width = 1
height = 1

class SOLUTION:
    def __init__(self, nextAvailableId):
        self.weights = numpy.matrix(numpy.random.rand(constants.numSensorNeurons,constants.numMotorNeurons))
        # print(self.weights)
        self.weights = self.weights * 2 - 1
        self.myID = nextAvailableId


    def Evaluate(self, directOrGUI):
        self.Create_World()
        self.Create_Robot()
        self.Create_Brain()

        prompt = f"python3.13 simulate.py {directOrGUI} {self.myID} 2>&1 &"
        os.system(prompt)
        fitnessFileName = "fitness" + self.myID + ".txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)

        f = open(fitnessFileName, "r")
        self.fitness = float(f.read()) # step 49
        f.close()

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Robot()
        self.Create_Brain()

        prompt = f"python3.13 simulate.py {directOrGUI} {self.myID}"
        os.system(prompt)

    def Wait_For_Simulation_To_End(self, directOrGUI):
        # f = open("fitness" + str(self.myID) + ".txt", "r")
        # self.fitness = float(f.read()) # step 49

        with open(f"fitness{self.myID}.txt", 'r') as f:
            self.fitness = float(f.read())

        os.system(f"rm fitness{self.myID}.txt")

        # print(self.fitness)
        # f.close()

        # print(os.path.exists("fitness" + str(self.myID) + ".txt"))
        # # print("removing fitness" + str(self.myID)  + "file")
        # os.system("rm fitness" + str (self.myID) + ".txt")
        # print(os.path.exists("fitness" + str(self.myID) + ".txt"))

    def Create_World(self):
        # while not os.path.exists('world.sdf'):
        #     time.sleep(0.01)

        #  tell pyrosim the name of the file where information about the world you're about to create should be stored. 
        pyrosim.Start_SDF("world.sdf")
        # stores a box with initial position x=0, y=0, z=0.5, and length, width and height all equal to 1 meter, in box.sdf.
        pyrosim.Send_Cube(name="Box", pos=[0 - 5, 0 + 5, 0.5], size=[length, width, height])
        pyrosim.End()
        # time.sleep(0.01)

        
    def Create_Robot(self):  # step 5, renamed Create_Robot()
        # while not os.path.exists('body.urdf'):
        #     time.sleep(0.01)

        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[length, width, height])
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[0, -0.5, 1.0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0], size=[0.2,1,0.2])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute",
                           position=[0, 0.5, 1.0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0], size=[0.2,1,0.2])
        # pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="FrontLeg", type="revolute",
        #                    position=[-0.5, 0, 1.0], jointAxis="1 0 0")
        # pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5, 0.5, 0], size=[1, 0.2, 0.2])
        pyrosim.End()


        # time.sleep(0.01)

    def Create_Brain(self):  # step 5, renamed Create_Robot()
        # while not os.path.exists('brain.nndf'):
        #     time.sleep(0.01)

        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        # motorNames = [3, 4]  # replace with indices
        # sensorNames = [0, 1, 2]

        # Inside generate, create two nested for loops.
        # The outer loop should iterate over the names of the three sensor neurons.
        # The inner loop should iterate over each of the two motor neurons.

        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        # pyrosim.Send_Sensor_Neuron(name=3, linkName="LeftLeg")
        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")
        # pyrosim.Send_Motor_Neuron(name=6, jointName="Torso_LeftLeg")

        # print(self.weights.shape)
        for currentRow in range(constants.numSensorNeurons):
            # print('row', currentRow)
            for currentColumn in range(constants.numMotorNeurons):
                # print('col', currentColumn)
                # print(self.weights[currentRow, currentColumn])
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+3, weight=self.weights[currentRow, currentColumn])

        pyrosim.End()
        # exit()
        # time.sleep(0.01)

    def Mutate(self):
        randomRow = random.randint(0,numSensorNeurons-1)
        randomCol = random.randint(0,numMotorNeurons-1)
        self.weights[randomRow, randomCol] = random.random() * 2 + 1

    def Set_ID(self, nextAvailableId):
        self.myID = nextAvailableId