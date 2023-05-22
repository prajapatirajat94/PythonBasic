class Person(object):

    def __init__(self,name):
        self.name=name

    def getName(self):
        return self.name

    def isEmployee(self):
        return False

#To inherite parent class
# Employee(Parent class name)
class Employee(Person):
    def isEmployee(self):
        return True

#Test Person class
Per = Person("Rajat")
print(Per.name)
print(Per.name,Per.isEmployee())

emp1=Employee("Kajol")
print(emp1.name)
print(emp1.getName(),emp1.isEmployee())