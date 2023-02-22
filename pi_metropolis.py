# -------------------------------------------------------------
# INTRODUCTION TO SIMULATION WITH PYTHON MC SESSION
# Feb 2023 
# Example program by Jordi Faraudo
# Markov chain - Monte Carlo simulation for calculation of Pi
# -------------------------------------------------------------
# 
# The algorithm is an implementation of Algorithm 1.2 from the book by W Krauth "Statistical Mechanics Algorithms and Computations"
#

# Here we import the mathematical library and the plots library
import numpy as np
import matplotlib.pyplot as plt

# input total number of random points
total_random_points = int(input("\nEnter number of points for Monte Carlo estimate of Pi?\n>"))

# input total number of random points
delta = float(input("\nEnter size of jump (example 0.3): \n>"))

# Init counter of number of points inside unit circle and inside unit square
inside_circle = 0
inside_square = 0
outside = 0

#Create list to save x,y of points inside circle to be shown in the graph
xc = []
yc = []

#Create list to save x,y of points inside square but outside circle to be shown in the graph
xs = []
ys = []

#---------------------------------------------------
#Calculation

#Initial position
x=1.0
y=1.0

while (inside_square<total_random_points):
    
    #generate a random jump
    del_x = np.random.uniform(-delta, delta)
    del_y = np.random.uniform(-delta, delta)
    
    #check new positions and if they are outside the square make zero jump
    if abs(x+del_x) > 1.0 or abs(y+del_y) > 1.0:
        outside = outside +1
        del_x = 0.0
        del_y = 0.0

    #Update number of points inside square and update the new starting position
    inside_square = inside_square +1 
    x = x + del_x
    y = y + del_y
       
    #check whether it is inside circle (count and save for representation)
    if x**2 + y**2 <= 1.0:
        inside_circle = inside_circle +1
        xc.append(x)
        yc.append(y)
    else:
        xs.append(x)
        ys.append(y)

#---------------------------------------------------  

# Statistics

# Number of points inside circle as compared with total
circle_ratio = inside_circle /  inside_square

#Number of points inside circle as compared with those inside the total square with area 4.0
pi_approx = 4.0*circle_ratio 

# Print output
print('\n--------------')
print('\nPerformance of calculation')
print('\nNumber of failed jumps (removed):',outside,' (',100*outside/inside_square,'%)')
print('\n\nResult')
print('\nNumber of points inside square of area 4:', inside_square)
print('Number of points inside unit circle:',inside_circle,)
print('Ratio unit circle/full square=',circle_ratio*100,'%)')
print('\n Estimated Area of unit circle =',circle_ratio,'x Total Area =', pi_approx)
print('\n Exact value (pi):', np.pi)
          
#Plot 

# create empty x and y arrays for eventual scatter plot of generated random points
x_plot_array = np.empty(shape=(1,inside_square))
y_plot_array = np.empty(shape=(1,inside_square))

# plot output of random points and circle
random_points_plot1 = plt.scatter(xc, yc, color='blue', s=.1)
random_points_plot2 = plt.scatter(xs, ys, color='red', s=.1)
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
ax.add_artist(random_points_plot1)
ax.add_artist(random_points_plot2)
ax.add_artist(circle_plot)

plt.axhline(0, color='black')
plt.axvline(0, color='black')
#Show plot in screen
plt.show()
