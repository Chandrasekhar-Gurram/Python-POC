dictionary = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}


person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

print(person)

# Accessing values by key
print(person["name"])
print(person["age"])

print(person.get("city"))
print(person.get("job"))

#Modifying Existing Values
person["age"] = 26
print(person)

#Adding New Key-Value Pairs
person["job"] = "Engineer"
print(person)


#Removing Key-Value Pairs
person.pop("city")
print(person)

del person["job"]
print(person)

person.clear()
print(person)


#Looping Through a Dictionary
person = {"name": "Alice", "age": 26, "city": "New York"}

#Looping Through Keys
for key in person:
    print(key)

#Looping Through Values
for value in person.values():
    print(value)

#Looping Through Key-Value Pairs
for key, value in person.items():
    print(key, ":", value)

#Dictionary Methods
print(person.keys())  
print(person.values()) 
print(person.items())

new_info = {"country": "USA", "age": 27}
person.update(new_info)
print(person)


#Nested Dictionaries
employees = {
    "employee1": {"name": "Alice", "age": 25, "job": "Engineer"},
    "employee2": {"name": "Bob", "age": 30, "job": "Manager"}
}

print(employees["employee1"]["name"])


#Dictionary Comprehensions
squares = {x: x**2 for x in range(5)}
print(squares)

