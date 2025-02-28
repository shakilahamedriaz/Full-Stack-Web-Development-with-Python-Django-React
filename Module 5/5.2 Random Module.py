import random

help(random)
#help(random), Python will display the documentation for the random module
print(dir(random)) # we can see there is no __init__ , so it is package shurly
print(random.__doc__) # breaf description of random module




# now see some exampe of random module examples:

# Random float between 0 and 1
print(random.random())

## Random float between 5 and 10
print(random.uniform(5, 10))

# Random integer between 10 and 50
print(random.randint(10, 50))

# generates a random number from the range 1 to 99, incrementing by 5 (e.g., 1, 6, 11, ... 96).
print(random.randrange(1, 100, 5))


fruits = ['apple', 'banana', 'cherry', 'mango']
# Random choice from a list
print(random.choice(fruits))

# Shuffle a list
random.shuffle(fruits)
print(fruits)


def generate_pin():
    return random.randint(1000, 9999)

# to generate 4 digit pin, like one time pass/varification etc
print(f"Your 4 digit otp pin {generate_pin()}")