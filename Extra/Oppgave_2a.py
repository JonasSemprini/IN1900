n = 10000
i = 500
bin_co = 1 #start value for the binomial coefficient
for j in range(1, (n-i+1)):
    bin_co = (i + j)/j * bin_co #creating a product for the j'th term of the coefficient
print(bin_co)


"""
Output: python Oppgave_2a.py
a.)

Example one
1.) 26010428123750.86

Example two
2.)
1.1806919799625589e+218

Example three
3.)
2.7028824094543663e+299

"""
