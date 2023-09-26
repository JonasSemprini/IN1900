import matplotlib.pyplot as plt

N = 1 #number of years
x1 = 100
p = 5 #growth percentage
#while-loop calculating the first and the n-1 term and plotting the results as red points
while N < 5:
    xn = x1 + (p/100)*x1
    plt.plot(N, xn, "ro")
    x1 = xn
    N = N + 1
plt.xlabel("Years")
plt.ylabel("Growth")
plt.savefig("growth.png")
plt.show()

"""
Output: python3  growth_years_efficient.py
Graph shown in the png picture (growth.png)
"""
