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

#thank you Austin P. For the help. I was struggling a bit with some aspects and he pointed me in the right direction.
