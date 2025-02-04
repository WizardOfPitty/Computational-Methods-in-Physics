import numpy as np
g = 9.81
h_0 = 1.2
v_0 = 5.4 #Get all the constants together

# User input time variable and it is forced as a float 
# so that it will play nice with the givens 
# 0.55 is a pretty cool first input
t= float(input("How many seconds has it been since launch:"))

# The equations relating givens and time to the desired outputs
h = h_0 + v_0 * t - (1/2)*g * t ** 2
v= v_0 - g * t

# Print those suckers
print("The ball is at height {:.2f}".format(h), "meters")
print("The ball is travelling at {:.2f}".format(v), "meters per second")
