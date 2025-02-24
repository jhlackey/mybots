import numpy 
import matplotlib.pyplot as pyplot
import os

# backLegSensorValues = numpy.load('data/backLegSensorValues.npy')
# frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy')
FrontLeg_targetAngles = numpy.load('data/FrontLeg_targetAngles.npy')
BackLeg_targetAngles = numpy.load('data/BackLeg_targetAngles.npy')
pyplot.plot(FrontLeg_targetAngles)
pyplot.plot(BackLeg_targetAngles)

# pyplot.plot(backLegSensorValues, label='BackLeg', lw=3)
# pyplot.plot(frontLegSensorValues, label='FrontLeg',)

pyplot.ylabel('Value in Radians')
pyplot.xlabel('Steps')
pyplot.title('Motor Commands')
pyplot.legend()
pyplot.show()


pyplot.savefig(os.path.join('data', 'targetAngles.png'))
