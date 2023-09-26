#Oppgave 4.5
import sys

try:
    F = float(sys.argv[1])
except IndexError:
    print("You forgot the argument!")
    exit()
except ValueError:
    print("The argument must be a pure number")
    exit()
    
C = (F-32)*5.0/9
print(C)
