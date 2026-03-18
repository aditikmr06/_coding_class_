#mylist = ["sanjana", "ashish", "komal", "77", "sandeep", "60.25"]
# print(mylist)
# print(type(mylist))
# print(mylist[0])
# print(mylist[-1])
# print(mylist[2:5])
# print(mylist[1:])
# print(mylist[:])
# print(mylist[::-1])
# print(mylist[1:4:2])

# mylist.append('harsh')
# mylist.append("laxman")
# print(mylist)

# mylist.insert(1,"sanket")
# print(mylist)

# mylist.remove("sandeep")
# print(mylist)

# newlist = mylist.copy()    #cloning
# print(mylist)
# print(newlist)

# mylist = [['prashant', 'jha'],['85.56'],[440022,"yyy"]]
# print("example of multidimensional list: ")
# print(mylist)
# print(mylist[0][0])
# print(mylist[0][1])
# print(mylist[1][0])
# print(mylist[2][0])
# print(mylist[2][1])

# list1 = ["prashant","jha"]
# print(list1*2)

# list2 = [50,25,50]
# print(list1+list2)
list1=["prashant" , "jha"]
print(list1*2)

list2 =[50,25.50]
print(list1+list2)


list2 =[50,25.50,'prashant']
#del list2[2]
print(list2)

list2 =[50,25.50,'prashant']
list2.clear()
print(list2)

name="prshant"
print(name)
myname=list(name) #type casting
print(myname)

sorting example
mylist=[44,22,77,0,9,88]
mylist.sort()
print(mylist)
#default sorting rder for no. is ascending order
#default soting order for string is alphabetical order
#we should know that list should contain homogenious data otherwise error occurs

sorting example
mylist=[44,22,77,0,9,88]
mylist.sort(reverse=True)
print(mylist)

math = 10
print(id(math))

phy = 50
math = 50
print(id(math))
print(id(phy))  #it is temperory memory

math=50
phy=50
eng=40
print(id(math))
print(id(phy))
print(id(eng))

#alising
mylist=[44,22,77,0,9,88]
newlist = mylist
print(id(mylist))
print(id(newlist))


#2 special operator membership = (in and not in) and identity 
name = 'prashant'
print('Z' in name)
print('Z' not in name)
#looping
for i in range(2,6):
    print(i)
    #1=0
for i in range(1,10,2): #2 is the increment like 1 3 5 7
    print(i)
    #1=2
for i in range(5,0,-2): #2 is the decrement like 5 3 1
    print(i)
    #1=2
for i in range(1,11): 
    print(i*2)

    #1=2
#print all tables
for i in range(1,11): 
    print(i*2,"  ", i*3,"  ",i*4,"  ", i*5,"  ",i*6,"  ", i*7,"   ",i*8,"  ",i*9)
    print("\n")
    print(i*2,"  ", i*3,"  ",i*4,"  ", i*5,"  ",i*6,"  ", i*7,"   ",i*8,"  ",i*9)
    #1=2

#conditional ststement
#simple if
no = int(input("enter any digit"))
if no>0:
  print('positive')
if no<0:
  print("negative")
if no == 0:
  print('zero')
# logical operator
# a and b when all cond are true it gives true
# a or b if all are false then only false

#accept days and check if weekend  or not
day = (input("enter any day"))
if day == "sat" or "sun" or "SAT" or "SUN":
  print('weekend')
else:
  print('normal day')


#write a prog to accept 3 ppr marks and calc total % and if percent is greater then equal to 60 then he she is eligible for placement
mark1 = int(input("enter marks in maths"))
mark2 = int(input("enter amarks in phy"))
mark3 = int(input("enter marks in eng"))
percent = ((mark1+mark2+mark3)/300)*100
print(percent)
if percent >= 75:
  print('eligible')
else:
  print('not eligible')

#write a program to accept 5  diff val in 5v  diff variable and check max value and print by using simple if statement
n1 = int(input("enter 1st no"))
n2 = int(input("enter 2nd no"))
n3= int(input("enter 3rd no"))
n4 = int(input("enter 4th no"))
n5 = int(input("enter 5th no"))
if n1>n2 and n1>n3  and n1>n4 and n1>n5:
  print("n1 is greatest")
if n2>n1 and n2>n3  and n2>n4 and n2>n5:
  print("n2 is greatest")
if n3>n1 and n3>n2  and n3>n4 and n3>n5:
  print("n3 is greatest")
if n4>n1 and n4>n3  and n4>n2 and n4>n5:
  print("n4 is greatest")
if n5>n1 and n5>n3  and n5>n2 and n5>n4:
  print("n5 is greatest")
