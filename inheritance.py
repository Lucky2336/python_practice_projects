class employ:

    company = "itc"
    name = "laky"
    def show(self):
        print(f"name {self.name} and salary {self.company}")

class coder:
    language = "python"
    def print_lan(self):
        print(f"here isthe language {self.language}")



class programmer(employ, coder):
    company = "itc infotech"
    def show(self):
        print(f"name {self.name} and salary {self.company}")
    def showlanguage(self):
        print(f"name {self.company} and language {self.language}")

a = employ()
b= programmer()
b.show()
b.showlanguage()
# print(a.company , b.company)