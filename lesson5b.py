#function with parameters
#Parameter:they are values that get passed as arguments given to a function inside of the parenthesis
def greeting(name):
    print(f"{name} How are you?I hope everything is fine")

greeting("Gabriel")

print("===============================")
def message(names):
    print(f"Hello {names}. we shall be having a general meeting on date.... please avail yourself.")
    # message("joy")
    # message("gabriel")
    for x in range(1,11):
        print(x)



print("===================================")

#Create that accept two parameters to add two numbers
def addition(x,y):
    sum=x+y
    print(" the sum of the numbers is:",sum)

addition(45,50)
addition(45,80)