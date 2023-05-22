#String representation of class objects
#Object printing concept
class Test:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __repr__(self):
        return "x:%s y:%s" % (self.x,self.y)

    def __str__(self):
        return "value of x is %s and value of y is %s" % (self.x,self.y)

t = Test(10,20)
print(t)






