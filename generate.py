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
    # pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5], size=[length, width, height])
    # pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[1, 0, 1.0])
    # pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[length, width, height])
    # pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[2, 0, 1.0])
    # pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[length, width, height])

    # new?
    pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[length, width, height])
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[0, -0.5, 1.0],
                       jointAxis="1 0 0")
    pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0], size=[0.2, 1, 0.2])
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute",
                       position=[0, 0.5, 1.0], jointAxis="1 0 0")
    pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0], size=[0.2, 1, 0.2])
    pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute",
                       position=[-0.5, 0, 1.0], jointAxis="0 1 0")
    pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5, 0, 0], size=[1, 0.2, 0.2])
    pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute",
                       position=[0.5, 0, 1.0], jointAxis="0 1 0")
    pyrosim.Send_Cube(name="RightLeg", pos=[0.5, 0, 0], size=[1, 0.2, 0.2])

    pyrosim.End()

def Generate_Brain(): # step 5, renamed Create_Robot()
    pyrosim.Start_NeuralNetwork("brain.nndf")
    motorNames = [6,7,8,9,10] # replace with indices
    sensorNames = [0,1,2,3,4,5]

    # Inside generate, create two nested for loops.
    # The outer loop should iterate over the names of the three sensor neurons.
    # The inner loop should iterate over each of the two motor neurons.

    # pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
    # pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
    # pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
    # pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
    # pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

    pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
    pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
    pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
    pyrosim.Send_Sensor_Neuron(name=3, linkName="LeftLeg")
    pyrosim.Send_Sensor_Neuron(name=4, linkName="RightLeg")
    pyrosim.Send_Sensor_Neuron(name=5, linkName="FrontLowerLeg")
    pyrosim.Send_Motor_Neuron(name=6, jointName="Torso_BackLeg")
    pyrosim.Send_Motor_Neuron(name=7, jointName="Torso_FrontLeg")
    pyrosim.Send_Motor_Neuron(name=8, jointName="Torso_LeftLeg")
    pyrosim.Send_Motor_Neuron(name=9, jointName="Torso_RightLeg")
    pyrosim.Send_Motor_Neuron(name=10, jointName="FrontLeg_FrontLowerLeg")

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