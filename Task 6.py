
#Write a program in Python to find out the character in a string which is uppercase using list
#comprehension.

z=[x for x in input("Enter string:") if x.isupper()]
print(z)


#Write a program to construct a dictionary from the two lists containing the names of students and
#their corresponding subjects. The dictionary should map the students with their respective subjects.
#Let’s see how to do this using for loops and dictionary comprehension.
#HINT - Use Zip function also

#Sample input: students = ['Smit', 'Jaya', 'Rayyan'] subjects = ['CSE', 'Networking', 'Operating System']
#Expected output: {‘Smit’ : ’CSE’ , ’Jaya’ : ’Networking’ , ’Rayyan’ : ’Operating System’}

students = ["Smit", "Jaya", "Rayyan"]
subjects = ['CSE','Networking','OS']
print ("Students : " + str(students))
print ("Subjects : " + str(subjects))
res = dict(zip(students, subjects))
print ("Output : " +  str(res))



#Write a program in Python using generators to reverse the string.
#Input String = “Consultadd Training”

def rev(str):
    length = len(str)
    for i in range(length - 1, -1, -1):
        yield str[i]
for char in rev("Consultadd Training"):
    print(char)







#Write an example on decorators.

def decorator(func):
    def wrap():
        print("first")
        func() 
        print("second")     
    return wrap
@decorator
def demo():
    print("Demo function !!")
demo()











