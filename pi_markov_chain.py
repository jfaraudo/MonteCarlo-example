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
print('Number of failed jumps (removed):',outside,' (',100*outside/inside_square,'%)')
print('\nResult')
print('\nNumber of points inside square of area 4:', inside_square)
print('Number of points inside unit circle:',inside_circle,)
print('Ratio unit circle/full square=',circle_ratio*100,'%')
print('\nEstimated Area of unit circle =',circle_ratio,'x Total Area =', pi_approx)
print(' Exact value (pi):', np.pi)
          
#Plot 

#create plot with the data and title
plt.plot(xc,yc,'ro',markersize=2.0)
plt.plot(xs,ys,'bo',markersize=2.0)
plt.title('MC estimate of Pi')

#Create axis with equal aspect ratio in both axis
ax = plt.gca()
ax.set_aspect('equal', 'box')

#Set axis limits
ax.set_xlim((-1, 1))
ax.set_ylim((-1, 1))

#Add a circle
circle_plot = plt.Circle( ( 0, 0 ), 1, color='green', linewidth=1.0, fill=False)
ax.add_artist(circle_plot)

#add black lines to show the different quadrants
plt.axhline(0, color='black')
plt.axvline(0, color='black')
#Show plot in screen
plt.show()
