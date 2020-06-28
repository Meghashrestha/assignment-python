class vehical:
    category = 'car'
    def __init__(self,colour, wheel): #initializer
        self.colour= colour
        self.wheel= wheel
    def description(self):
        return f"this is to return that the clour is {self.colour}."
    def make_it_blue(self):
        self.colour="blue"
obj1 = vehical('red','4')
print(f"the colour of the car is {obj1.colour}")
print(f"the colour of the car is {obj1.category}")
print(f"category: {obj1.__class__.category}")
print(f"the colour of the car is {obj1.description()}")
print(f"Before : {obj1.colour}")
obj1.make_it_blue()
print(f"Aftr: {obj1.colour}")


class magicmethod:
    def __init__(self, milage):
        self.milage = milage

    def __str__(self):
        return f'a{self.milage}car'
mycar = magicmethod(12)
print(mycar)
class newcls:
    def __new__(cls):
        print("hello hi i am new")
        return super().__new__(cls)

    def __init__(self):
        print("hello")

newcls()
