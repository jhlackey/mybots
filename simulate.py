import pybullet as p
import pybullet_data
import time

SLEEP_CONSTANT = 1/60

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
# p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

p.setGravity(0,0,-9.8) #responsible for determining what forces exist in our world. The first, most obvious one to add is gravity. 
planeId = p.loadURDF("plane.urdf") # add floor
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf") #tells pybullet to read in the world described in box.sdf.
for i in range(1000):
    print(i)
    p.stepSimulation()
    time.sleep(SLEEP_CONSTANT)
    
p.disconnect()