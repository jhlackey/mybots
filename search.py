import os
import parallelHillClimber

for _ in range(1):
    #Add a statement that creates an instance of HILL_CLIMBER called hc.
    phc = parallelHillClimber.PARALLEL_HILL_CLIMBER()
    phc.Evolve()
    phc.Show_Best()
    # os.system("python3 generate.py") #Comment out the existing statements in search.py.
    # os.system("python3 simulate.py")
