single_quote_str = 'Hello'
double_quote_str = "World"
multi_line_str = '''This is 
a multi-line 
string.'''

print(single_quote_str) 
print(double_quote_str) 
print(multi_line_str)    

#String Concatenation
greeting = "Hello" + " " + "World"
print(greeting)

#String Repetition
repeated_str = "Hi! " * 3
print(repeated_str)

#String Indexing and Slicing
string = "Python"

# Indexing
print(string[0])
print(string[-1])

# Slicing
print(string[0:3])
print(string[2:])
print(string[:4])
print(string[-3:])


#String Length
string = "Hello, World!"
print(len(string))


#String Methods
text = "Hello, World!"

# Changing case
print(text.upper()) 
print(text.lower())

# Capitalizing
print(text.capitalize())
print(text.strip().capitalize())

# Title case
print(text.title())

# Replacing
print(text.replace("World", "Python"))

# Splitting and Joining
words = text.split(",")
print(words)

joined_string = "-".join(words)
print(joined_string)

# Finding and Counting
print(text.find("World"))
print(text.count("l"))

# Checking start and end
print(text.startswith("H"))
print(text.endswith("!"))
