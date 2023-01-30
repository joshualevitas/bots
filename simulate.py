from simulation import SIMULATION
import sys

directOrGui = sys.argv[1]

x = SIMULATION(directOrGui)
x.Run()
x.get_fitness()
