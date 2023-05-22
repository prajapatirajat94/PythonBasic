
#1.non Parameterized function
def test():
    print("This is Test")

test()
print("---------------*****************-------------------")
#2. Parameterized function

def abc(a):
    print("value of parmter is "+a)

abc("a")

print("---------------*****************-------------------")
#3. Default/Optional  Parameter

def CountryName(name="India"):
    print(name)

CountryName()
CountryName("UK")
print("---------------*****************-------------------")
#we can pas list also in parameter

def getNames(list):
    for x in list:
        print(x)

names=["java","Python","Csharp","dotnet"]
getNames(names)

print("---------------*****************-------------------")
#Functions with returns

def sum(a,b):
    return a+b

print(sum(1,2))

def getCapitalName(CountryName):
    if CountryName=="India":
        print("New Delhi")
    elif CountryName=="USA":
        print("Washington")

getCapitalName("India")
getCapitalName("USA")

#Recursion in Python
# Recursion means function is calling it self call rescursion
def fact(num):
    if(num>1):
        num=num*fact(num-1)
    return num

print(fact(4))

def login(username,password):
    print("Login with %s and %s"%(username,password))
    print(f"login with {username} and {password}")
    print("login with {} and {}".format(username,password))

login("Rajat","Rajat123")
