
# Function that takes n, the order of the function, and an arbirtrary array of x values to be plotted over.
def j(n, x=0.0):
    # make dummy array
    jn = np.zeros_like(x)
    
    # Use this format I found on stack exchange to get around problems with applying booleans to arrays
    mask_x_z = (x == 0)
    mask_x_nz = np.logical_not(mask_x_z)
    
    if n == 0:
        # We only wanna change the 0 element of the output
        jn[mask_x_z] = 1
        # then the expression takes care of the rest of the domain
        jn[mask_x_nz] = np.sin(x[mask_x_nz]) / x[mask_x_nz]
    
    elif n == 1:
        
        jn[mask_x_z] = 0
        
        jn[mask_x_nz] = (np.sin(x[mask_x_nz]) / (x[mask_x_nz] ** 2)) - (np.cos(x[mask_x_nz]) / x[mask_x_nz])
    
    elif n == 2:

        jn[mask_x_z] = 0
        
        jn[mask_x_nz] = ((3 / (x[mask_x_nz] ** 2) - 1) * np.sin(x[mask_x_nz]) / x[mask_x_nz]) - (3 * np.cos(x[mask_x_nz]) / (x[mask_x_nz] ** 2))
    
    return jn

import numpy as np
import matplotlib.pyplot as plt

# Generate x values
x = np.linspace(0, 50, 1000) # make the x array to operate on
y = j(0, x)  #make the Y vals
d = j(1, x)
z= j(2,x)

# Plot the Bessel function
plt.plot(x, y, label='J_0(x)') #Separate plot call for each
plt.plot(x, d, label='J_1(x)')
plt.plot(x, z, label='J_2(x)')
plt.title('Bessel Functions of the Zeroeth to the Second Order')
plt.xlabel('x')
plt.ylabel('J_n(x)')
plt.legend()
plt.grid(True)
plt.show()