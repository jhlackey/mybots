import solution
import constants
import copy

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        self.parents = {}
        # print(constants.populationSize - 1)
        for val in range(constants.populationSize):
            self.parents[val] = solution.SOLUTION()


    def Evolve(self):
        for val in self.parents:
            self.parents[val].Evaluate('GUI')

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


