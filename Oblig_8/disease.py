import numpy as np
import matplotlib.pyplot as plt

a = 0.25 #the first ratio of people getting sick

N = 15 #number of weeks

b1 = 0.5 #people falling sick the coming terms (1)
b2 = 0.75 #people falling sick the coming terms (2)

x0 = 100 #number of sick people first week
x1 = 150 #number of sick people second week

#a.)
#main function for calculating the number of sick people as a difference equation
def disease_weeks(a, b, x0, x1, N):
    weeks = list(range(N+1)) #making a list with values from 0 to 15
    x = np.zeros(N+1) #empty array with a size of 15
    #for-loop simulating the difference equation
    for i in range(2, N+1):
        x[0] = x0 #first term
        x[1] = x1 #second term
        x[i] = a*x[i-1] + b*x[i-2] #the x[n] sequence
    return weeks, x

weeks, x = disease_weeks(a,b1,x0,x1,N)
weeks2, x2 = disease_weeks(a,b2,x0,x1,N)

print(disease_weeks(a,b1,x0,x1,N)) #printing the values for the difference equation with the b1 value
print(disease_weeks(a,b2,x0,x1,N)) #printing the values for the difference equation with the b2 value

plt.xlabel("Weeks")
plt.ylabel("Spreading of disease")
plt.plot(weeks, x, '-r')
plt.plot(weeks2, x2, '-b')
plt.savefig("disease.png")
plt.show()

#b.)
#Function to present the difference equation simplefied with a while loop
def disease_week_n(a, b, x0, x1, N):
    n = 2
    while n < N+1:
        xn = x1*a + x0*b #the difference equation
        x0 = x1 #the first and second term
        x1 = xn
        n += 1 #incremating n
    return xn
sick = disease_week_n(a, b1, x0, x1, N)
sick2 = disease_week_n(a, b2, x0, x1, N)

print(sick, sick2)

"""
Output: python3 disease.py
#a.)
The plot is show in the png disease.png
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
[100, 150, 87.5,  96.875, 67.96875,  65.4296875, 50.34179688,  45.30029297,
 36.49597168,  31.7741394 ,  26.19152069,  22.43494987,
 18.70449781,  15.89359939,  13.32564875,  11.27821188]

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
[100, 150, 112.5, 140.625, 119.53125, 135.3515625 , 123.48632812, 132.38525391,
125.71105957, 130.71670532, 126.96247101, 129.77814674,
127.66638994, 129.25020754, 128.06234434, 128.95324174]

#b.)
11.278211884200573 128.95324174314737
"""
