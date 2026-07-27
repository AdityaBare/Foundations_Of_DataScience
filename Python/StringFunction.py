# String is Immutable 
str = "i am coder"


# Boolean Result
print(str.endswith('r'))

# Capitalize first character
print(str.capitalize()) # Here is no change in original string  , this function return updated string.

# Replace all accurance of old value to new value
print(str.replace("am","am best")) # Here is no change in original string  , this function return updated string.

# Return index of first occurence
print("coder") #If not present then return -1

# Count the occurence of substring
print(str.count("e"))