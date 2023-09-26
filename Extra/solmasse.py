from math import pi
yr = (9.5*10**12)*1000
c = 3.0*10**8
au = 1.5*10**(-5)*(365*24*60*60*60)
au2 = au*c
g = 6.67*10**(-11)


masseSol = (((4*pi)**2)*((au2)**3))/(g*(yr)**2)
print(f"The mass of the sun is calculated to be around: masseSol = {masseSol: g}.")
