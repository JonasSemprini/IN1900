def read_file(filename): #main function for extracting data from the text-file
    infile = open(filename, 'r')
    infile.readline() #skipping the first line
    moon = {} #empty dictionary
    for line in infile:
        words = line.split(';') #sorting the data into a list by splitting on the ";"
        for words2 in words:
            pair = words2.split('-') #Splitting the data once to again to separate the elements with their corresponding compositions
            key = pair[0].strip().upper() #stripping to remove whitespace and changing all names to upper case
            value = pair[1].strip().replace(",","") #stripping the values for whitespace and replacing the commas with blank stripped space
            moon[key] = float(value) #sorting the keys to their corresponding values
    infile.close()
    return moon

moon_a = read_file("atm_moon.txt")
key = "HELIUM 4" #testing if the program prints out the corresponding values to their keys
print(f"'{key}': {moon_a[key]}")

"""
Output: python3 atm_moon.py
'HELIUM 4': 40000.0

This is only a example. If the user wants to print out the whole dictionary that is also possible with this program
"""
