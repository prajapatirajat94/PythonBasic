

name="Hello Rajat"

mod = name.split(" ")
print(mod[0])
print(mod[1])

SplitName="    Hello this is name with space     "

print(SplitName.strip());

ReplaceName=SplitName.replace("Hello","Rajat").strip()
print(ReplaceName)
print(type(ReplaceName))

city="scarborough"
age ="29"

#way to use value in String
print(f"My city is {city} and age is {age}")
print("My city is {} and age is {}".format(city,age))
print("My city is %s and age is %s"%(city,age))

