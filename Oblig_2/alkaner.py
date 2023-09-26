Mh = 1.0079 #g/mol
Mc = 12.011 #g/molar
n = 2 #start value of carbon atoms

for n in range(2,10):
    m = 2*n+2 #number of hydrogen atoms per alkan
    McH = n*Mc + m*Mh #molar mass of the alkan
    print(f"M(C{n}H{m}): {McH: .3f} g/mol")

"""
Output: python alkaner.py
M(C2H6):  30.069 g/mol
M(C3H8):  44.096 g/mol
M(C4H10):  58.123 g/mol
M(C5H12):  72.150 g/mol
M(C6H14):  86.177 g/mol
M(C7H16):  100.203 g/mol
M(C8H18):  114.230 g/mol
M(C9H20):  128.257 g/mol

"""
