import pybullet as p
import constants as c
import numpy
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import random

## TYPO?? Call this method from simulate.Run(), just after the simulation has been stepped.


class SENSOR:
    def __init__(self,linkName):
        self.linkName = linkName
        self.values = numpy.zeros(1000)
        # print(self.values)

    def Get_Value(self, timestep):
        # Cut the other one and paste it into sensor.Get_Value()
        # # Modify the statement so that it stores the values in self.values and uses self.linkName to know which link to extract touch sensor values from.
        self.values[timestep] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

        # if sensor_value is None:
        #     print(
        #         f"Warning: No valid sensor value for link {self.linkName} at timestep {timestep}. Assigning default value 0.")
        #     sensor_value = 0  # Assign a default value (e.g., 0) in case of None

        # print(sensor_value, " : " , timestep)

        # self.values[timestep] = sensor_value

        if timestep == len(self.values) - 1:
            print(f"Final values for link {self.linkName}: {self.values}")

    def Save_Values(self, filepath, arr):
        outFile = open("data/" + self.linkName + "Data.npy", "wb")
        numpy.save(outFile, self.values)
        outFile.close()