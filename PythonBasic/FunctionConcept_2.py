def Login(username,password):
    print(username,password)

Login("Rajat","Rajat@123")
 # Or

Login(username="Rajat",password="Rajat@123")

#*Arguement
def getMarks(*Arg):
   for x in Arg:
    print(x)

getMarks(1,2,3,4,5)

#Keyword Args
#**args

def getStudentMarks(**Args):
    for key,value in Args.items():
        print("%s = %s"%(key,value))

getStudentMarks(naveen=10,Ravi=20,Rajat=30)