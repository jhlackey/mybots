import pybullet as p
import numpy
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import random

SLEEP_CONSTANT = 1/60

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

p.setGravity(0,0,-9.8) #responsible for determining what forces exist in our world. The first, most obvious one to add is gravity. 
planeId = p.loadURDF("plane.urdf") # add floor
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf") #tells pybullet to read in the world described in box.sdf.

pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(10000)
frontLegSensorValues = numpy.zeros(10000)
# exit()

for i in range(10000):
    print(i)
    p.stepSimulation()
#    
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Torso") # unsure if will work with frontleg

    pyrosim.Set_Motor_For_Joint(

    bodyIndex = robotId,

    jointName = b'Torso_BackLeg',

    controlMode = p.POSITION_CONTROL,

    targetPosition = -numpy.pi / 6 ,

    maxForce = 500)

    pyrosim.Set_Motor_For_Joint(

    bodyIndex = robotId,

    jointName = b'Torso_FrontLeg',

    controlMode = p.POSITION_CONTROL,

    targetPosition = numpy.pi / 6,

    maxForce = 500)

    time.sleep(SLEEP_CONSTANT)
    
numpy.save('data/backLegSensorValues.npy', backLegSensorValues)
numpy.save('data/frontLegSensorValues.npy', frontLegSensorValues)

p.disconnect()