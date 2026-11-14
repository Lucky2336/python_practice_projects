from  random import randint

class train:

    def __init__(self, train_no):
        self.train_no = train_no
        
    def book(self,fro, to):
        
        print(f"train ticket booked from {fro} to {to}")
        

    def get_status(self):
        print(f"train   no {self.train_no} is running on time")


    def get_fare(self, fro, to):
         print(f"train ticket fare is {randint(2000, 200000)} \n ticket no {self.train_no} from {fro} to {to}")

t = train(1234345)
t.book("rampir","delhiṇ")
t.get_status()
t.get_fare("rampor", "delhi")