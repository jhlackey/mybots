import numpy
import pyrosim.pyrosim as pyrosim
import random
import os
import time

length = 1
width = 1
height = 1

class SOLUTION:
    def __init__(self):
        self.weights = numpy.matrix(numpy.random.rand(3,2))
        # print(self.weights)
        self.weights = self.weights * 2 - 1

        # print(self.weights)
        # exit()
        # pass

    def Evaluate(self, directOrGUI):
        self.Create_World()
        self.Create_Robot()
        self.Create_Brain()
        # os.system('python3 simulate.py ' + directOrGUI)
        os.system("python3 simulate.py " + directOrGUI + " &")
        # os.system("start /B python3 simulate.py " + directOrGUI)

        fitnessFile = 'fitness.txt'
        f = open(fitnessFile, "r")
        self.fitness = float(f.read()) # step 49
        f.close()

    def Create_World(self):
        while not os.path.exists('world.sdf'):
            time.sleep(0.01)
        #  tell pyrosim the name of the file where information about the world you're about to create should be stored. 
        pyrosim.Start_SDF("world.sdf")
        # stores a box with initial position x=0, y=0, z=0.5, and length, width and height all equal to 1 meter, in box.sdf.
        pyrosim.Send_Cube(name="Box", pos=[0 - 5, 0 + 5, 0.5], size=[length, width, height])
        pyrosim.End()
        # time.sleep(0.01)

        
    def Create_Robot(self):  # step 5, renamed Create_Robot()
        while not os.path.exists('body.urdf'):
            time.sleep(0.01)
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5], size=[length, width, height])
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[1, 0, 1.0])
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[length, width, height])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute",
                           position=[2, 0, 1.0])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[length, width, height])
        pyrosim.End()
        # time.sleep(0.01)

    def Create_Brain(self):  # step 5, renamed Create_Robot()
        while not os.path.exists('brain.nndf'):
            time.sleep(0.01)
        pyrosim.Start_NeuralNetwork("brain.nndf")
        # motorNames = [3, 4]  # replace with indices
        # sensorNames = [0, 1, 2]

        # Inside generate, create two nested for loops.
        # The outer loop should iterate over the names of the three sensor neurons.
        # The inner loop should iterate over each of the two motor neurons.

        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

        # print(self.weights.shape)
        for currentRow in range(3):
            # print('row', currentRow)
            for currentColumn in range(2):
                # print('col', currentColumn)
                # print(self.weights[currentRow, currentColumn])
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+3, weight=self.weights[currentRow, currentColumn])

        pyrosim.End()
        # time.sleep(0.01)

    def Mutate(self):
        randomRow = random.randint(0,2)
        randomCol = random.randint(0,1)
        self.weights[randomRow, randomCol] = random.random() * 2 + 1
