class EMP:

    #hidden data memeber or Private member of EMP class
    __salary=1000
    __name="Rajat"

E1 = EMP()
#print(E1.__salary) -> this is not the right way to access hidden private variables

#access private variable using tricky syntax:
print(E1._EMP__salary) # objectname._Classname__private variable
print(E1._EMP__name)
