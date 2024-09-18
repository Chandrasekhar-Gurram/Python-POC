#Example of Uniqueness:
numbers = {1, 2, 2, 3, 4, 4, 5}
print(numbers)


# Looping through a set
fruits = {"apple", "banana", "cherry"}
for fruit in fruits:
    print(fruit)

#Adding Elements to Set
fruits = {"apple", "banana"}
fruits.add("cherry")
print(fruits)
fruits.update(["orange", "grape"])
print(fruits)


#Removing Elements from Set
fruits = {"apple", "banana", "cherry"}

fruits.remove("banana")
print(fruits)
fruits.discard("grape")
removed_item = fruits.pop()
print(removed_item)
print(fruits)
fruits.clear()
print(fruits)


#Union
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1 | set2
print(union_set) 
union_set = set1.union(set2)
print(union_set)

#Intersection
set1 = {1, 2, 3}
set2 = {3, 4, 5}

intersection_set = set1 & set2
print(intersection_set)

intersection_set = set1.intersection(set2)
print(intersection_set)

#Difference
set1 = {1, 2, 3}
set2 = {3, 4, 5}

difference_set = set1 - set2
print(difference_set)
difference_set = set1.difference(set2)
print(difference_set)

#Symmetric Difference
set1 = {1, 2, 3}
set2 = {3, 4, 5}

symmetric_diff = set1 ^ set2
print(symmetric_diff)
symmetric_diff = set1.symmetric_difference(set2)
print(symmetric_diff)
