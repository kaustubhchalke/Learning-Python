

# 1. Create a list of given structure and get the Access list as provided below:

x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]

print(x[5][:5])






# Create a list of thousand numbers using range and xrange and see the difference between each
#other.

r=list(range(0,1001))
print(r)


# Write a program in Python to iterate through the list of numbers in the range of 1,100 and print
# the number which is divisible by 3 and is a multiple of 2.

x= [x for x in range(1,101) if x%3==0 and x%2==0 ]
print(x)


#Write a program in Python to reverse a string and print only the vowel alphabet if it exists in the
#string with their index.

x="consultadd"
s={}
y=""
for i in range(len(x)-1,-1,-1):
    if x[i] in ["a","i","e","o","u"]:
        s[x[i]]=i
print(x[i])
#dict[key]=value


#
#6. Write a program in Python to iterate through the string “hello my name is abcde” and print the
#string which is having an even length.

s="hello my name is abcde"
w=s.split()
for x in w:
    if len(x)%2==0:
        print(x)

#
#7. Write a program in python to print the pair of numbers whose sum is equal to the result
#number that is let's say 8.
#x=[1,2,3,4,5,6,7,8,9,-1]
        
x=[1,2,3,4,5,6,7,8,9,-1]
for i in range(0,len(x)):
    y=x[:i]+x[i+1:]
    for j in y:
        if x[i]+j==8:
            print(x[i],j)
    
        
#
#Write a program to find out the occurrence of a specific character from an alphanumeric string.
#Sample input: 12abcbacbaba344ab
#Expected output: a=5 b=5 c=2

#
#dict[key]=value
            
x="12abcbacbaba344ab"
res={}
for ele in x:
    if ele.isalpha():
        if ele in res:
            res[ele]+=1
        else:
            res[ele]=1
print(res)
        
    
#
#Generate and print another tuple whose values are even numbers in the given tuple
#(1,2,3,4,5,6,7,8,9,10).
            
            






`
