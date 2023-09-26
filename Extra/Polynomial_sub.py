#Oppgave 7.25

class Polynomial:
    def __init__(self, coefficients):
        self.coeff = coefficients
    def __call__(self, x):
        s = 0
        for i in range(len(self.coeff)):
            s = s + self.coeff[i] * x**i
        return s

    def __add__(self, other):

        if len(self.coeff) > len(other.coeff):
            result_coeff = self.coeff[:]
            for i in range(len(other.coeff)):
                result_coeff[i] += other.coeff[i]
        else:
            result_coeff = other.coeff[:]
            for i in range(len(self.coeff)):
                result_coeff[i] += self.coeff[i]
        return Polynomial(result_coeff)

    def __sub__(self,other):

        if len(self.coeff) > len(other.coeff):
            result_coeff = self.coeff[:]
            for i in range(len(other.coeff)):
                result_coeff[i] -= other.coeff[i]
        else:
            result_coeff = [0]*len(other.coeff)
            for i in range(len(self.coeff)):
                result_coeff[i] = self.coeff[i]
            for i in range(len(other.coeff)):
                result_coeff[i] -= self.coeff[i]
        return Polynomial(result_coeff)



p1 = Polynomial([1,1,1,1])
p2 = Polynomial([0,1,2])

print(p1(0.5))
print(p2(0.5))

p3 = p1+p2

print(p3(1.0))

p4 = p1-p2

print(p4(1.0))
