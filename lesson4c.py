# A for loop can be used to iterate through the a list,tuple, string or even a dictonary
name="Gabriel"
for letter in name:
    if letter =="r":
        print("the letter is r")
else:
    print(letter)

    #Comments
print("...............................................")
# Below is a list of counties
counties=["Nakuru","Kisumu","Kakamega","Meru","Kericho","Eldoret","Bomet","Eldoret","Embu","Nairobi"]
print(counties)

for county in counties:
    print(county)

print("............................................")
for county in counties:
    if "Nairobi" in counties:
        print("The county is party of the list")
        break
else:
    print("The county is not party of the list")

print("............................................")
#For the loop can also be used to iterate through a dictonary
player={
    "name":"Musera",
    "Age" :35,
    "Nationality":"Kenyan",
    "Teams":["FC Leopard", "Homeboyz","Ingwe FC"]
}
for key in player:
    print(key)

print("............................................")
for value in player:
    print(player[value])

print("............................................")
# for loop the team the player has played for
print(player["Teams"])
for Teams in player:
    print(Teams)
   
