import os 
from solution import SOLUTION
# from hillclimber import HILL_CLIMBER
from parallelHillclimber import PARALLEL_HILL_CLIMBER


# phc = PARALLEL_HILL_CLIMBER()
# phc.Evolve()
# phc.Show_Best()
x = 5
for i in range(x):
    s = SOLUTION(0)
    s.Evaluate("GUI")
