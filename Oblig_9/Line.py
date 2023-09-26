class Line():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    def value(self, x):
        a = (self.p2[1] - self.p1[1])/(self.p2[0] - self.p1[0])
        b = self.p1[1] - a*self.p1[0]
        return a*x + b
line = Line((0,-1), (2,4))
def test_line():
    x = 0.5
    excpected = 0.25
    computed = line.value(0.5)
    tol = 1e-10
    success = abs(expected - computed) < tol
    assert success 
print(line.value(0.5), line.value(0), line.value(1))
