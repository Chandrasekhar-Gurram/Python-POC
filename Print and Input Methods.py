#Print Method
print("Sample Message")
name = "Alice"
age = 30
print("Name:", name, "Age:", age)
print("apple", "banana", "cherry", sep=', ', end='.\n')
print(f'There is a {age}-year-old boy named {name} in the school.')
print('There is a {}-year-old boy named {} in the school.'.format(age,name))
print('There is a {1}-year-old boy named {0} in the school.'.format(name,age))

#Input Method
name = input("Enter your name: ")
print("Hello, " + name + "!")
age = int(input("Enter your age: "))
print("You are", age, "years old.")


#Operators
a = 10
b = 3
#Arithmetic Operators
print("Addition:", a + b)   
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b) 
print("Modulus:", a % b)   
print("Exponentiation:", a ** b) 

#Comparison Operators
print("Equal to:", a == b)  
print("Not equal to:", a != b) 
print("Greater than:", a > b) 
print("Less than:", a < b)
print("Greater than or equal to:", a >= b)
print("Less than or equal to:", a <= b)

#Logical Operators
x = True
y = False

print("AND:", x and y)
print("OR:", x or y)
print("NOT x:", not x)