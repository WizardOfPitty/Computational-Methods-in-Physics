

# Part 1: Sum of n dice throws function
def dice(n):
    #What do you do if they only roll one?
    if n < 2:
        y= np.random.randint(1,7)

        
    #And here is how I figured it would be best to handle 
    # anything else, but I feel like the for 
    # loop would get overwhelmed at high n
    else:
    
        x = np.zeros(n)
    
    
        for i in range(n):
    
            x[i]= np.random.randint(1,7)
    
        y = np.sum(x)
       
    return y



import numpy as np
import matplotlib.pyplot as plt

print(dice(2))


#Part 2: The histogram

#Make a storage space
store= np.zeros(10000)

#It seems to hold up well for these purposes
for i in range (10000):
   
   #Fill it with unique values
   y= dice(2)
   store[i]=y


plt.hist(store, 11, range = (2,12), rwidth = 0.97, color = "Blue")
plt.title("Sum of Two Dice")
plt.show()


#Part 3: The histogram of 3 Dice

#Same as before
x = np.zeros(10000)

for i in range (10000):

   y= dice(3)

   x[i]=y


plt.hist(x, 15, range = (3,18), rwidth = 0.97, color = "Blue")
plt.title("Sum of Three Dice")
plt.show()