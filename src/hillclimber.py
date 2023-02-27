import copy 

from solution import SOLUTION
from constants import numberOfGenerations

class HILL_CLIMBER():
    def __init__(self) -> None:
        self.parent = SOLUTION()
        self.child = None
    
    def Evolve(self):
        self.parent.Evaluate("GUI")
        for currentGeneration in range(numberOfGenerations):
            self.Evolve_For_One_Generation()
    
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Create_Brain()
        self.child.Evaluate("DIRECT")
        print('\n',self.parent.fitness, self.child.fitness)
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)


    def Mutate(self):
        self.child.Mutate()


    def Select(self):
        if self.child.fitness < self.parent.fitness:
            self.parent = self.child

    def Show_Best(self):
        self.parent.Evaluate("GUI")
