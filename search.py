import os
import hillclimb

for _ in range(1):
    #Add a statement that creates an instance of HILL_CLIMBER called hc.
    hc = hillclimb.HILL_CLIMBER()
    hc.Evolve()
    hc.Show_Best()
    # os.system("python3 generate.py") #Comment out the existing statements in search.py.
    # os.system("python3 simulate.py")
