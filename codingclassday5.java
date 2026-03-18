#function
def msg(): #called function
    print("hello world")
msg()

#function
def add(): #called function
    n1 = int(input("enter  val 1:"))
    n2 = int(input("enter  val 2:"))
    print("Add=", n1+n2)
add()
#learn types of python function

#how to return multiple value
def add(): #called function
  n1 = int(input("enter  val 1:"))
  n2 = int(input("enter  val 2:"))
  sum = n1+n2
  sub = n1-n2
  mul = n1*n2
  div = n1/n2
  return sum,sub,mul,div

result = add()
print(result)

#4 types of argument that can be passed in python are 1.positional argument 2.keyword argument 3.default argument 4.variablevariable no. of argument
#mainly these 4 but another is unknown argument
def personalInfo(fname, lname):
   print("first name", fname)
   print("last name", lname)
personalInfo("aditi","kumar")

#keyword argument
def personalInfo(fname, lname):
   print("first name", fname)
   print("last name", lname)
   fname = "aditi"
   lname = "kumar"
personalInfo("fname","lname")

#default argument
def cityname(city="nagpur"):
   print(city)
cityname("delhi")
cityname("mumbai")
#cityname() gives error if no argument is passes then we cane keep a default argument
cityname()

#variable length argument
def studentName(*name):# * for all and by default type i tuple
   print(name)
studentName("aditi","rahul","olly")

mylist = [5,2,9,7,5,6]
#search the element 7
#n = len(mylist)
#print(n)
def searchElement(target):
   for i in range(len(mylist)): #mylist = 6
        #print(mylist[i]) #i=0 , mylist[0]
        if target == mylist[i]:
            print("element found at index", i)
searchElement(7) #this element we have to search