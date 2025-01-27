import pybullet as p
import time

SLEEP_CONSTANT = 1/60

physicsClient = p.connect(p.GUI)
# p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

p.loadSDF("box.sdf") #tells pybullet to read in the world described in box.sdf.
for i in range(1000):
    print(i)
    p.stepSimulation()
    time.sleep(SLEEP_CONSTANT)
    
p.disconnect()