import numpy as np
import matplotlib.pyplot as plt

def read_info(filename): #main function for extracting the data
    infile = open(filename, 'r')
    infile.readline() #skipping line 1
    infile.readline() #skipping line 2
    k = [] #list for k-values
    band1 = [] #band values 1
    band2 = [] #band values 2
    band3 = [] #band values 3

#for loop to add all the values from band.txt to the empty lists

    for line in infile:
        words = line.split()
        k.append(float(words[0]))
        band1.append(float(words[1]))
        band2.append(float(words[2]))
        band3.append(float(words[3]))

#plotting the band values along the y-axis with the corresponding k-values on the x-axis

    for i in range(len(k)):
        plt.plot(k[i], band1[i], "ro") #plotting the output as circles
        plt.plot(k[i], band2[i], "bo") #plotting the output as circles
        plt.plot(k[i], band3[i], "go") #plotting the output as circles
    plt.title("Band structure of solids")
    plt.xlabel("Wave number")
    plt.ylabel("Band structure")
    plt.axis([k[0], k[-1], 0, 100])
    return band1, band2, band3, k

k, band1, band2, band3 = read_info("bands.txt")
plt.savefig("band.png")
plt.show()

"""
Output: python3  band_structure.py
The output is shown in the png picture.
"""
