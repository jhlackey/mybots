import solution
import constants
import copy

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        self.parents = {}
        self.nextAvailableID = 0
        # print(constants.populationSize - 1)
        for val in range(constants.populationSize):
            self.parents[val] = solution.SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1


    def Evolve(self):
        for val in self.parents:
            self.parents[val].Start_Simulation('DIRECT')

        for val in self.parents:
            self.parents[val].Wait_For_Simulation_To_End('DIRECT')
            # print(self.parents[val].fitness)
        # self.parent.Evaluate('GUI')
        # for currentGeneration in range(constants.numberOfGenerations):
        #     self.Evolve_For_One_Generation()
        #     # exit()

    def Show_Best(self):
        pass
        # self.parent.Evaluate('GUI')
        #Add a new method to HILL_CLIMBER, Show_Best(), which re-evaluates the parent with graphics turned on.

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate('DIRECT')
        self.Select()
        self.Print()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)
        # You will have to assign unique IDs to new child solutions, in PHC's Spawn() method, as well.
        # You can do so by adding a method, Set_ID(), to SOLUTION.
        # Make sure to increment self.nextAvailableID after you have set the newly-created child's ID.
        self.child.setID(self.nextAvailableID)
        self.nextAvailableID += 1

    def Mutate(self):
        self.child.Mutate()
        # print('self.parent.weights:', self.parent.weights)
        # print('self.child.weights:', self.child.weights)
        # exit()

    def Select(self):

        if(self.parent.fitness > self.child.fitness):
            self.parent = self.child

    def Print(self):
        print('parent:', self.parent.fitness, 'child:', self.child.fitness)


