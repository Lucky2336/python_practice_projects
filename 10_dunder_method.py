


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __add__(self, other):
    return self.age + other.age

p1 = Person("Emil", 22)
p2 = Person("Tobias", 19)

print(p1 + p2)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __eq__(self, other):
    return self.name == other.name and self.age == other.age

p1 = Person("Linus", 30)
p2 = Person("Linus", 30)

print(p1 == p2)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __repr__(self):
    return f"Person('{self.name}', {self.age})"

p1 = Person("Tobias", 25)
print(p1)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
#   __str__ only returns string if anything else return it gives an error 
  def __str__(self):
    return f"{self.name} ({self.age})"

p1 = Person("Tobias", 25)
print(p1) 