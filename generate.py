import pyrosim.pyrosim as pyrosim

# constants
length = 1
width = 2
height = 3

x = 0  
y = 0
z = 1.5

#  tell pyrosim the name of the file where information about the world you're about to create should be stored. 
pyrosim.Start_SDF("box.sdf")

# stores a box with initial position x=0, y=0, z=0.5, and length, width and height all equal to 1 meter, in box.sdf.
pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])

pyrosim.End()