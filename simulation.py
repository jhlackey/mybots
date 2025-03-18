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
    def __init__(self, directOrGUI):
        self.directOrGUI = directOrGUI
        if directOrGUI == "DIRECT":
           self.physicsClient = p.connect(p.DIRECT) # step 73. In SIMULATION's constructor, change p.connect(p.GUI) to p.connect(p.DIRECT).
        else:
            self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
        p.setGravity(0, 0, -9.8)  # responsible for determining what forces exist in our world. The first, most obvious one to add is gravity.
        p.loadSDF("world.sdf")
        self.planeId = p.loadURDF("plane.urdf")
        self.robot = ROBOT(2,2) # load body urdf ... creates robot in body urdf file.
        self.world = WORLD() # load plane and world urdf i.e place block and checkered ground

    def Run(self):

        for i in range(1000):
         p.stepSimulation()
         self.robot.Sense(i)
         self.robot.Think()
         self.robot.Act(i)
         if self.directOrGUI == "GUI":
             time.sleep(c.SLEEP_CONSTANT)

        self.Get_Fitness()

    def Get_Fitness(self):
        self.robot.Get_Fitness()

def __del__(self):
   p.disconnect()
