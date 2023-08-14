import random

def generate_random_number(x, y):
    return random.randint(x, y)

lower_number = int(input("Lower number"))
higher_number = int(input("higher number"))
generate_random_number(lower_number,higher_number)
