# Dictionary is mutable in python
Student = {
    'name':"Aditya",
    "age":22,
    "score":{
        "math":30,
        "dbms":56,
        "SEMD":50,
    },
    "Program":"IT"
}

print(Student['name'])
print('Math Score : ',Student['score']['math'])

Student['score']['math'] = 98

print("Updated math score :", Student['score']['math'])

print(Student.keys()) # Print all keys , which further only converted into list..

# .keys()
List = Student.keys()
print(List)
print(type(List))

List2 = list(Student.keys()) #Return all keys in list 
print(List2)
print(type(List2))

# .values()

print(Student.values())
print(list(Student.values()))
print(tuple(Student.values()))

# .items() -> return all key:value pair as tuple

print(Student.items())
print(list(Student.items()))
print(tuple(Student.items()))


# .get('key')

print(Student.get("name")) # Get they value 

# In this if key is not present in the dictionary that time it return none , but we use Student['key'] which is not present in dictionary it return error that stop execution of code .

# .update("key":"value") -> to add pair in dict

Student.update({"cgpa":8.91})

print(Student)
