from solution import SOLUTION
import constants as c
import copy
import math
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        self.parents = {}
        self.children = {}
        self.nextAvailableID = 0

        for p in range(c.population_size):
            self.parents[p] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        

    def evolve(self):
        self.evaluate(self.parents)

        # for p in self.parents:
        #     self.parents[p].evaluate("GUI")
        
        # for currentGeneration in range(c.numberOfGenerations):
        #     self.Evolve_For_One_Generation()
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
            # self.Print()
    
    def Spawn(self):
        for k in self.parents.keys():
            self.children[k] = copy.deepcopy(self.parents[k])
            self.children[k].set_id(self.nextAvailableID)
            self.nextAvailableID += 1
      


    def Mutate(self):
        # self.child.mutate()
        for c in self.children.items():
            # print(child)
            c[1].mutate()
       

    def Select(self):
        for i in range (c.populationSize):
            if self.children[i].fitness > self.parents[i].fitness:
                self.parents[i] = self.children[i]


    def Evolve_For_One_Generation(self):
        self.Spawn()

        self.Mutate()

        # self.child.evaluate("DIRECT")
        for c in self.children.items():
            c[1].Create_Brain()
        
        self.evaluate(self.children)


        # print(str(self.child.fitness) + ", " + str(self.parent.fitness))

        # self.Select()

    def show_best(self):
        # self.parent.evaluate("GUI")
        min_parent =  None
        min_parent_fitness = math.inf
        for i in self.parents.items():
            if i[1].fitness < min_parent_fitness:
                min_parent = i[1]
                min_parent_fitness = min_parent.fitness
        min_parent.Create_Brain()
        min_parent.Start_Simulation("GUI")

    def evaluate(self, solutions):
        for i in solutions.keys():
            solutions[i].Start_Simulation("DIRECT")

        for j in solutions.keys():
            solutions[j].Wait_For_Simulation_To_End()