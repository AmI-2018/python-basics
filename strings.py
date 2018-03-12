# String
for char in "hello":
    print(char)

say_hello = "hello"
print(say_hello[1])

# Type of a "character"
print(type(say_hello[1]))

# Building complex strings
language_name = "Python"
version = "3.6.4"

language = language_name + " " + version
print(language)

language = language_name * 3
print(language)

a = 3
b = 5
print(a, "times", b, "is", a*b)

print(str(a) + " times " + str(b))

say_hello = "helko"
# say_hello[3] = "l" # it's an error

# Getting input from the user
print("How old are you?")
age = input()  # age is a string, here
# age = int(input())  # if we want/need "age" as a number

print("Your age is " + age)
