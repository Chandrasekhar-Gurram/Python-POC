numbers = (1, 2, 3)
fruits = ("apple", "banana", "cherry")
mixed = (1, "apple", 3.14)


fruits = ("apple", "banana", "cherry")
print(fruits[0])
print(fruits[-1])

#Packing values into a tuple
person = ("Alice", 25, "Engineer")


#Unpacking tuple into variables
name, age, job = person

print(name)
print(age)
print(job)

# Single-element tuple
single_tuple = (42,)
print(type(single_tuple))

# Without the comma, it's just an integer
not_a_tuple = (42)
print(type(not_a_tuple))

#Tuple Methods
numbers = (1, 2, 3, 2, 2, 4)
#count() method
print(numbers.count(2))

#index() method
print(numbers.index(3))


#Slicing the tuple
numbers = (0, 1, 2, 3, 4, 5)

print(numbers[1:4])
print(numbers[:3])
print(numbers[3:])

