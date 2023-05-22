class Car:
    wheels=4
    #To create class write class name:
    #To create constructor write def __init__
    #Constructor overloading is not posssible in python
    #function is start with def name ()


    def __init__(self):
        print("non Parameterize constructor")

    def __init__(self, color):
        self.color = color
        print("Its constructor")

    def SetPrice(self, price):
        self.price = price
        print("Test Price set to",self.price)

    def GetPrice(self):
        return self.price

#How to call function in python just as below Car is class and we are
#creating objec as below c = Car() and then call method with reference
c1 = Car("Red")
c1.SetPrice(20)
print(c1.GetPrice())
print(Car.wheels)





class EMP:

    def __init__(self,name):
        self.name=name
        print("ITS EMP Constructor")

    def EMPName(self):
        print("Name is ",self.name)

E =EMP("Rajat")
E.EMPName()