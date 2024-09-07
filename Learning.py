"""

print("Ejaz will be hero")
day = "Monday"
date= 2
time = 32.3
print(day, date)
year = True
print(year)
first_name="Ejaz"
last_name="Ahmed"
age=51
is_genius=True
print("Name of Person is", first_name, last_name)
print(first_name,last_name ,"'s age is",age)
print(first_name,last_name,"is a genius", is_genius)
name= input("What is your name?")
print(name)
superhero=input("Ejaz who is your superhero?")
print("My superhero is my",superhero)
old_age=input("Enter your  age")
new_age=int(old_age)+6
print("you will be",new_age,"years old in 2030")
first=input("first")
second=input("second")
sum=first+second
print(sum)
sum=int(first)+int(second)
print(sum)
print("the sum is",sum)
name="Ejaz"
print(name.upper())
print(name.lower())
print(name.find("E"))
print(name.replace("Ejaz","Ahmed"))
print('a' in name)
print('x' in name)
print(5+6,6-5,6*5,5/4,5//4,6%4,5**2)
print(3<4 or 3>4)
print( not (4<4 and 4<22)) 
age = input("Please enter your age")
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
numbers = range(4)#range
print(numbers)    
i=1
while i <=5:
    print(i* "*")
    i+=1
for i in range(5):
    print(i)
marks = [96,66,95,"English"]#list
print(marks)
print(marks[1])
print(marks[-3])#reverse
print(marks[0:3])
for score in marks:
    print(score)
marks.append(88)
marks.insert(1, 86)
print(99 in marks)
print(marks)
i=0
while i<len(marks):
    print(marks[i])
    i+=1
marks.clear()
print(marks)
students=["Ejaz","Ahmed","Abdullah","Ali","Raza","osama"]
for student in students:
    if student == "Abdullah":
        #break
        continue
    print(student)
#tuple
marks = (99,65,89)#can't be changed
print(marks.count(89))
#set
marks = {99,33,19,19}
print(marks)#always unique value, no index
#Dictionary, key and value
marks={"english":99,"name":"ejaz"}
print(marks["name"])
marks["name"]="Abdullah"
print(marks)
import math
print(dir(math))
from math import sqrt
print(sqrt(16))
from math import *
def printsum(first,second):
    print(first+second)
    
printsum(3,4)
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
"""    
print(len("python"))
print("2"+"2")
print(3*'python')
print (4//2)