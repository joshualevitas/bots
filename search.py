

from parallelHillclimber import PARALLEL_HILL_CLIMBER

from solution import SOLUTION
from random_solution import RANDOM_SOLUTION

def evolve():
    phc = PARALLEL_HILL_CLIMBER()
    phc.Evolve()
    phc.Show_Best()

def random():
    r = SOLUTION(0)
    r.Evaluate("GUI")


def random_evolution():
    r = RANDOM_SOLUTION(0)
    r.Evaluate("GUI")