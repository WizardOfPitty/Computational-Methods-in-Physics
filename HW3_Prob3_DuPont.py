
# Function that will create a face of radius r, with an expression determined by the mood kwarg, centered at x0,y0 and you can change its color
def smiles(r, mood, x0 = 0.0, y0 = 0.0,  col = "Blue"):
   
    theta = np.linspace(0, 2 *np.pi, 500, endpoint = True)
    theta_s = np.linspace(5/4 * np.pi, 7/4 * np.pi, 500, endpoint = True)
    theta_f = np.linspace(np.pi / 3, 2/3 *np.pi, 500, endpoint = True)
   
   
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    
    #Pack them them together and plot them as a part of the function
    plt.plot(x + x0, y + y0, color = col)

    ex1 =0.1 * r * np.cos(theta) + 0.25 * r
    ey1 =0.1 * r * np.sin(theta) + 0.25 * r
    
    
    
    plt.plot(ex1 + x0, ey1 + y0, color = col)

    ex2 =0.1 * r * np.cos(theta) - (0.25 * r)
    ey2 =0.1 * r * np.sin(theta) + 0.25 * r
    
    
    plt.plot(ex2 + x0, ey2 + y0, color = col)

    nosex = 0.1 * r * np.cos(theta)
    nosey = 0.1 * r * np.sin(theta) - (0.125 * r)
    
    
    plt.plot(nosex + x0, nosey + y0, color = col)

    if mood == "happy":
        hapx =  r * np.cos(theta_s)
        hapy = 2 * (r * np.sin(theta_s) + (0.6 * r))
        
        plt.plot(hapx + x0, hapy + y0, color = col)

    elif mood == "sad":
          sadx= r * np.cos(theta_f)
          sady = 2 * (r * np.sin(theta_f) - (1.2 * r))
         
          plt.plot(sadx + x0, sady + y0, color = col)

        
    return smiles   



import numpy as np
import matplotlib.pyplot as plt

#smiles(r, mood, x0, y0, color)
smiles(2, 'sad', 30, 7.25)
smiles(22, 'happy', x0 = 30, y0 =  10, col = "r")
plt.xlim(4,56)
plt.ylim(-15, 36)
plt.show()
