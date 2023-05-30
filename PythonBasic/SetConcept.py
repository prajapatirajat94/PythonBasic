#List and tuples are order based while Set is not order based
#duplicate values are allowed in tuples,List but in Set its not allowed
#it performs diffrent mathemetical operation
# define Set with : {}

s1 = {"java",100,"tom",12.33}
print(s1)

#set() function:
s2 =set("python")
print(s2)
#with list
s3=set([10,20,30,40])
print(s3)
#with tuples
s4=set((10,20,30,40))
print(s4)

#while creating set object, you can store only different number,strings,tuples
#List And dictionary objects are not allowed
s5={(1,2),2,3}
print(s5)

#Set Operations :-
#1.Union : |     :- this will give combine 2 set collection
print("Union :->")
T1 ={1,2,3,4,5}
T2= {4,5,6,7,8}
T3=T1.union(T2) # or T1|T2

print(T3)

#Intersection: &   -> this will give common value from 2 sets
print("Intersection :->")
T4 ={1,2,3,4,5}
T5= {4,5,6,7,8}

print(T4&T5)
#or
T6=T4.intersection(T5)
print(T6)
if T6==set() :
    print("No common values")
else:
    print("is not null")

#Difference of Sets: - difference()
print("Difference :->")
T7 ={1,2,3,4,5}
T8= {4,5,6,7,8}
print(T7-T8)
print(T8.difference(T7))

#Symetric differenc: ^
# remove common elemets and combine
T9 ={1,2,3,4,5}
T10= {4,5,6,7,8}
print(T9^T8)

#Set In-Built methods:
#1.add()
print("Adding value :- add()")
p1={"java","Python","c++"}
p1.add("dotnet")
print(p1)
#2.upadte()
print("UPdating value :- update()")
p2={"java","Python","c++"}
p2.update(["c","VbScript"]) #this is not list [] that we are adding
print(p2)
p2.update(("Ruby","javaScript"))
print(p2)
#3 clear()
p2.clear()
print(p2) #this is empty set
#4 copy():
lang={"java","Python","ruby"}
lang2=lang.copy()
print("this is a copy of lang ",lang2)

#5 discard() : remove the element
lang.discard("ruby")
print(lang)

#6 remove(): if element is not present and you are trying to remove element then
# it will give error
print(lang2)

