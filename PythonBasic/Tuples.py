#Tuples: is collection of elements of any python data type
#tuples vs List
#1.syntax: you have to store value in  tuples x = (a,b,c)
#2.tuples is immutable can not change value once its  but list is mutable

names=("Java","Python","DotNet","Csharp","Zebra")

marks=(100,20,30,400)

employeetype =("Rajar",50,"n",True,23.33)

#To delete tuple object
#del Objectname  example: del marks


print(employeetype)
print(employeetype[0])
print(employeetype[1])
#backward indexing
print(employeetype[-1])

#Concatination of tuples
t1 =(1,2,3)
t2 =(1,2,3)

print(t1+t2)

#Range slicing
t3=(1,2,3,4,5)
print(t3[1:3])

#in:
employeetype2 = ("Rajat",25,"male","married")

print("male" in employeetype2)

#not in
print(35 not in employeetype2)
lengh = len(employeetype2)
print(lengh)

#Max numbers
num = (1,2,3,4,5,6)
print(max(num))
#alhabatical order
print(max(names))