#
# INTRODUCTION TO PYTHON2 SESSION
# May 2018 
# Supporting example program by Jordi Faraudo
# This simply draws a unit circle inside a square 
#

# Here we import the mathematical library and the plots library
import numpy as np
import matplotlib.pyplot as plt

# Here we create a draw of a circle (not a math function)
circle_plot = plt.Circle( ( 0, 0 ), 1, color='red', linewidth=2, fill=False)

#Make a line in 

#Create axis with equal aspect ratio in both axis
ax = plt.gca()
ax.set_aspect('equal', 'box')

#Clear axis (do we need this?)
ax.cla()

#Set axis limits
ax.set_xlim((-1, 1))
ax.set_ylim((-1, 1))

#Add the circle draw to the axis
ax.add_artist(circle_plot)

#Show both axis in the plot
plt.axhline(0, color='black')
plt.axvline(0, color='black')

#Show plot in screen
plt.show()



