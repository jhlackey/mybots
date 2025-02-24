from world import WORLD
from robot import ROBOT
import pybullet as p
import constants as c
import numpy
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import random

class SIMULATION:
    def __init__(self):

        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
        p.setGravity(0, 0, -9.8)  # responsible for determining what forces exist in our world. The first, most obvious one to add is gravity.

        self.robot = ROBOT() # load body urdf ... creates robot in body urdf file.
        self.world = WORLD() # load plane and world urdf .. i.e place block and checkered ground

    def Run(self):
        for i in range(1000):
         # print(i)
         p.stepSimulation()
         self.robot.Sense(i)
         time.sleep(c.SLEEP_CONSTANT)


def __del__(self):
   p.disconnect()
