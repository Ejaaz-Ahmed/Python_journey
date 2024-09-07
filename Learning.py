#Basic concepts....

print("Hello World") #Simple command to print anything written in qoutations
day = "Monday"    #In python, data type is automatically determined
date= 2
time = 32.3
print(day, date)    #not using quotations here because now printing the value
year = True    #boolean type variable
print(year)
first_name="Tom"
last_name="Jerry"
age=51
is_genius=True
print("Name of Person is", first_name, last_name)
print(first_name,last_name ,"'s age is",age)
print(first_name,last_name,"is a genius", is_genius)
name= input("What is your name?")    #to give the input from the user and storing in variable
print(name)
superhero=input("Who is your superhero?")
print("My superhero is",superhero)
old_age=input("Enter your  age")
new_age=int(old_age)+6       #To change the value of variable which was taken input, you would mention the data type.
print("you will be",new_age,"years old in 2030")
    #this example will explain the importance of mentioning data type
first=input("first?")
second=input("second?")
sum=first+second
print(sum)        #without using data type..
sum=int(first)+int(second)
print(sum)        #using data type...
print("the sum is",sum)
name="Tom"
print(name.upper())    #All letters will be uppercase....
print(name.lower())    #All letters will be lowecase
print(name.find("E"))    #find E,if E is present return true or 1 otherwise false or 0
print(name.replace("Tom","Jerry"))    #it will replace the Tom by Jerry
print('o' in name)    #it will print true if o is present
print('x' in name)
print(5+6,6-5,6*5,5/4,5//4,6%4,5**2)    #arithmetic operations
print(3<4 or 3>4)    #or will give true if any of the condition is true
print( not (4<4 and 4<22))     #not will change the result
age = input("Please enter your age")
#use of if, elseif and else
if int(age)>=18:
    print("You are an adult")
    print("You can vote")
elif (int(age)<18 and int(age) >3):
    print("you are a kid")
print("Thanks")

print("Calculator:")
first = float(input("Enter the first number: "))
operator = input("Enter the operation (+,-,*,/,%) ")
second = float(input("Enter the second number: "))
if operator == '+':
    print(first+second)
elif operator=='-':
    print(first-second)
elif operator=='*':
    print(first*second)
elif operator=='/':
    print(first/second)
elif operator=='%':
    print(first%second)
else:
    print("Invalid.....")
#Range
numbers = range(4)
print(numbers)    
i=1
while i <=5:    #while loop
    print(i* "*")
    i+=1
for i in range(5):    #for loop
    print(i)
#List in python
marks = [96,66,95,"English"]
print(marks)    #prints the whole list
print(marks[1])
print(marks[-3])    #check in a reverse manner
print(marks[0:3])
for score in marks:    #where score is temporarily created and gets each value of list
    print(score)
marks.append(88)    #it will insert at the end of list
marks.insert(1, 86)    #it will insert at the desired position i.e 1 (2nd position)
print(99 in marks)
print(marks)
i=0
while i<len(marks):
    print(marks[i])
    i+=1
marks.clear()    #clears the list
print(marks)
students=["Ejaz","Ahmed","Abdullah","Ali","Raza","osama"]
for student in students:
    if student == "Abdullah":
        #break    #break statement will terminate the loop
        continue    #continue statement will start the new iteration
    print(student)
#Tuple
marks = (99,65,89)    #can't be changed
print(marks.count(89))
#Set
marks = {99,33,19,19}
print(marks)    #always unique value, no index
#Dictionary, key and value
marks={"english":99,"name":"ejaz"}
print(marks["name"])
marks["name"]="Abdullah"
print(marks)
import math    #import is the keyword to include the necessary libraries
print(dir(math))    #it will show you the library of math
from math import sqrt
print(sqrt(16))    #square root function
from math import *    #*means all
def printsum(first,second):    #def is the keyword indicating function
    print(first+second)
    
printsum(3,4)    #calling printsum function
def calculator(first,second,operator):
    if operator=='+':
        print(first+second)
    elif operator=='-':
        print(first-second)
    elif operator=='*':
        print(first*second)
    elif operator=='/':
        print(first/second)
    elif operator=='%':
        print(first%second)
    else :
        print("invalid")

calculator(3,4,'-')

print(len("python"))    #it will print the length of string
print("2"+"2")
print(3*'python')
print (4//2)

#Well done. congratulations...........:)
#Practice 
