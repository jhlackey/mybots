import numpy

# CONSTANTS
SLEEP_CONSTANT = 1/60

BackLeg_amplitude = numpy.pi / 2
BackLeg_frequency = 7 * numpy.pi / 100
BackLeg_phaseOffset = 5

FrontLeg_amplitude = numpy.pi / 4
FrontLeg_frequency = 12 * numpy.pi / 100
FrontLeg_phaseOffset = 10

# planeId = p.loadURDF("plane.urdf") # add floor
# robotId = p.loadURDF("body.urdf")