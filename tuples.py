# creating a tuple
my_tuple = (1,2,3,4)
print(my_tuple)
 
# printing type of tuple
print(type(my_tuple))
 
# diffrent data types can be operated with tuple
tuple2 = ("sting",'c',123,123.4,["d1","d2"])
print(tuple2)
 
# Nested tuples
tuple3 = ("sting", 'C', 123, 123.4, [4,5,6], (1,2,3))
print(tuple3)
 
# anything declared by default is a tuple, with square braces is list
tuple4 = 3,4,5,"string",'C'
print(type(tuple4), tuple4 )
 
# accessing data in tuple, Indexing starts from 0
print(tuple3[3])
 
# data in tuple can be accessed by this method
# accessing 3rd char of string of tuple3
print(tuple3[0][2])
# accessing 3rd item of tuple in tuple3
print(tuple3[4][2])
 
# single data in a tuple gets the type of datatype inside it
# a tuple cannot be created with a single datatype in it.
tuple5 = ("single data")
print(type(tuple5))
# a tuple can be created with a single datatype by adding a comma " ," after datatype
tuple6 = ("single data",)
print(type(tuple6))
 
# diffrence bw list and tuple,
# => list is mutable it can be modified, while tuples are immutable
# lets try changing data in tuple
# tuple[2] = 456
# print(tuple[2])
# gives error TypeError: 'type' object does not support item assignment
 
# couting the repeatation.
tuple7 = ('a', 'b','c','d','a')
print("occurance of a :", tuple7.count('a'))
 
# testing if an item exists in tuple or not
print('a' in tuple7) #True
print('f' in tuple7) #False
print('b' in tuple7) #True
 
# print all data of tuple using for loop
for items in tuple3:
  print(items)
 
# create a tuple, take input from user, check if item is in it
tuple8 = input("enter data in tuple:")
print(tuple8)
 
datatocheck = input()
# checking
if(datatocheck in tuple8):
  print("data present")
else:
  print("data not present")
