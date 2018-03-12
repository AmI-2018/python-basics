# Range
for number in range(0, 10, 2):
    print(number)

# List
fruits = ["apples", "oranges", "pears"]
# Dictionary
legs = {"ant": 6, "snake": 0, "cow": 4}

# Printing lists
for fruit in fruits:
    print("I love", fruit)

print(fruits)

# Printing dictionaries
for (animal, number) in legs.items():
    print("{} has {} legs".format(animal, number))

print(legs)

# Print a single list element
print(fruits[0])

# Replace a list element
fruits[0] = "strawberry"
print(fruits[0])

# Add a new element to the end of the list
fruits.append("bananas")
print(fruits)

# Extend the list with another list
fruits.extend(["apples"])
print(fruits)

# Concatenate a list with another list
fruits = fruits + ["kiwi"]
print(fruits)
