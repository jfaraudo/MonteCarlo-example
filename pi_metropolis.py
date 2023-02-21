# -------------------------------------------------------
# INTRODUCTION TO PYTHON2 SESSION
# May 2018 
# Example 3 program by Jordi Faraudo
# MonteCarlo simulation for calculation of Pi
# -------------------------------------------------------
# 
# The algorithm is an implementation of Algorithm 1.1 from the book by W Krauth "Statistical Mechanics Algorithms and Computations"
# This is a classical example of a direct sampling Monte Carlo calculation 
# For other similar implementations see for example https://gist.github.com/louismullie/3769218.
# By Jordi Faraudo 2018

# Here we import the mathematical library and the plots library
import numpy as np
import matplotlib.pyplot as plt

# input total number of random points
total_random_points = int(input("\nEnter number of points for Monte Carlo estimate of Pi?\n>"))

# input total number of random points
delta = float(input("\nEnter size of jump (delta): \n>"))

# Init counter of number of points inside unit circle and inside unit square
inside_circle = 0
inside_square = 0

#---------------------------------------------------
#Calculation

#Create list to save x,y of points to be shown in the graph
xp = []
yp = []

#Initial position
x=1.0
y=1.0

while (inside_square<total_random_points):
    
    #generate a random jump
    del_x = np.random.uniform(-delta, delta)
    del_y = np.random.uniform(-delta, delta)
    
    #check new positions inside the square
    if abs(x + del_x) <= 1.0 and abs(y + del_y) <= 1.0:
        
        #Update number of points inside square and update the new starting position
        inside_square = inside_square +1 
        x = x + del_x
        y = y + del_y
        
        #save position in list for further representation
        xp.append(x)
        yp.append(y)
        
        #check whether it is inside circle
        if x**2 + y**2 <= 1.0: 
            inside_circle = inside_circle +1 

#---------------------------------------------------  

# Statistics

# Number of points inside circle as compared with total
circle_ratio = inside_circle /  inside_square

#Number of points inside circle as compared with those inside the total square with area 4.0
pi_approx = 4.0*circle_ratio 

# Print output
print('\n--------------')
print('\nStatistics')
print('\nNumber of points inside square of area 4:', inside_square,' (100%)')
print('Number of points inside unit circle:',inside_circle,' (',(circle_ratio*100.0),'%)')
print('\n Estimated Area of unit circle =',circle_ratio,'x Total Area =', pi_approx)
print('\n Exact value (pi):', np.pi)
          
#Plot 

# create empty x and y arrays for eventual scatter plot of generated random points
x_plot_array = np.empty(shape=(1,inside_square))
y_plot_array = np.empty(shape=(1,inside_square))

# plot output of random points and circle
random_points_plot = plt.scatter(xp, yp, color='blue', s=.1)
circle_plot = plt.Circle( ( 0, 0 ), 1, color='red', linewidth=2, fill=False)

#Create axis with equal aspect ratio in both axis
ax = plt.gca()
ax.set_aspect('equal', 'box')

#Clear axis (do we need this?)
ax.cla()

#Set axis limits
ax.set_xlim((-1, 1))
ax.set_ylim((-1, 1))

#Add the points and the circle to the plot
ax.add_artist(random_points_plot)
ax.add_artist(circle_plot)

plt.axhline(0, color='black')
plt.axvline(0, color='black')
#Show plot in screen
plt.show()
