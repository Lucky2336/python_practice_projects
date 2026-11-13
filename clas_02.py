class employee:
    salary = 2000
    increment = 1.5

    @property
    def salary_after_increment(self):
        return (self.salary  * (self.increment/100 + 1))

    @salary_after_increment.setter
    def increment(self, value):
        self.increment = value/self.salary * 100



e = employee()
e.salary = 50000
print(e.salary_after_increment)
