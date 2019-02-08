#
# INTRODUCTION TO PYTHON2 SESSION
# May 2018 
# First example program by Jordi Faraudo
# 

# Here we import the mathematical library and the plots library
import numpy as np
import matplotlib.pyplot as plt

# Here we create a list of values for variable x from 0.0 to 2.0 each 0.01
x = np.arange(0.0, 2.0, 0.01)

# Calculate two new sets of values by appplying a function to x
y = np.exp(x)
z = np.exp(-x)

# Create a plot the sets y and z as a function of x
plt.plot(x, y, 'ro', x, z, 'bv')

#Show the plot in screen
plt.show()


