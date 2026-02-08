#reseach 
# Research on python list, tuple and Dictionary Data types.
#Alist is mutable ordered collection of elements: it can store different data types and can allows duplicate values. The list is represent using bracket squares[]
My_list=[1,2,3,4,5]
My_list.append(5) #adding an element
My_list.remove(2) # removing an element
print(My_list)
thelist=["banana","Avocado","jackfruit","apple","grapes","blackjack","dragon","strawberry","orange","lemon"]
print(thelist)

#Tuples
#are immutable, ordered element.like list tuples can store different element of data and allow duplicate values. The different between the two the tuples are represented using parentheses()
#Creating and accessing Tuples
my_tuple=(10,20,30)
print(my_tuple[1])# output:20
# They are commonly used for fixed data like coordinators or constants,and can also serve as dictonary  due to its immutabality nature.

#Dictionary 
#A dictionary is a mutable, unordered collection of key-value pairs (ordered since Python 3.7). Keys must be unique and hashable, while values can be of any data type. Dictionaries are represented using curly braces {}.
#examples
my_dict={'name':'Gabriel','age': 25}
my_dict["age"]=26 #updating Value
print('name') #output:Gabriel


