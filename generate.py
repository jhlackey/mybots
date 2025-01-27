import pyrosim.pyrosim as pyrosim

# constants
length = 1
width = 1
height = 1

x = 0  
y = 0
z = .5

#  tell pyrosim the name of the file where information about the world you're about to create should be stored. 
pyrosim.Start_SDF("boxes.sdf")

# stores a box with initial position x=0, y=0, z=0.5, and length, width and height all equal to 1 meter, in box.sdf.

# pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])

for x in range(5):
    length = 1
    width = 1
    height = 1
    for y in range(5):
        length = 1
        width = 1
        height = 1
        for i in range(10):
            # i *= .5
            length = length * 0.9
            width = width * 0.9
            height = height * 0.9
            pyrosim.Send_Cube(name="Box", pos=[x,y,z + (i * .9) ] , size=[length,width,height])


pyrosim.End()