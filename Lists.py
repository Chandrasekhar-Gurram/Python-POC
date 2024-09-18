#List Initialization
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "apple", 3.14, True]

#List Values Indexing
fruits = ["apple", "banana", "cherry"]
print(fruits[0])
print(fruits[1])
print(fruits[-1])

#Assigning new values to List
fruits[1] = "blueberry" 
print(fruits)

#Adding new values to List
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)

fruits.insert(1, "blueberry")
print(fruits)

more_fruits = ["orange", "grape"]
fruits.extend(more_fruits)
print(fruits)

#Removing Elements from List
fruits = ["apple", "banana", "cherry", "banana"]

fruits.remove("banana")
print(fruits)

popped_fruit = fruits.pop(1)
print(popped_fruit)
print(fruits)

fruits.clear()
print(fruits)

#List Slicing
numbers = [0, 1, 2, 3, 4, 5, 6]

print(numbers[2:5])
print(numbers[:4])
print(numbers[4:])

#List Length
fruits = ["apple", "banana", "cherry"]
print(len(fruits))  # Output: 3

#Sorting and Reversing a List
numbers = [4, 2, 8, 1, 7]
numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)


#List comprehension
squares = [x**2 for x in range(5)]
print(squares)

even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)


#Nested Lists
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list[1])
print(nested_list[1][2])

