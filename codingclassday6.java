// #what will be the output of the following code snippet?

// fruit_list1 = ['apple','berry','cherry','papaya']
// fruit_list2 = fruit_list1 #both will have some address
// fruit_list3 = fruit_list1[:]
// fruit_list2[0] = 'guava'
// fruit_list3[1] = 'kiwi'

// sum = 0
// for ls in (fruit_list1, fruit_list2, fruit_list3):
//     if ls[0] == 'guava':
//       sum += 1
//     if ls[1] == 'kiwi':
//       sum += 20
// print(sum)

// //output: 22

// def f(i, values = []): #default list
//     values.append(i)
//     print(values)
//     #return values
// f(1) #calling function
// f(2)
// f(3)

// // output: [1]
// // [1, 2]
// // [1, 2, 3]

// def func(value, values):
//     var = 1
//     values[0] = 44
// t = 3
// v = [1,2,3]
// func(t, v)
// print(t, v[0])

// output: 3 44

// dict = {'c': 97, 'a':96, 'b': 98}
// #when variable not used in loop then _ can be put
// for _ in sorted(dict):
//     print(dict[_])

// 96
// 98
// 97

// fruit = {}
// def addone(index):
//     if index in fruit:
//         fruit[index] += 1
//     else:
//         fruit[index] = 1 #{'Apple':1,'banana':1,'apple':1}
// addone('Apple')
// addone('banana')
// addone('apple')
// print(len(fruit))

// output:3

// #product of array except self
// arr = [1,2,3,4]
// for i in range(len(arr)):
//   if i==0:
//     x=arr[1]*arr[2]*arr[3]
//   if i==1:
//     y=arr[0]*arr[2]*arr[3]
//   if i==2:
//     z=arr[1]*arr[0]*arr[3]
//   if i==3:
//     n=arr[1]*arr[2]*arr[0]
// print("[",x,y,z,n,"]")