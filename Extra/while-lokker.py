n = 100
C = []
F = []
Ca = []

for i in range(0, n+1, 10):
    F1 = (9/5)*i + 32
    C2 = (F1-30)/2
    C.append(i)
    F.append(F1)

for C3, F2, C4 in zip(C, F, Ca):
    print(f"Celsius:{C3} Farenheit:{F2} Approx Celsius:{C4}")
