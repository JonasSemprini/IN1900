import numpy as np
import matplotlib.pyplot as plt
#a.)
"""
def graph1(point1, point2): #main function
    t_array = np.linspace(0, 1) #array with t-values from 0 to 1
    point_x = t_array*point1[0] + (1 - t_array)*point2[0] #point 1
    point_y = t_array*point1[1] + (1 - t_array)*point2[1] #point 2
    plt.plot(point_x, point_y)
    plt.show()

graph1((0,0), (3,0)) #plotting the horisontal line
graph1((0,3), (0,0)) #plotting the vertical line
"""
#b.)

def graph2(p): #main function
    t_array2 = np.linspace(0,1) #array with t-values from 0 to 1
    for i in range(0, len(p)):
        for n in range(0, len(p)): #double for-loop to connect the lines between every point
            x = t_array2*p[i][0] + (1 - t_array2)*p[n][0]
            y = t_array2*p[i][1] + (1 - t_array2)*p[n][1]
            plt.plot(x, y)
    plt.show()
L = [(0,0), (1,0), (1,3), (0,3)] #list with points
graph2(L)

"""
Output: python3 graph1.py

"""
