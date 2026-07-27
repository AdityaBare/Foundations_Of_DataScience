
marks = [90,98,76,86,45,36]

# List is mutable 

print(marks)
print(type(marks))
print(len(marks),'\n')

print("Initial list value")
print(marks[0])
print(marks[3])
print(marks[2])

marks[0] = 2
marks[3] = 5
marks[2] = 3.5

print("After updating list value")

print(marks[0])
print(marks[3])
print(marks[2])


# List Slicing

print(marks[0:4])

print(marks[-3:])

# List method 

list = [1,3,4]

# Add element at last 
list.append(2)
print('\n',list)

# Reverse list 
list.reverse()
print(list)

# Sort list in assending order
list.sort()
print(list)

# Sort in reverse order 
list.sort(reverse=True)
print(list)

# Insert value at specific index
list.insert(2,41)
print(list)

# Remove first occurence
print(list.remove(41)) #Return none
print(list)

# Remove element by idx

print(list.pop(3)) # Return removed value
print(list)