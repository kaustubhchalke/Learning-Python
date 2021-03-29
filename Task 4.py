
#1. Write a program to reverse a string.
#Sample input: “1234abcd”
#Expected output: “dcba4321”


text = "1234abcd" [::-1]
print(text)



#2. Write a function that accepts a string and prints the number of uppercase letters and lowercase
#letters.
#Sample input: “abcSdefPghijQkl”
#Expected Output: No. of Uppercase characters : 3 No. of Lower case Characters : 12


def count(string):
    lowercase_count = 0
    uppercase_count = 0

    for letter in string:
        if letter.isupper():
            uppercase_count += 1
        elif letter.islower():
            lowercase_count += 1
    print("Upper",uppercase_count,"lower",lowercase_count)
#    print("No. of Uppercase characters :{} ", "No. of Lower case Characters :{} " .format(uppercase_count, lowercase_count)


count("abcSdefPghijQkl")



#3. Create a function that takes a list and returns a new list with unique elements of the first list.


def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,4,'s','g',62,5,2,'d','g',11,1,3,2,5])) 



#4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words
#in a hyphen-separated sequence after sorting them alphabetically.


items=[n for n in input().split("-")]
items.sort()
print("-".join(items))



#5. Write a program that accepts a sequence of lines as input and prints the lines after making all
#characters in the sentence capitalized.
#Sample input: Hello world Practice makes man perfect
#Expected output: HELLO WORLD PRACTICE MAKES MAN PERFECT


lines = []
while True:
    l = input()
    if l:
        lines.append(l.upper())
    else:
        break;

for l in lines:
    print(l)
    
    
    
#6. Define a function that can receive two integral numbers in string form and compute their sum and
#print it in the console.
    


def res (a,b):
	s = int(a) + int(b)
	return s 
num1 = "10"
num2 = "20"
sum = res(num1, num2)
print("Result = ", sum)




#7. Define a function that can accept two strings as input and print the string with the maximum length
#in the console. If two strings have the same length, then the function should print both the strings line
#by line.


def length(str1, str2):
	if (len(str1)==len(str2)):
		print(str1)
		
		print(str2)

	elif (len(str1)<len(str2)):
		print(str2)
	
	else:
		print(str1)

string1 = input(str("enter First String: "))
string2 = input(str("enter Second String: "))

print("\n")

length(string1, string2)



#8. Define a function which can generate and print a tuple where the values are square of numbers
#between 1 and 20 (both 1 and 20 included).



def printValues():
	l=list()
	for i in range(1,21):
		l.append(i**2)
	print(tuple(l))
printValues()



#9. Write a function called showNumbers that takes a parameter called limit. It should print all the
#numbers between 0 and limit with a label to identify the even and odd numbers.
#Sample input: show Numbers(3) (where limit=3)
#Expected output:
#0 EVEN
#1 ODD
#2 EVEN
#3 ODD





#10. Write a program which uses filter() to make a list whose elements are even numbers between 1
#and 20 (both included)


l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
even=filter(lambda x: x%2==0,l)
print(even)



#11. Write a program which uses map() and filter() to make a list whose elements are squares of even
#numbers in [1,2,3,4,5,6,7,8,9,10].
#Hints: Use filter() to filter even elements of the given listUse map() to generate a list of squares of the
#numbers in the filtered list. Use lambda() to define anonymous functions.


l=[1,2,3,4,5,6,7,8,9,10] 
even= map(lambda x: x**2, filter(lambda x: x%2==0, l)) 
print(even)
 


#12. Write a function to compute 5/0 and use try/except to catch the exceptions


def divide():
    return 5/0

try:
    divide()
except ZeroDivisionError as ze:
    print("Divison by zero")
    
    
#13. Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().
    
    




