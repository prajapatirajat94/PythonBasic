
score=[10,20,30,40,50]

print(score)

print(score[:]) #shallow copy of list

print(score+[60,70,80])

number=[1,2,3,4,5]
print(number[2])
number[2]=90
print(number)
number.append(200)
print(number)

name=['a','b','c','d','e','f']
print(name)
name[2:5]=['C','D','E']
print(name)

#to make it empty
name[:]=[]
print(name)

a=['a','b','c']
n=[1,2,3]

x=[a,n]
print(x)

print(x[0][1])
print(x[1][1])
