class calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"square is {self.n * self.n}")    
    def cube(self):
        print(f"cube is {self.n * self.n * self.n}")    
    def squareroot(self):
        print(f"squareroot is {self.n**(1/2)}")    

a = calculator(81)
a.square()
a.cube()
a.squareroot()