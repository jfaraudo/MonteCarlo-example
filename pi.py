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
total_random_points = int(input("\n Number of random points for Monte Carlo estimate of Pi?\n>"))

# number of random points inside unit circle and total random points
inside_circle = 0

# create empty x and y arrays for eventual scatter plot of generated random points
x_plot_array = np.empty(shape=(1,total_random_points))
y_plot_array = np.empty(shape=(1,total_random_points))

# create random values (x,y) between -1 and 1
x = np.random.uniform(-1, 1, size = total_random_points)
y = np.random.uniform(-1, 1, size = total_random_points)
    
# Loop over points to locate them and count points inside unit circle
for i in range(0, total_random_points):
    x_2 = x[i]**2
    y_2 = y[i]**2
    # count if inside unit circle
    if (x_2 + y_2) <= 1.0:
        inside_circle = inside_circle + 1

# Number of points inside cercle as compared with total
cercle_area = inside_circle / total_random_points

#Number of random points expected inside a square of unit area
inside_unit_square = total_random_points / 4.0

#Number of points inside cercle as compared with those inside a square of unit area
pi_approx = inside_circle / inside_unit_square

# Print output
print('\n--------------')
print('\n Statistics')
print('\n Number of total points inside total square:',total_random_points)
print('\n Number of points inside unit square:',inside_unit_square,' percentage:',(inside_unit_square*100.0/total_random_points),'%')
print('\n Number of points inside unit circle:',inside_circle,' percentage:',(inside_circle*100.0/total_random_points),'%')
print('\n Ratio of points inside unit circle compared with unit square =',(inside_circle*100.0/total_random_points),'%/',(inside_unit_square*100.0/total_random_points),'% =',pi_approx)
print('\n\nApproximate value for pi:', pi_approx)
print('Exact value of pi:', np.pi)

# plot output of random points and circle
random_points_plot = plt.scatter(x, y, color='blue', s=.1)
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
