# from pybullet_envs.deep_mimic.env.testLaikago import jointName
import random

import pyrosim.pyrosim as pyrosim

# constants
length = 1
width = 1
height = 1

x = 0  
y = 0
z = .5

def Create_World():
    #  tell pyrosim the name of the file where information about the world you're about to create should be stored. 
    pyrosim.Start_SDF("world.sdf")
    # stores a box with initial position x=0, y=0, z=0.5, and length, width and height all equal to 1 meter, in box.sdf.
    pyrosim.Send_Cube(name="Box", pos=[x - 5,y + 5,z] , size=[length,width,height])

    pyrosim.End() 

# def Create_Robot():
#     pyrosim.Start_URDF("body.urdf")
#     pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5] , size=[length,width,height])
#     pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1,0,1.0])
#     pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5] , size=[length,width,height])
#     pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2,0,1.0])
#     pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5] , size=[length,width,height])
#     pyrosim.End()

def Generate_Body(): # step 5, renamed Create_Robot()
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5], size=[length, width, height])
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[1, 0, 1.0])
    pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[length, width, height])
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[2, 0, 1.0])
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[length, width, height])
    pyrosim.End()

def Generate_Brain(): # step 5, renamed Create_Robot()
    pyrosim.Start_NeuralNetwork("brain.nndf")
    motorNames = [3,4] # replace with indices
    sensorNames = [0,1,2]

    # Inside generate, create two nested for loops.
    # The outer loop should iterate over the names of the three sensor neurons.
    # The inner loop should iterate over each of the two motor neurons.

    pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
    pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
    pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
    pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
    pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

    for sensor in sensorNames:
        for motor in motorNames:
            pyrosim.Send_Synapse(sourceNeuronName=sensor, targetNeuronName=motor, weight=random.uniform(-1,1))

    # pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=3, weight=1.0)
    # pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=3, weight=1.0)
    # pyrosim.Send_Synapse(sourceNeuronName=0, targetNeuronName=5, weight=1.0)
    # pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=4, weight=1.0)
    # pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=4, weight=1.0)

    pyrosim.End()

def main():
    Create_World()
    Generate_Body()
    Generate_Brain()

if __name__ == "__main__":
    main()