import pybullet as p
import constants as c
import numpy
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import random
from sensor import SENSOR
from motor import MOTOR

class ROBOT:
    def __init__(self):
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)  # robotid


        # testing to find num joints
        num_joints = p.getNumJoints(self.robotId)
        print(f"Number of joints in robot: {num_joints}")

        self.Prepare_To_Sense()
        self.motors = {}
        self.Prepare_To_Act()


    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            print(linkName)
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, timestep):
        for sensor in self.sensors.values():
            # print(type(sensor.values))
            # sensor.values[timestep] = sensor.Get_Value()
            sensor.values[timestep] = sensor.Get_Value(timestep)

    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            print(jointName)
            self.motors[jointName] = MOTOR(jointName)


    def Act(self, timestep):
        for motor in self.motors.values():
            motor.Set_Value(self.robotId, timestep)

    def Save_Values(self, filepath, arr):
        numpy.save(filepath, arr)

