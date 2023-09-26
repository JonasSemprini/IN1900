"""
NB!

This is the program which we will use as a basis for our solution!!

def read_densities(filename):
    infile = open(filename, 'r')
    densities = {}
    for line in infile:
        words = line.split()
        density = float(words[-1])

        if len(words[:-1]) == 2:
            substance = words[0] + ' ' + words[1]
        else:
            substance = words[0]

        densities[substance] = density
    infile.close()
    return densities
"""
#a.)

def read_densities_a(filename): #main function for extracting the data
    infile = open(filename, 'r')
    densities = {} #empty dictionary
    spacing = " " #making a variable only for a spacing element
    for line in infile:
        words = line.split() #splitting the words from the numbers into a list
        substance = '' #declaring the substance output as blank in the beggining
        density = float(words[-1]) #making the density values, float numbers
        substance = spacing.join(words[:-1]) #using a substring method to create spacing between names with more than one word
        densities[substance] = density #organising the keys to their corresponding values

    infile.close()
    return densities

densities_a = read_densities_a('densities.txt')
#print(densities_a)

#b.)
def read_densities_b(filename): #main function for extracting the data
    infile = open(filename, 'r')
    densities = {} #empty dictionary
    for line in infile:
        words = line.split() #splitting the words from the numbers into a list
        density = float(words[-1])
        substance = line[:12].strip() #using a strip method to remove all whitespace within the dictionary
        densities[substance] = density #organising the keys to their corresponding values
    infile.close()
    return densities

densities_b = read_densities_b('densities.txt')

print(densities_b)

def test_densities_read(): #test-function to check that both the latter functions give the same outputs
        success = read_densities_a('densities.txt') == read_densities_b('densities.txt')
        assert success

test_densities_read()


"""
Output: python3 density.py

{'air': 0.0012, 'gasoline': 0.67, 'ice': 0.9, 'pure water': 1.0,
'seawater': 1.025, 'human body': 1.03, 'limestone': 2.6,
'granite': 2.7, 'iron': 7.8, 'silver': 10.5, 'mercury': 13.6,
'gold': 18.9, 'platinium': 21.4, 'Earth mean': 5.52,
'Earth core': 13.0, 'Moon': 3.3, 'Sun mean': 1.4,
'Sun core': 160.0, 'proton': 230000000000000.0}
"""
