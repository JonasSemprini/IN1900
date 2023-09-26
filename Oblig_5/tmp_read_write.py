#a.)
"""
def extract_file(filename): #main function for extracting the values from tmp_formatted.txt
    infile = open(filename, 'r') #opening the text file
    infile.readline()
    values = []
    for line in infile:
        words = line.split() #splitting the values into two lists with separate values
        values += words
        values = list(map(float, values)) #converting the values inside the list to float
    infile.close()
    return values
print(extract_file('tmp_formatted.txt')) #printing the information from tmp_formatted.txt
"""
#b.)

import numpy as np

def extract_file(filename): #main function for extracting the values from Oxygen.txt
    infile = open(filename, 'r') #opening the text file
    infile.readline()
    values = []
    for line in infile:
        words = line.split() #splitting the values into two lists with separate values
        values += words
        values = list(map(float, values)) #converting the values inside the list to float
    infile.close()
    return values
values1 = (extract_file('temp_oct_1945.txt')) #extracting data from temp_oct1945...
values2 = (extract_file('temp_oct_2014.txt')) #extracting data from temp_oct2014...

max_val1 = np.max(values1) #max value for temp_oct1945
max_val2 = np.max(values2) #max value for temp_oct2014
min_val1 = np.min(values1) #min value for temp_oct1945
min_val2 = np.min(values2) #min value for temp_oct2014
mean_val1 = np.mean(values1) #mean value for temp_oct1945
mean_val2= np.mean(values2) #mean value for temp_oct2014

print(f"""Max value October 1945 {max_val1: g} celsius Max value October 2014 {max_val2: g} celsius

Min value October 1945 {min_val1: g} celsius Min value October 2014 {min_val2: g} celsius

Mean value October 1945 {mean_val1: g} celsius Mean value 2014 {mean_val2:g} celius
""")
#c.)

def write_formatting(filename, list1, list2): #main function for transfering values from oct 1945 and oct 2014 into a new text file
    with open(filename, 'w') as outfile: #opening a new textfile for writing
        for j,k in zip(list1, list2):
                outfile.write(f'{j:14.8f} {k:14.8f}''\n') #linebreak and spacing
write_formatting("temp_formatting.txt", values1, values2)

"""
Output tmp_read_write.py
a.)
[9.0, 12.3, 15.8, 13.4, 11.0, 16.2, 13.3,
12.9, 14.0, 14.1, 12.0, 17.3, 15.5, 15.4]

b.)
Max value October 1945  11.6 celsius Max value October 2014  13.6 celsius

Min value October 1945  2.1 celsius Min value October 2014  2.3 celsius

Mean value October 1945 celsius  6.50645 Mean value 2014 8.85484 celsius

c.)
Output in temp_formatting.txt
"""
