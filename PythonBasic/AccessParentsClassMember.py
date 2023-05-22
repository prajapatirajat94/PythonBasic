class Base(object):

    def __init__(self,x):
        self.x=x


class Child(Base):
    def __init__(self,x,y):
        Base.x= x #this is how we access parents class variable
        self.y=y

    def printWork(self):
        print(Base.x,self.y)

#Test Code

c= Child(10,20)
c.printWork()