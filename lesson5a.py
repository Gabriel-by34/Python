# Python function
# they are block of code/statements that performs a given task/action.they can be reused throughout the program to perform different tasks.
# Functions are defined using def keyword.(define)
# We have two main type of functions i.e:
#1. in buit function=> they come preinstalled with the interpreter i.e print(), pop(), range(), append() et.c
#2.User defined functions=> they are created by a programmer to solve a given task
# to define a function you need to give it a name followed by parenthesis
# for the funcctions body, it is usually indented and to invoke a function we use the function name
def greeting():
    print("Hello are you?")
    #Below we call the function by use of its name
greeting()

print("========================================")
#addition function
def addition():
    num1=40
    num2=50
    sum=num1+num2
    print("The sum of the numbers:", sum)
addition()
   
print("==================================")
#create a function that can be able multiple three values
def multiplication():
    num1=10
    num2=30
    num3=20
    product=num1*num2*num3
    print("the product of the numbers:",product)
multiplication()

# below is division function
def divide():
    number1=int(input("Enter the number: "))
    number2=int(input("Enter the number: "))
    quotient=number1/number2
    print("The answer is:", quotient)
    print("-------")
for function in range(3):
    divide()




