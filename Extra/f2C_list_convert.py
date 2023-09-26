#Oppgave 4.4

infile = open("Fdeg.txt", "r")


for i in range(3):
  inline.readline()

Flist = []
Clist = []

for line in infile:
  words = line.split()
  F = float(words[-1])
  Flist.append(F)
  C = (F-32)*(5/9)
  Clist.append(C)

infile.close()
print(Flist)
print(Clist)


outfile = open("outfile.txt", "w")

for F, C in zip(Flist, Clist):
    outfile.write(f"{F:6.2f}{C:6.2f}\n")

outfile.close()
