import math
import time
import solution
import constants
import copy
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system('rm brain*.nndf')
        os.system('rm fitness*.txt') # currently breaks program...
        self.parents = {}
        self.nextAvailableID = 0
        for val in range(constants.populationSize):
            self.parents[val] = solution.SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1


    def Evolve(self):
        # copying two for loops into evaluate
        self.Evaluate(self.parents)
        # exit()
        # for val in self.parents:
        #     self.parents[val].Start_Simulation('DIRECT')
        #
        # for val in self.parents:
        #     self.parents[val].Wait_For_Simulation_To_End('DIRECT')

        for currentGeneration in range(constants.numberOfGenerations):
            self.Evolve_For_One_Generation()
        #     # exit()

    def Show_Best(self):
        min_fitness = math.inf
        min_fitness_parent = None
        for parent in self.parents.keys():
            if self.parents[parent].fitness < min_fitness:
                min_fitness = self.parents[parent].fitness
                min_fitness_parent = self.parents[parent]

        time.sleep(0.01)
        min_fitness_parent.Start_Simulation('GUI')
        # self.parent.Evaluate('GUI')
        #Add a new method to HILL_CLIMBER, Show_Best(), which re-evaluates the parent with graphics turned on.

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Select()
        self.Print()
        # self.Show_Best()
        # exit()
        # self.child.Evaluate('DIRECT')

    def Spawn(self):
        self.children = {}
        for key in self.parents:
            self.children[key] = copy.deepcopy(self.parents[key])
            self.children[key].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1
        # self.child = copy.deepcopy(self.parent)
        # You will have to assign unique IDs to new child solutions, in PHC's Spawn() method, as well.
        # You can do so by adding a method, Set_ID(), to SOLUTION.
        # Make sure to increment self.nextAvailableID after you have set the newly-created child's ID.
        # self.child.setID(self.nextAvailableID)

    def Mutate(self):
        for child in self.children.values(): # iterate over valyes of children
            child.Mutate()

        # self.child.Mutate()

        # print('self.parent.weights:', self.parent.weights)
        # print('self.child.weights:', self.child.weights)
        # exit()

    def Select(self):
        for key in self.parents:
            if(self.parents[key].fitness > self.children[key].fitness):
                self.parents[key] = self.children[key]

        # if(self.parent.fitness > self.child.fitness):
        #     self.parent = self.child

    def Print(self):
        #Modify Print() to iterate through the keys in self.parents, and print the fitness of self.parents[key] and then the fitness of self.children[key] on the same line.
        for key in self.parents.keys():
            print('parent:', self.parents[key].fitness, 'child:', self.children[key].fitness)

    def Evaluate(self, solutions):
        for val in solutions:
            solutions[val].Start_Simulation('DIRECT')

        for val in solutions:
            solutions[val].Wait_For_Simulation_To_End('DIRECT')

