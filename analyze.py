import numpy 
import matplotlib.pyplot as pyplot

backLegSensorValues = numpy.load('data/backLegSensorValues.npy')
pyplot.plot(backLegSensorValues)
pyplot.show()