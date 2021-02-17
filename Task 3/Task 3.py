

#1. Create a list of 10 elements of four different data types like int, string, complex and float.

l1= [1,5.4,"list",2+4j,2,4,5,7,1,5]
print(l1)


#2. Create a list of size 5 and execute the slicing structure

l1=[1,2,3,4,5]
print(l1[1,4])


#3. Write a program to get the sum and multiply of all the items in a given list.

l1=[1,2,3,4,5]
print("Sum=",sum(l1))


#4. Find the largest and smallest number from a given list.

l1=[12,42,436,12,567,3]
print("Max=", max(l1))
print("Min=", min(l1))


#5. Create a new list which contains the specified numbers after removing the even numbers from a predefined list.

l1=[1,2,3,4,5,6,7,8,9]
l2=[i for i in l1 if i%2!=0]
print(l2)


#6. Create a list of elements such that it contains the squares of the first and last 5 elements between1 and30 (both included).




#7. Write a program to replace the last element in a list with another list.
#Sample input: [1,3,5,7,9,10], [2,4,6,8]
#Expected output: [1,3,5,7,9,2,4,6,8]

l1=[1,3,5,7,9,10]
l2=[2,4,6,8]
l1[-1:]=l23
print(l1)


#8. Create a new dictionary by concatenating the following two dictionaries:
#Sample input: a={1:10,2:20} b={3:30,4:40}
#Expected output: {1:10,2:20,3:30,4:40}

a={1:10,2:20}
b={3:30,4:40}
a.update(b)
print(a)


#9. Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1 and n(both 1 and n included).
#Sample input: n=5
#Expected output: {1:1, 2:4, 3:9, 4:16, 5:25}







#10. Write a program which accepts a sequence of comma-separated numbers from console and generates a list and a tuple which contains every number in the form of string.
#Sample input: 34,67,55,33,12,98
#Expected output: [‘34’,’67’,’55’,’33’,’12’,’98’] (‘34’,’67’,’55’,’33’,’12’,’98’)

values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)






