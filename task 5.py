
#2
  
import sys

file=sys.argv[1]
#file=input("Enter file name : ")
try:  
    f = open(file, "r")
    print(f.read())
    f.close()
except:
    print("please enter a valid name")  
    
    


##33. Write a program to handle an error if the user entered a number more than four digits it should
#return “The length is too short/long !!! Please provide only four digits”

num=input("Enter 4 digit number :")
if len(num)!=4:
    raise Exception("The length is too short/long !!! Please provide only four digits")
print("You entered", num)
 

#
#Create a login page backend to ask users to enter the username and password. Make sure to
#ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it
#should not be more than 3 times.

my_user="Kaustubh"
my_pass="qwerty"
c=0
while c<3:
    try:
        username=input("enter username:")
        password=input("enter password:")
        if username == my_user and password==my_pass:
            print("login success")
            break
    
    except:
        print("Invalid credentials")
    c+=1
if c==3:
    raise Exception ("too many attempts")
        
        

#6. Read doc.txt file using Python File handling concept and return only the even length string from
#the file. Consider the content of doc.txt as given below:
#Hello I am a file
#Where you need to return the data string
#Which is of even length
#Make sure you return the content in The same link as it is present.
    

import sys
import os
print(os.getcwd())
file="doc.txt"
try: 
    f = open(file, "r")
    for line in f:
        if len(line%2==0):
            print(line)
    f.close()
        
except:
    print("file does not exist")  

    




