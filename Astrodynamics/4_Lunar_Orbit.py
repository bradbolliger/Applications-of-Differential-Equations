# PROBLEM 1
#
# Modify the orbit function below to model
# one revolution of the moon around the earth,
# assuming that the orbit is circular.
#
# Use the math.cos(angle) and math.sin(angle) 
# functions in order to accomplish this.

import math
from udacityplots import *

moon_distance = 384e6 # m

def orbit():
    num_steps = 50
    x = numpy.zeros([num_steps + 1, 2])
    
    for i in range(num_steps + 1):
        sin_x = math.sin(2 * math.pi * i/(num_steps))
        cos_x = math.cos(2 * math.pi * i/(num_steps))
        
        x[i, 0] = moon_distance * cos_x
        x[i, 1] = moon_distance * sin_x

    return x

x = orbit()

@show_plot
def plot_me():
    matplotlib.pyplot.axis('equal')
    matplotlib.pyplot.plot(x[:, 0], x[:, 1])
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Longitudinal position in m')
    axes.set_ylabel('Lateral position in m')
plot_me()
