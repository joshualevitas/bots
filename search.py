

from parallelHillclimber import PARALLEL_HILL_CLIMBER

from solution import SOLUTION


def evolve():
    phc = PARALLEL_HILL_CLIMBER()
    phc.Evolve()
    phc.Show_Best()

def random():
    r = SOLUTION(0)
    r.Evaluate("GUI")


def random_evolution():
    r = SOLUTION(0)
    r.Evaluate("GUI")