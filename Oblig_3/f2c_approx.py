n = 100 #number of outputs
C = [] #Celsius
F = [] #Farenheit
Ca = [] #Approx Celsius

for i in range(0, n+1, 10):
    F1 = (9/5)*i + 32
    C2 = (F1-30)/2
    C.append(i)
    Ca.append(C2)
    F.append(F1)

for C3, F2, C4 in zip(C, F, Ca):
    print(f"Celsius:{C3} Farenheit:{F2} Approx Celsius:{C4}")

"""
Output: python f2c_approx.py
Celsius:0 Farenheit:32.0 Approx Celsius:1.0
Celsius:10 Farenheit:50.0 Approx Celsius:10.0
Celsius:20 Farenheit:68.0 Approx Celsius:19.0
Celsius:30 Farenheit:86.0 Approx Celsius:28.0
Celsius:40 Farenheit:104.0 Approx Celsius:37.0
Celsius:50 Farenheit:122.0 Approx Celsius:46.0
Celsius:60 Farenheit:140.0 Approx Celsius:55.0
Celsius:70 Farenheit:158.0 Approx Celsius:64.0
Celsius:80 Farenheit:176.0 Approx Celsius:73.0
Celsius:90 Farenheit:194.0 Approx Celsius:82.0
Celsius:100 Farenheit:212.0 Approx Celsius:91.0
"""
