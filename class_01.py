class animal:
    pass

class pets(animal):
    pass

class dog(pets):

    @staticmethod
    def bark():
        print("bhaaoo bhaaooo")
    pass 

d = dog()

d.bark()
