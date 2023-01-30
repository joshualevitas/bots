from solution import SOLUTION
import constants as c
import copy

class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()

    def evolve(self):
        self.parent.evaluate("GUI")
        
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
    
    def Spawn(self):
        self.child = copy.deepcopy(self.parent)


    def Mutate(self):
        self.child.mutate()
       

    def Select(self):
        if self.child.fitness > self.parent.fitness:
            self.parent = self.child


    def Evolve_For_One_Generation(self):
        self.Spawn()

        self.Mutate()

        self.child.evaluate("DIRECT")

        print(str(self.child.fitness) + ", " + str(self.parent.fitness))

        self.Select()

    def show_best(self):
        self.parent.evaluate("GUI")
