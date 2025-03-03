# -------------------------------------------------------------
# INTRODUCTION TO SIMULATION WITH PYTHON: Monte Carlo 
# March 2025
# Example program by Jordi Faraudo
# Markov Chain simulation for calculation of Pi
# Study of convergence as a function of iterations
# -------------------------------------------------------------
# The algorithm is an implementation of Algorithm 1.1 from the book by W Krauth "Statistical Mechanics Algorithms and Computations"
# This is a classical example of a direct sampling Monte Carlo calculation 

# Here we import the mathematical library and the plots library
import numpy as np
import matplotlib.pyplot as plt

#Create output file with data
f = open('MCpi.dat','w')
    
# initial and maximum number of random points
max_random_points = 100000
min_random_points = 100

#step for iteration
step = 100

#Loop over number of random points
total_random_points=min_random_points
while (total_random_points <= max_random_points):

    # Init counter of number of points inside unit circle and inside unit square
    inside_circle = 0
    inside_square = 0

    #Calculation

    while (inside_square<total_random_points):
    
        #generate a random point
        x = np.random.uniform(-1.0, 1.0)
        y = np.random.uniform(-1.0, 1.0)

        #Update number of points inside square
        inside_square = inside_square +1 
       
        #check whether it is inside circle (count and save for representation)
        if x**2 + y**2 <= 1.0:
           inside_circle = inside_circle +1
         
    # Statistics

    # Number of points inside circle as compared with total
    circle_ratio = inside_circle /  inside_square

    #Approximation to pi
    pi_approx = 4.0*circle_ratio 
    
    #save data to a file
    print(f'{total_random_points} {pi_approx}\n')
    f.write(f'{total_random_points} {pi_approx}\n')
    
    #update 
    total_random_points=total_random_points + step

          

