from random import randint

def exponential_randomness(max, exp=2):
    index = 0

    while True:
        index += 1
        rand = randint(1, exp)

        if index == max:
            return max
        elif rand != 1:
            return index
        else:
            continue