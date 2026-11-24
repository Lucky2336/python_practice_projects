class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
         print(f"Full name: {self.fname} {self.lname}"  )  


p1 = Person("pilluuu", "tailerr")

p1.printname()


# class person_son(person):
#     def __init__(self, fname, lname):
#        person.__init__(s)

# p2  = person_son("pilluuuu", "tailer ka beta")

# p2.printname()

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.fname, self.lname, "to the class of", self.graduationyear)


p2 = Student("pillu", "tailer", 203)

p2.welcome()