#loops sometime we might need to do a piece of work a number of repeated times in such case we may use loops.
# Aloop is a control structure that exucute a block of code repeatedly until a cetain condition is met
# there are two types of loop in python thats: for loop and while Loop
#Below is syntax of for loop in python
"""
for variable in range(n):
#block of codes to be executed
"""
for greeting in range(5):
    print("hello moses",greeting)

    print('...........................')
    for number in range(10,20):
        print(number)
    print('............................')
#find an even number in range of 50,71
for number in range(50,71, 2):
    print(number)

print('...............................')
# write a python program that print odd number from 100 to 150
for number in range(101,150,4):
    print(number)

if number %2!=0:
    print(number)

#Create a program that prints the multiples of three starting from 201 to 150 
for  number in range (201,150,-3):
    print(number)


#create a python program that prints the leap years in between 2000 and 2024
for number in range (2000, 2024,4):
    print(number)
    



