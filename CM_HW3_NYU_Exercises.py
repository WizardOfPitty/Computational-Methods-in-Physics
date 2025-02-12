import numpy as np
import matplotlib.pyplot as plt

################# Exercise 1 #####################################
x = np.linspace(-1,3,10000)
y = 3 * (x ** 2)
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-1,3)
plt.show()
################# Exercise 3########################################
x_trig = np.linspace(-np.pi, np.pi, 10000) #create 10000 evenly spaced elements in an array to act as the angles
y_sin = np.sin(x_trig) #Now define the y values
y_cos = np.cos(x_trig)
plt.plot(x_trig, y_cos, label = "Cosine",  color = "green") #cosine in green
plt.plot(x_trig, y_sin, label = "Sine", color = "black") # sine in black
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-np.pi, np.pi)
plt.legend()
plt.show()
########################## Exercise 4 ###############################
dataPt, time, height, error = np.loadtxt("C:/Users/edupo/Documents/MCLA/The_ghost_of_MCLA_past/MCLA_Spring_2025/Computational_Methods_in_Physics/Programs/MyData.txt", skiprows = 5, unpack = True)
data_fit = (3 + 1/2 * np.sin((np.pi * time)/5)) * time * np.exp(-time/10)
info = 'Data for falling mass experiment'
plt.plot(time, data_fit , label = "y(t)", color = "Black", zorder = 1)
plt.scatter(time, height, label = "Data",color = "Green", zorder = 2, marker = "o", s = 13)
plt.xlabel("Time (s)")
plt.ylabel("Position (cm)")
plt.errorbar(time, height, yerr = error, fmt = 'none', ecolor = "Green", capsize = 2.5, capthick = 1.0)
plt.legend()
plt.show()
data = np.array(list(zip(dataPt, time, height, error)))
np.savetxt("MyDataOut.txt", data, header = info, fmt = "%12.1f") 
