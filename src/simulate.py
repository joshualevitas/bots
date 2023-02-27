import sys 
from simulation import SIMULATION

# directOrGUI = sys.argv[1]
# solutionID = sys.argv[2]
# dont_delete = sys.argv[3]

# simulation = SIMULATION(directOrGUI,int(solutionID))
# simulation.Run()
# simulation.Get_Fitness()

def simulate(directOrGUI, solutionID, links, joints, delete = True):
    simulation = SIMULATION(directOrGUI,int(solutionID),links,joints, delete=delete)
    if simulation == None: return 
    simulation.Run()
    simulation.Get_Fitness()