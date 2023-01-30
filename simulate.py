from simulation import SIMULATION
import sys

directOrGui = sys.argv[1]
solutionId = sys.argv[2]

x = SIMULATION(directOrGui, solutionId)
x.Run()
x.get_fitness()
