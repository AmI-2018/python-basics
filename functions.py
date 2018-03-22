# function with default parameters and docstring
def say_hello(name="AmI"):
    """
    This is a function for saying "hello"
    :param name: the name of the person to greet
    """
    print("Hello", name)


# function that returns more than one element
def build_greetings(name="AmI"):
    return ("Hello", name)


# sample call of the first function
say_hello("AmI students")

# sampe call of the second function
greetings, person = build_greetings()
print(greetings + " to " + person)
