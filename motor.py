from world import WORLD

import pybullet as p
import constants as c
import numpy
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import random

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        # self.Prepare_To_Act()

    # def Prepare_To_Act(self):
    #     self.motorValues = numpy.sin(numpy.linspace(0, 2 * numpy.pi, 1000))
    #     self.amplitude = c.BackLeg_amplitude
    #     self.frequency = c.BackLeg_frequency
    #     self.offset = c.BackLeg_phaseOffset
    #
    #     if self.jointName == b'Torso_BackLeg':
    #         # Back leg operates at the given frequency
    #         self.frequency = self.frequency / 2
    #
    #     for i in range(1000):
    #      self.motorValues[i] = self.amplitude * numpy.sin(self.frequency * i + self.offset)
    #
    #     self.motorValues = c.scale_to_range(self.motorValues,-numpy.pi/4, numpy.pi/4)
    #     print(self.motorValues)

    def Set_Value(self, robotId, desiredAngle):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotId,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = desiredAngle,
            maxForce = 500)

    # def Save_Values(self):