from math import exp
B = 50000 # carrying capacity
k = 0.2 #growth constant
C = (B - 5000)/5000 #constant
n = 48 #number of calculations

T = [i for i in range(0, n+1)] #time
N1 = [(B/(1+C*exp(-k*t))) for t in T] #population
table1 = [T, N1] #nested list of both the time and population

for i1 in range(len(table1[1])):
    value1 = table1[0][i1]
    value2 = table1[1][i1]
    print(f"Tid:{value1: .1f} Populasjon:{value2: .1f}")

tn2 = [] #new list putting value1 and value2 into one common list
for i in range(0, n+1):
    tn3 = table1[0][i] + table1[1][i]
    tn2.append(tn3)

for i in range(0, n+1, 4):
    value3 = tn2[i]
    print(f"Tid: {i: .1f} Populasjon: {value3: .1f}")

"""
Ouput: population_table2.py
a.)
Tid: 0.0 Populasjon: 5000.0
Tid: 1.0 Populasjon: 5974.7
Tid: 2.0 Populasjon: 7109.5
Tid: 3.0 Populasjon: 8418.5
Tid: 4.0 Populasjon: 9912.8
Tid: 5.0 Populasjon: 11598.5
Tid: 6.0 Populasjon: 13474.4
Tid: 7.0 Populasjon: 15531.0
Tid: 8.0 Populasjon: 17748.9
Tid: 9.0 Populasjon: 20099.0
Tid: 10.0 Populasjon: 22542.7
Tid: 11.0 Populasjon: 25034.7
Tid: 12.0 Populasjon: 27526.0
Tid: 13.0 Populasjon: 29967.7
Tid: 14.0 Populasjon: 32314.6
Tid: 15.0 Populasjon: 34528.4
Tid: 16.0 Populasjon: 36580.2
Tid: 17.0 Populasjon: 38450.9
Tid: 18.0 Populasjon: 40131.2
Tid: 19.0 Populasjon: 41620.3
Tid: 20.0 Populasjon: 42924.3
Tid: 21.0 Populasjon: 44054.4
Tid: 22.0 Populasjon: 45024.9
Tid: 23.0 Populasjon: 45851.9
Tid: 24.0 Populasjon: 46552.0
Tid: 25.0 Populasjon: 47141.3
Tid: 26.0 Populasjon: 47635.0
Tid: 27.0 Populasjon: 48046.9
Tid: 28.0 Populasjon: 48389.6
Tid: 29.0 Populasjon: 48673.7
Tid: 30.0 Populasjon: 48908.9
Tid: 31.0 Populasjon: 49103.1
Tid: 32.0 Populasjon: 49263.3
Tid: 33.0 Populasjon: 49395.2
Tid: 34.0 Populasjon: 49503.8
Tid: 35.0 Populasjon: 49593.0
Tid: 36.0 Populasjon: 49666.3
Tid: 37.0 Populasjon: 49726.4
Tid: 38.0 Populasjon: 49775.8
Tid: 39.0 Populasjon: 49816.3
Tid: 40.0 Populasjon: 49849.5
Tid: 41.0 Populasjon: 49876.7
Tid: 42.0 Populasjon: 49899.0
Tid: 43.0 Populasjon: 49917.3
Tid: 44.0 Populasjon: 49932.3
Tid: 45.0 Populasjon: 49944.5
Tid: 46.0 Populasjon: 49954.6
Tid: 47.0 Populasjon: 49962.8
Tid: 48.0 Populasjon: 49969.5
b.)
Tid:  0.0 Populasjon:  5000.0
Tid:  4.0 Populasjon:  9916.8
Tid:  8.0 Populasjon:  17756.9
Tid:  12.0 Populasjon:  27538.0
Tid:  16.0 Populasjon:  36596.2
Tid:  20.0 Populasjon:  42944.3
Tid:  24.0 Populasjon:  46576.0
Tid:  28.0 Populasjon:  48417.6
Tid:  32.0 Populasjon:  49295.3
Tid:  36.0 Populasjon:  49702.3
Tid:  40.0 Populasjon:  49889.5
Tid:  44.0 Populasjon:  49976.3
Tid:  48.0 Populasjon:  50017.5

PS! I am noticing the round off errors because it adds 4 between every 4-level interval...
I tried to fix it but i could not find a solid solution
"""
