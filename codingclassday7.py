#  import re 
#  var = 'gasgg54@#vscsd!s*'
#  count = 0
#  for i in var:
#  python dosent follow ascii so we have to type cast and convert it
#    #z = re.findall('[a-z],0-9',1)
#    z =ord(i)
#    # print(z)
#    #if z:
#    if z>97 and z<=122:
#          continue
#    elif z>=48 and z<=57:
#          continue
#    else:
#          count+=1
#  print(count)

# //output: 5

#  A=[1,2,3]
#  B=[2,3,4]
#  C=[3,4,5]
#  for i in A:
#     if i in B and i in C:
#      print(i)

# // output: 3

# list =[0,1,0,3,12]
# for i in list: #i=0:0 change with all index
#         list.remove(i)
#         list.append(i)
# print(list)

# output:[1, 3, 12, 0, 0]

# list =[7,3,9,2,8]
# list.sort()
# print(list)
# print(list[-2])

# outpit:[2, 3, 7, 8, 9]
# output:8

# N=int(input()) #5
# sum =0
# mylist=[] #[10,11,7,12,14]
# for i in range(N):
#   a = int(input('enter element value:'))
#   mylist.append(a)
# for j in range(len(mylist)): #j=1
#     if j+1 in range(len(mylist)):
#       sum+= abs(mylist[j]-mylist[j+1]) #11-7=4
# print(sum)

# #output:5
# # enter element value:1
# # enter element value:2
# # enter element value:3
# # enter element value:4
# # enter element value:5
# # 4


