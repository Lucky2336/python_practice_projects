class programmer_info:
    company = "microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

jarry = programmer_info("jarry", 12000, 4800) 

print(jarry.salary, jarry.company)
        