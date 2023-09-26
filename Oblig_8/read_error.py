import numpy as np
import matplotlib.pyplot as plt

with open('read.txt', 'r') as infile: #extracting the data from the text-file
    epsilon = np.zeros(5) #empty array with size five (epsilon values)
    exact = np.zeros(5) #empty array with size five (exact error)
    n = np.zeros(5) #empty array with size five (terms)
    for line in infile:
        words = line.split() #splitting into a list
        #if-statement so we only extract the correct values and not the other irrelevant ones
        #The stamenet will only work when a line in the text-document starts with the letter e
        if line[0] == "e":
            epsilon = eval(words[1]) #evaluating the epsilon values if they are string
            exact = eval(words[4]) #evaluating the exact_error values if they are string
            n = eval(words[6]) #evaluating the terms if they are string

        plt.semilogy(n, epsilon, 'ro') #plotting the epsilon-values as red dots with a logarithmic y-axis
        plt.semilogy(n, exact, 'bo') #plotting the exact_error-values as blue dots with a logarithmic y-axis
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("read_error.png")
plt.show()

"""
Output: python3 read_error.py
The output is shown in the png picture read_error.png
"""
