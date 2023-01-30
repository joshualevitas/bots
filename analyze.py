import numpy 
import matplotlib.pyplot as p 

backdata = numpy.load('data/backvalues.npy')
frontdata = numpy.load('data/frontvalues.npy')
targetAngles_back = numpy.load('data/targetvalues_back.npy')
targetAngles_front = numpy.load('data/targetvalues_front.npy')

# p.plot(backdata, label = 'BackLeg Data', linewidth = 3)
# p.plot(frontdata, label = 'FrontLeg Data', linewidth = 3)
p.plot(range(1000), numpy.sin(targetAngles_back), label = 'Target Back', linewidth = 3)
p.plot(range(1000), numpy.sin(targetAngles_front), label = 'Target Front', linewidth = 3)
p.legend()
p.show()