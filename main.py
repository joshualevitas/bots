import os 
from hillclimber import HILL_CLIMBER
from parallelHillclimber import PARALLEL_HILL_CLIMBER


phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()
