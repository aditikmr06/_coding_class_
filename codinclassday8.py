# #write a program to perform arithemetic operations using functional programming approach
# #Functions helps us to achieve mudularity approach
# import sys #to stop infinite loop there is a function in sys
# def addition(num1,num2):#called function
#   print("addition", num1+num2)
# def Subtraction(num1,num2):#called function
#   print("Substraction", num1-num2)
# def multiplication(num1,num2):#called function
#   print("multiplication", num1*num2)#pass skips the body you cannot keep it empty
# def division(num1,num2):#called function
#   print("division", num1/num2)
# while True:
#   print()
#   print("1. Addition")
#   print("2. Subtraction")
#   print("3. multiplication")
#   print("4. division")
#   print("5. exit")
#   choice = int(input("enter your choice from above options:"))
#   if choice == 5:
#     sys.exit()
#   val1 = int(input("enter first value:"))
#   val2 = int(input("enter second value:"))
#   if choice == 1:
#      addition(val1,val2)
#   elif choice == 2:
#      Subtraction(val1,val2)
#   elif choice == 3:
#      multiplication(val1,val2)
#   elif choice == 4:
#      division(val1,val2)
#   else :
#     print("invalid choice")



# output:1. Addition
# 2. Subtraction
# 3. multiplication
# 4. division
# 5. exit
# enter your choice from above options:1
# enter first value:1
# enter second value:2
# addition 3

# 1. Addition
# 2. Subtraction
# 3. multiplication
# 4. division
# 5. exit
# enter your choice from above options:2
# enter first value:4
# enter second value:3
# Substraction 1

# 1. Addition
# 2. Subtraction
# 3. multiplication
# 4. division
# 5. exit
# enter your choice from above options:3
# enter first value:2
# enter second value:4
# multiplication 8

# 1. Addition
# 2. Subtraction
# 3. multiplication
# 4. division
# 5. exit
# enter your choice from above options:4
# enter first value:2
# enter second value:3
# division 0.6666666666666666

# 1. Addition
# 2. Subtraction
# 3. multiplication
# 4. division
# 5. exit
# enter your choice from above options:6
# enter first value:2
# enter second value:3
# invalid choice

# 1. Addition
# 2. Subtraction
# 3. multiplication
# 4. division
# 5. exit
# enter your choice from above options:5
# An exception has occurred, use %tb to see the full traceback.

# SystemExit
# /usr/local/lib/python3.12/dist-packages/IPython/core/interactiveshell.py:3561: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.
#   warn("To exit: use 'exit', 'quit', or Ctrl-D.", stacklevel=1)


# #nested function
# def outerFunction():
#   print("this is my outer function")
#   def innerFunction():
#     print("inner function")
#   innerFunction()
# outerFunction() #first exe start from here

# output:this is my outer function
# inner function

# #write the program to count the words
# #input = prashant is good programmer you can count words or space
# #output=4
# name = "she is a good programmer"
# count =1
# for i in name: #i=0
#     if i==" ":
#         count +=1
#     else:
#       continue
# print("total word count is:",count)

# output:total word count is: 5

# init_tuple = ()
# print(init_tuple.__len__())

# output:0

# init_tuple_a = 'a', 'b'
# init_tuple_b = ('a', 'b')
# print(init_tuple_a == init_tuple_b)
# #in tuple circular bracekt is not important runs with or without
# #id() function for address so check here if it is comparing by address or value comparision

# output:True

# init_tuple_a = '1','2'
# init_tuple_b = ('3', '4')
# print(init_tuple_a + init_tuple_b)
# id(init_tuple_a)
# id(init_tuple_b)

# output:('1', '2', '3', '4')
# 139238960559808

# l = [1,2,3]
# init_tuple = ('Python',) * (l.__len__() - 1[::-1][0])
# print(init_tuple)

# output:python

# init_tuple = ('Python') * 3
# print(type(init_tuple))

# output:<class 'str'>

# init_tuple = (1,) * 3
# init_tuple[0] = 2
# print(init_tuple)
# #error is right answer

# output:
# TypeError: 'tuple' object does not support item assignment

# init_tuple = ((1,2),)*7
# print(len(init_tuple[3:8]))

# output:4

# #replacing a string with another string:
# #s.replace(oldstring,newstring)
# #inside s, every occurence of oldstring will be replaced with newstring
# s=""
# s1=s.replace("difficult","easy")
# print(s1)
# #all occurence will be replaced
# s="abababababababba"
# s1=s.replace("a","b")
# print(s1)

# output:bbbbbbbbbbbbbbbb

# #REMOVING SPACE
# city=input("enter your city name:")
# scity=city.strip()
# if scity=='Hyderabad':
#   print("hello hyderabadi")
# elif scity=='channai':
#   print("hello madrasi")
# elif scity=='bengalore':
#   print("hello kannadiga")
# else:
#   print("your entered city is invalid")

# output:enter your city name:Hyderabad
# hello hyderabadi

# #list comprehension
# s=[i*i for i in range(1,11)] #i=
# print(s)

# output:[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# val=[2**i for i in range(1,6)] #1= 1,2,3,4,5
# print(val)

# output:[2, 4, 8, 16, 32]

# s=[i*i for i in range(1,11)] #i=
# print(s)
# val2=[i for i in s if 1%2==0]
# print(val2)

# output:[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# []

# #dictionary comprehension
# squares={x:x*x for x in range(1,6)}
# print(squares)
# doubles={x:x*2 for x in range(1,6)}
# print(doubles)

# output:{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}