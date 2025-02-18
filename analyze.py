import numpy 
import matplotlib.pyplot as pyplot
import os

# backLegSensorValues = numpy.load('data/backLegSensorValues.npy')
# frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy')
targetAngles = numpy.load('data/targetAngles.npy')
pyplot.plot(targetAngles)

# pyplot.plot(backLegSensorValues, label='BackLeg', lw=3)
# pyplot.plot(frontLegSensorValues, label='FrontLeg',)

pyplot.ylabel('Value in Radians')
pyplot.xlabel('Steps')
pyplot.title('Motor Commands')
pyplot.legend()
pyplot.show()


pyplot.savefig(os.path.join('data', 'targetAngles.png'))
