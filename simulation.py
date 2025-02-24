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
        self.world = WORLD()
        self.robot = ROBOT()

        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

        p.setGravity(0,0,-9.8) #responsible for determining what forces exist in our world. The first, most obvious one to add is gravity.
        self.planeId = p.loadURDF("plane.urdf") # add floor
        self.robotId = p.loadURDF("body.urdf")
        p.loadSDF("world.sdf") #tells pybullet to read in the world described in box.sdf.

        pyrosim.Prepare_To_Simulate(self.robotId)