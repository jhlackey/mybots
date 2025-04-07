import pybullet as p
import constants as c
import numpy
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import random

class WORLD:
    def __init__(self):
        self.planeId = p.loadURDF("plane.urdf") # add floor
        # p.loadSDF("box.sdf") #tells pybullet to read in the world described in box.sdf.
