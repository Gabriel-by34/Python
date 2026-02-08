#Tuples
# a tuple is immutable type of a list( it cannot change)
# To introduce a tuple we use a parentheses()
Counties=("Nairobi","Kakamega","Kisumu","Migori","Suba","Mombasa","Meru","Embu","Nyeri")
print(Counties)
print(type(Counties))
#Slicing a tuples
print(Counties[3:])
# accesing the items of the tuples using indexes
print(Counties[4])
print(Counties[9])# Error out of Range
# NOTE: below will gerenate an errors
Counties.append("Machakos")
print(Counties)# errors thats immutable(attribute error)

# this marks the end of sequential data types: (String,List & Tuples)

