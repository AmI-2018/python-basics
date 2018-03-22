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

# Print a subset of the list
fruits = ["apples", "oranges", "pears"]
print(fruits[1:3])

# Copy the list
remember = fruits[:]

# Different way to remove an element
fruits.pop(1)
fruits.remove("apples")
print(fruits)

# You can also remove multiple elements at once
# del fruits[1:2]

# String to list
language_name = "Python"
print(list(language_name))

sentence = "this is a sentence"
words = sentence.split()
print(words)

# Dictionaries
legs = {"ant": 6, "snake": 0}

# Add a new element to the dictionary and set its correct value
legs["spider"] = 273  # basically, run
legs["spider"] = 8

# Different ways to delete an pair (key, value) from a dictionary
del legs["spider"]
# legs.pop("spider")

# Clear the entire dictionary
legs.clear()

# Get an element from the dictionary, print "Not present" if the key doesn't exist
print(legs.get("spider", "Not present"))
