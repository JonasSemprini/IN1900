molarMasseO = 16
molarMasseC = 12
molarMasseH = 1
vekt = 3.243
molarMasseTotal = (molarMasseC*6)+(molarMasseH*12)+(molarMasseO*6)
avogadroN = 6.022*10**23
mol = vekt/molarMasseTotal
atom = avogadroN*(mol)
print(f"The amount of mol we get from {vekt} grams is: {mol: g} mol.")
print(f"The amount of atoms we get from {mol: .3f} mol is: {atom: g} atoms.")
