import pyrosim.pyrosim as pyrosim

# constants
length = 1
width = 1
height = 1

x = 0  
y = 0
z = .5

def Create_World():
    #  tell pyrosim the name of the file where information about the world you're about to create should be stored. 
    pyrosim.Start_SDF("world.sdf")
    # stores a box with initial position x=0, y=0, z=0.5, and length, width and height all equal to 1 meter, in box.sdf.
    pyrosim.Send_Cube(name="Box", pos=[x - 5,y + 5,z] , size=[length,width,height])

    pyrosim.End() 

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="BackLeg", pos=[x,y,z] , size=[length,width,height])
    pyrosim.Send_Cube(name="Torso", pos=[1,0,0.5] , size=[length,width,height])
    pyrosim.Send_Cube(name="FrontLeg", pos=[2,0,-1.5] , size=[length,width,height])
    pyrosim.Send_Joint(name = "BackLeg_Torso" , parent= "BackLeg" , child = "Torso" , type = "revolute", position = [0,0,1])
    pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0,0,1])
    pyrosim.End()

def main():
    Create_World()
    Create_Robot()

if __name__ == "__main__":
    main()