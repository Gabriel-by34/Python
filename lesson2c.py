#Dictionary
#Is a data type that store data in terms of keys-value pair
#It is introduced by use of curly braces{}
# The value of data stored inside a dictonary can of any type
# To access the values in dictonary we use the keys
Phonebook={
    "Benson":"+254712347514",
    "Grace":"+254715146512",
    "Gabriel":"+254790953000"
}
#showing the entire dictonary
print(Phonebook)
print(type(Phonebook))

# printing out the benson number
print(Phonebook["Benson"])
#Second option
player={
    "name":"messi",
    "age": 40,
    "teams":["PSG","Bercalona","Argentina"]

}
#Print  bercalona the second team he played for
print(player["teams"][1])

