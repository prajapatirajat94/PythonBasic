#Multiple inheritance is allowed in pyhton
class Base1(object):
    def __init__(self):
        self.str1="Rajat"
        print("Base1")

class Base2(object):
    def __init__(self):
        self.str2="Prajapati"
        print("Base2")

class Child(Base1,Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)
        print("Child")

    def printstring(self):
        print(self.str1,self.str2)

c=Child()
c.printstring()


