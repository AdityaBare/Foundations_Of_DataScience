# Colllection of unorder items and each element in the set must be unique and immutable , But set is mutable(we can add and remove element)



# Examples of immutable types:

# int
# float
# str
# tuple (if it contains only immutable objects)

# Examples of mutable types:

# list
# dict
# set

# A set can only contain immutable objects because Python uses a hash value to store and find elements efficiently. Mutable objects can change, which would change their hash and break the set's internal structure.


set1 = {1,2,8,8,8,3,4,'aditya'} 

print(set1)

#Null Set 
null_set = set()
print(null_set)

# Add 

set1.add((10,99,999))
set1.add(10)
print(set1)


# .remove(el) remove element
set1.remove(10)
print(set1)

# .pop() remove a random element 

print(set1.pop())

#  set1.union(set2) -> combine both set values and return (save in third set)

set2 = {99,88,2,1,11,123}
set3 = set1.union(set2)
print("set1 :",set1)
print("set3 : ",set3)


#  set1.intersection(set2) -> combine both set common values and return (save in third set)

set4 = {99,88,2,1,11,123}
set5 = set1.intersection(set4)
print("set1 :",set1)
print("set3 : ",set5)

# .clear -> make set empty

set1.clear()
print(set1)