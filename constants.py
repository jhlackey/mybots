import numpy

SLEEP_CONSTANT = 1/60
BackLeg_amplitude = numpy.pi / 2
BackLeg_frequency = 7 * numpy.pi / 100
BackLeg_phaseOffset = 5

FrontLeg_amplitude = numpy.pi / 4
FrontLeg_frequency = 12 * numpy.pi / 100
FrontLeg_phaseOffset = 10

backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)


BackLeg_targetAngles = numpy.sin(numpy.linspace(0, 2 * numpy.pi, 1000)) # create 1000 values in sin wave
FrontLeg_targetAngles = numpy.sin(numpy.linspace(0, 2 * numpy.pi, 1000)) # create 1000 values in sin wave