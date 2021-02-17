

#1. Write a program in Python to perform the following operation:
# - If a number is divisible by 3 it should print “Consultadd” as a string
# - If a number is divisible by 5 it should print “Python Training” as a string
# - If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a string.

num=int(input("enter a number : "))
if num%3==0:
    print("Consultadd")
if num%5==0:
    print("Python training")
if num%3==0 and num%5==0:
    print("Consultadd - Python Training")
    
    
#2. Write a program in Python to perform the following operator based task:
#    Ask user to choose the following option first:
#If User Enter 1 - Addition
#If User Enter 2 - Subtraction
#If User Enter 3 - Division
#If User Enter 4 - Multiplication
#If User Enter 5 - Average
#Ask user to enter two numbers and keep those numbers in variables num1 and num2 respectively for the first 4 options mentioned above.
#Ask the user to enter two more numbers as first and second for calculating the average as soon as the user chooses an option 5.
#At the end if the answer of any operation is Negative print a statement saying “NEGATIVE”
#NOTE: At a time a user can only perform one action.
    
val=int(input("Enter: 1-Addition, 2-Substraction, 3-Division, 4-Multiplication, 5-Average ="))
num1,num2=eval(input("Enter two numbers="))
if 0<val<5:
    op={
        1:"+",
        2:"-",
        3:"/",
        4:"*"
        }
    print("Result=", eval(str(num1)+op[val]+str(num2)))
elif val==5:
    first,second=eval(input("Enter two more numbers:"))
    res=(num1+num2+first+second)/4
    print("Result=", res)

  

#val=int(input("Enter: 1-Addition, 2-Substraction, 3-Division, 4-Multiplication, 5-Average ="))
#if val==1:
#    num1,num2=eval(input("Enter two number:"))
#    add=num1+num2
#    if add>=0:
#        print("Addition:",add)    
#    else:
#        print("Negative")
#if val==2:
#    num1,num2=eval(input("Enter two number:"))
#    sub=num1-num2
#    if sub>=0:
#        print("Substraction:",sub)
#    else: 
#        print("Negative")  
#if val==3:
#    num1,num2=eval(input("Enter two number:"))
#    div=num1/num2
#    if div>=0:    
#        print("Division:",div)
#    else:
#        print("Negative") 
#if val==4:
#    num1,num2=eval(input("Enter two number:"))
#    mul=num1*num2
#    if mul>=0:
#        print("Multiplication:",mul)
#    else:
#        print("Negative")   
#if val==5:
#    num1,num2,first,second=eval(input("Enter four number:"))
#    avg=(num1+num2+first+second)/4
#    if avg>=0:
#        print("Average:",avg)
#    else:
#        print("Negative")
    

#3. Write a program in Python to implement the given flowchart:

a,b,c=int(10),int(20),int(30)
avg=(a+b+c)/3
print("Avg=", avg)
if avg >a and avg>b and avg>c:
    print("avg is higher than a,b,c")
elif avg>a and avg>b:
    print("avg is higher than a,b,c")
elif avg>a and avg>c:
    print("avg is higher than a,c")
elif avg>b and avg>c:
    print("avg is higher than b,c")
elif avg>a:
    print("avg is just higher than a")
elif avg>b:
    print("avg is just higher than b")
elif avg>c:
    print("avg is just higher than c")
    

# 4. Write a program in Python to break and continue if the following cases occurs:


val=0
while val>=0:
    val=int(input())
    if val>=0:
        print("Keep going")
print("It's over")
    

# 5. Write a program in Python which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200.

for i in range(2000,3201):
    i%7==0 and i%5!=0
    print(i)
    
    
#7. Write a program that prints all the numbers from 0 to 6 except 3 and 6.

for i in range(0,7):
    if(i==3 or i==6):
        continue
    print(i)
    

#8. Write a program that accepts a string as an input from the user and calculate the number of digits and letters.
    
s=input("Enter a string=")
digits=letters = 0  
for i in s:
    if i.isdigit():
        digits=digits+1
    elif i.isalpha():
        letters=letters+1
print("Letters", letters,"Digits", digits)


# 9.Lucky number

## Write a program such that it asks users to “guess the lucky number”. If the correct number is guessed the program stops, otherwise it continues forever.
Num=int(input("Guess the number ="))
while Num!=11:
    print("Incorrect")
    Num=int(input("Guess the number ="))
    
    
   
#Modify the program so that it asks users whether they want to guess again each time. Use two variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want to continue guessing. The program stops if the user guesses the correct number or answers “no”. (
#The program continues as long as a user has not answered “no” and has not guessed the correct number)    

num = 0;
ans = "yes"
while num != 99 and ans != "no":
    num=int(input("Guess the number ="))
    if num != 99:
        print("Incorrect")
        ans=input("Do you want to continue?")



# 10 The program asks for five guesses (no matter whether the correct number was guessed or not). If the correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”. After the fifth guess it stops and prints “Game over!”.
        

counter=1
while counter<=5:
    num=int(input("Guess the number="))
    counter+=1
    if num==13:
        print("Good guess!")
    else:
        print("Try again!")
print("Game Over!")


# 11. In the previous question, insert break after the “Good guess!” print statement. break will terminate the while loop so that users do not have to continue guessing after they found the number. If the user does not guess the number at all, print “Sorry but that was not very successful”.

num=int(input("Guess the number="))
while num!=5:
    if num==5:
        break
    else:
        print("Sorry but that was not very successful.")
        break
    

