#python list
# Alist in python is a collection of items that are ordered in a certain way
# A list is introduced by use of square bracket[]
# Items of a list are stored inside indexes. Note: in programming we start counting from index (0), bmw, ford , benze, hiance
Cars=["Range","BMW","Prado","Nissan","benze","Mclarel","Mercedes","Toyota","Landrover","Isuzu"]
print(Cars)
print(type(Cars))
# Accessing items of the List
print(Cars[2])
print("The car on index four is;", Cars[4])


#List Slicing : This is creating a list from a given bigger list
print(Cars[4:])
# printing from index zero to three
print(Cars[:4])
# printing from Prado to mclarel
print(Cars[2:6])

# List Mutability
# we use the fucntion append to add an item at the end of the list
Cars.append("Mithubishi")
print(Cars)
Cars.append("Subaru")
print(Cars)

# we use pop function to remove an items from the list at the end
Cars.pop()
print(Cars)
# we can use an index to add an item on the list
Cars[5]="Pajero"
print(Cars)
# we can use the Sort function to sort our items in alphabetical order
Cars.sort()
print(Cars)
# Cars.sort(Reverse=True)
Cars.sort(reverse=True)
print(Cars)
del Cars(4)
print(Cars)
Cars.remove(bmw)
print(Cars)

