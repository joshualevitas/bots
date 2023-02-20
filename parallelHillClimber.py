import copy 
import os 
import math 

from solution import SOLUTION
from constants import numberOfGenerations, populationSize

class PARALLEL_HILL_CLIMBER():
    def __init__(self) -> None:
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        self.parents = {}
        self.children = {}
        self.nextAvailableID = 0
        for i in range(populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID +=1
        self.child = None

    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(numberOfGenerations):
            self.Evolve_For_One_Generation()
            self.Print()
    
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        for child in self.children.items():
            child[1].Create_Brain()
        self.Evaluate(self.children)
        self.Select()

    def Spawn(self):
        for i in self.parents.keys():
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID +=1



    def Mutate(self):
        for child in self.children.items():
            child[1].Mutate()


    def Select(self):
        for i in range (populationSize):
            if self.children[i].fitness < self.parents[i].fitness:
                self.parents[i] = self.children[i]

    def Show_Best(self):
        min_parent =  None
        min_parent_fitness = math.inf
        for i in self.parents.items():
            if i[1].fitness < min_parent_fitness:
                min_parent = i[1]
                min_parent_fitness = min_parent.fitness

        print("Our best fitness value was: ", min_parent_fitness)
        min_parent.Create_Brain()
        min_parent.Start_Simulation("GUI")
        min_parent.Wait_For_Simulation_To_End()
        min_parent.Create_Brain()

    def Evaluate(self,solutions):
        for i in solutions.keys():
            solutions[i].Start_Simulation("DIRECT")
        for j in solutions.keys():
            solutions[j].Wait_For_Simulation_To_End()


    def Print(self):
        for i in self.parents.keys():
            print('\n',self.parents[i].fitness,self.children[i].fitness,'\n')
