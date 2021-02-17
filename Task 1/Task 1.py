

## 1.Create three variables in a single line and assign values to them in such a manner that each one of them belongs to a different data type.

a, b, c = int(20), float(3.14), str("demo")
print(a, b, c)


## 2. Create a variable of type complex and swap it with another variable of type integer.

x = complex(input("Enter a complex number : "))
y = int(input("Enter an integer : "))
print('The value of x is', x)
print('The value of y is', y)
# swapping the values
x,y = y,x 
print('The value of x after swapping is' ,x)
print('The value of y after swapping is' ,y)


## 3. Swap two numbers using a third variable and do the same task without using any third variable.
###Using 3 variables
x=int(input("Enter a value of x : "))
y=int(input("Enter a value of y : "))
temp=x
x=y
y=temp
print("After swap value of x : ",x)
print("After swap value of y : ",y)

###Using 2 variables
x=int(input("Enter a value of x : "))
y=int(input("Enter a value of y : "))
x,y=y,x
print("After swap value of x : ",x)
print("After swap value of y : ",y)


##5. Write a program to complete the task given below: Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in another variable called z. Add 30 to z and store the output in variable result and print result as the final output.
x=int(input("Enter a value of between 1-10 : "))
y=int(input("Enter a value of between 1-10 : "))
z=x+y
result=z+30
print("Result", result)


##6. Write a program to check the data type of the entered values.
x=eval(input("Enter data : "))
print("The data type of the input value is :", type(x))


#7. Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and UPPERCASE.
tempA="lowerCamel"
TempB="UpperCamel"
temp_c="snake_case"
TEMP="UPPERCASE"
print(tempA,TempB,temp_c,TEMP)


#8. If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’ again. Will it change the value? If Yes then Why?
x=int(2)
##After changing the data type
x=float(2.3)
print(type(x))


