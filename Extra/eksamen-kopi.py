infile = open('summer_rain.txt', 'r')
infile.readline()
rain = 0
months = [ ]
for line in infile: months.append(line.split()[0])
rain += float(line.split()[-1])
print('The total rainfall from %s to %s was %.2f' %(months[0],months[-1],rain))
