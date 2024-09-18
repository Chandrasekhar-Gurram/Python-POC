age = 18

if age >= 18:
    print("You are an adult.")

age = 10

if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")


age = 25
is_student = False

if age < 18 or is_student:
    print("You are either under 18 or a student.")
else:
    print("You are an adult and not a student.")
