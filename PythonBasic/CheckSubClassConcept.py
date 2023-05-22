class Base(object):
    pass

class Child(Base):
    pass

#Test code
print(issubclass(Child,Base))

b=Base()
c = Child()


#here is we are checking b is instance of Base class or child class
#base class can also be reffered by child class
print(isinstance(b,Base))
print(isinstance(b,Child))
print(isinstance(c,Base))