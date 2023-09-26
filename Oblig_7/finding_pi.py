import numpy as np

x = np.zeros(3) #empty array with three spaces
x[0] = 3.14 #first value of x
print(x[0])

k = 1 #fixed k-value
#for-loop calcuating the second and third term of x
for i in range(1, k+2):
    x[i] = x[i-1] - (np.sin(x[i-1]))/(np.cos(x[i-1]))
    #Differential equation xn = xn-1 -(f(xn-1)/f'(xn-1))
    #Where the derivative of sin(x) is cos(x)
    print(f"{x[i]}")

print(f"{np.pi:.13f}") #print with the numpy pi element with 13 decimals

"""
Output: python3  finding_pi.py
3.14
3.1415926549364075
3.141592653589793
3.1415926535898
"""
