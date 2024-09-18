#Comments:
# This is a single-line comment
x = 5  # Assigning 5 to variable x
print(x)  # Print the value of x


"""
This is a multi-line comment.
It can span multiple lines.
"""
y = 10
print(y)

'''
Another way to write a multi-line comment.
This will also be ignored by the interpreter.
'''
z = 15
print(z)



def greet(name):
    '''
    Function to greet a person with their name.
    
    Parameters:
    name (str): The name of the person to greet.
    
    Returns:
    None
    '''
    print("Hello, " + name)

print(greet.__doc__)
