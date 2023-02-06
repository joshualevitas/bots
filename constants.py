import numpy 


num_steps = 1000 
max_force = 500 
sleep_time = 0

amplitude_front = numpy.pi/4 
frequency_front = 50
phaseOffset_front = 0 
targetAngles_front = numpy.linspace(0 , 2*numpy.pi, num = 1000)


amplitude_back = numpy.pi/4 
frequency_back = 50
phaseOffset_back = numpy.pi/8
targetAngles_back = numpy.linspace(0 , 2*numpy.pi, num = 1000)


numberOfGenerations = 10
populationSize = 10


numSensorNeurons = 8 #8 
numMotorNeurons = 7 # 7 

motorJointRange = 0.5