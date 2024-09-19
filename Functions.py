#Basic Function
def greet():
    print("Hello, World!")
    
greet()

#Function with Parameters
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")
greet_person("Bob")


#Function with Return Value
def add(a, b):
    return a + b

result = add(5, 3)
print(result)


#Default Parameter Values
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()
greet("Alice")

#Keyword Arguments
def introduce(name, age, city):
    print(f"My name is {name}, I'm {age} years old, and I live in {city}.")

introduce(age=30, name="Alice", city="New York")


#Arbitrary Arguments (*args)
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

result = sum_all(1, 2, 3, 4, 5)
print(result)


#Arbitrary Keyword Arguments (**kwargs)
def display_info(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=30, country="New York")


#Lambda Functions
add = lambda x, y: x + y
print(add(5,3))

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)

#Nested Functions
def outer_function(text):
    def inner_function():
        print(text)
    inner_function()

outer_function("Hello from outer function!")


#Recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

