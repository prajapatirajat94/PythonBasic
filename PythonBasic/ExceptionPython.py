


ItemsInCart=0

#Item will be added to cart

if ItemsInCart != 2: # raise Exception("Pls add value more then 0") -> this how we raise exception
    pass

assert(ItemsInCart==0)

# try , catch -> in python we use except instead of catch
try:
    with open('File.txt','r') as reader:
        print(reader.read(5))
        reader.readline()
        reader.close()

except:
    print("There is some exception")

