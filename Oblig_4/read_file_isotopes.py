
def oxy(filename): #main function for extracting the values from Oxygen.txt
    infile = open(filename, 'r') #opening the text file
    infile.readline()
    weights = [] #list for the values of the isotope weights
    abundance = [] #list for the natural abundance of the isotope
    for line in infile:
        words = line.split() #splitting the values into two lists with separate values
        weights.append(float(words[0]))
        abundance.append(float(words[1]))
    infile.close()
    return weights, abundance

abundance, weights = oxy('Oxygen.txt')

M = 0

for abundances, weight in zip(abundance, weights): #a for loop looping of over,
                                                    #the added values in Oxygen.txt
    M += (abundances*weight)                        #calculating the i`th sum

print(f"""The molar mass of oxygen is estimated to be {M: .4f} g/mol
with a precision of four decimals""")


"""
Output: python oxygen.py

The molar mass of oxygen is estimated to be  15.9994 g/mol
with a precision of four decimals

"""
