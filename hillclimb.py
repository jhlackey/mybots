import solution
import constants
import copy

class HILL_CLIMBER:
    def __init__(self):
        self.parent = solution.SOLUTION()

    def Evolve(self):
        self.parent.Evaluate()
        for currentGeneration in range(constants.numberOfGenerations):
            self.Evolve_For_One_Generation()
            # exit()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate()
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


