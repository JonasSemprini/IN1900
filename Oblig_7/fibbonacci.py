import numpy as np
n = 15 #number of terms
x = np.zeros(n+1, int) #empty array with n+1 zeros in int form

x[0] = 1 #first term
x[1] = 1 #second term

print(f" n:0 {x[0]}")
print(f" n:1 {x[1]}")

#for loop printing the remaining 13 terms
for i in range(2, n):
  x[i] = x[i-1] + x[i-2]
  print(f" n:{i} {x[i]}")

"""
Output: python fibonacci.py
 n:0 1
 n:1 1
 n:2 2
 n:3 3
 n:4 5
 n:5 8
 n:6 13
 n:7 21
 n:8 34
 n:9 55
 n:10 89
 n:11 144
 n:12 233
 n:13 377
 n:14 610
"""
