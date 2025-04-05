print("Hey every one , I am Debashis")

def chai (n):
  print(n)

chai("Lemon tea")

# using : from importlib import reload
#         reload(file_name)  ----> we can reload any file in terminal
# We can import any module by just typing ----> import module_name
# Then we can use the functions in this module ----> module_name.function_name()

chai_one = "Lemon tea"
chai_two = "Mint tea"
chai_three = "Masala chai"

# Mutable vs immutable(the next updated value points to the another memory location)
x=5
y=x
print(y)
x=9
print(x)
print(y)

# one can take help of dir(variable_name) to check how many methods are posible on this variable
# remembet two things :-
# for mathod calling ----- > variable_name[method_name]
# for function calling ----- > function_name(arguments) 

mylist=[123, "chai", 3.14, True]
print(mylist)
print(len(mylist)) # to check the length of the list
print(mylist[0]) # to access the first element of the list

mydict = {
    "name": "Debashis",
    "age": 21,
    "hobby": "coding"
}
print(mydict)
print(mydict["name"]) # to access the value of the key in the dictionary

mytuple = (1, 2, 3, 4, 5)
print(mytuple)
print(len(mytuple)) # to check the length of the tuple
print(mytuple[0]) # to access the first element of the tuple
# defference between list and tuple is that list is mutable and tuple is immutable

# sys.refcount() is used to check the reference count of an object
import sys
a = 10
b = a
print(sys.getrefcount(a)) # to check the reference count of the object a

m=[1,2,3]
n=m
print(m==n) # to check the equality of the two lists
print(m is n) # to check the identity of the two lists
m=[1,2,3]
n=[1,2,3]
print(m==n) # to check the equality of the two lists
print(m is n) # to check the identity of the two lists
# here m and n are two different lists but they have same values so they are equal but not identical
# so the identity of the two lists is different