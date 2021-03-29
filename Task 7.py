

#1. Write a program that calculates and prints the value according to the given formula:
#Q= Square root of [(2*C*D)/H]
#Following are the fixed values of C and H:
#C is 50.
#H is 30.
#D is a variable whose values should be input to your program in a comma-separated sequence.

#import math
#C=50
#H=30
#D=eval(input(","))
#Q= [(2*C*D)/H]
#print(math.sqrt(Q))


import math

numbers = input("Provide D: ")
numbers = numbers.split(',')

result= []
C=50
H=30
for D in numbers:
    print(math.sqrt((2*C*int(D)/H)))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#Define a class named Shape and its subclass Square. The Square class has an init function which
#takes length as argument. Both classes have an area function which can print the area of the shape
#where Shape’s area is 0 by default.


class Shape:
    def area(self):
        self.Area=0
        print(self.Area)
    
class Square(Shape):
    def __init__(self,length):
        self.length=length
    def area(self):
        self.Area=self.length*self.length
        print(self.Area)
        
s=Shape()    
sq=Square(5)  
  
s.area()
sq.area()


#Create a class to find three elements that sum to zero from a set of n real numbers
#Input array: [-25,-10,-7,-3,2,4,8,10]
#Expected output: [[-10,2,8],[-7,-3,10]]

x=[-25,-10,-7,-3,2,4,8,10]
res=[]
for i in range(0,len(x)):
    for j in range(i+1,len(x)):
        for k in range(j+1,len(x)):
            if x[i]+x[j]+x[k]==0:
                res.append([x[i],x[j],x[k]])
print(res)
            


        

#Create a Time class and initialize it with hours and minutes.
#Create a method addTime which should take two Time objects and add them.
#E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
#Create another method displayTime which should print the time.
#Also create a method displayMinute which should display the total minutes in the Time.
#E.g.- (1 hr 2 min) should display 62 minute.
#

class Time:
    def __init__(self,hours,minutes):
        self.hours=hours
        self.minutes=minutes
    def addTime(self,t1):
        minutes=self.hours*60+self.minutes+t1.hours*60+t1.minutes
        hours=minutes//60
        minutes=minutes%60
        print(hours,"hr and ",minutes,"min")
    def displayTime(self):
        print(self.hours,"hr and ",self.minutes,"min")
    def displayMinute(self):
        minutes=self.hours*60+self.minutes
        print(minutes,":minutes")

aT=Time(12,20)
bT=Time(12,50)
aT.addTime(bT)
aT.displayTime()
bT.displayMinute()













#Write a Person class with an instance variable “age” and a constructor that takes an integer as a
#parameter. The constructor must assign the integer value to the age variable after confirming the
#argument passed is not negative; if a negative argument is passed then the constructor should set
#age to 0 and print “Age is not valid, setting age to 0”. In addition, you must write the following instance
#methods:

#yearPasses() should increase age by the integer value that you are passing inside the function.
#amIOld() should perform the following conditional actions:I
#f age is between 0 and <13, print “You are young”.
#If age is >=13 and <=19 , print “You are a teenager”.
#Otherwise, print “You are old”.yearPasses() should increase age by the integer value that you are passing inside the function.
#amIOld() should perform the following conditional actions:I
#f age is between 0 and <13, print “You are young”.
#If age is >=13 and <=19 , print “You are a teenager”.
#Otherwise, print “You are old”.


class Person:
    def __init__(self,age):
        if age<0:
            self.age=0
            print("Age is not valid, setting age to 0")
        else:
            self.age=age
            
    def yearPasses(self,n):
        self.age=self.age+n
    
    def amIOld(self):
        if 0 < self.age <13:
            print("you are young")
        elif 13<= self.age <=19:
            print("you are teenager")
        else:
            print("you are old")

a=Person(7)
a.amIOld()
a.yearPasses(10)
a.amIOld()
a.yearPasses(10)
a.amIOld()
    







