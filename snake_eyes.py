import random

both_equal_one = False
count_tries = 0

while not both_equal_one:
    count_tries += 1
    roll_1 = random.randint(1,6)
    roll_2 = random.randint(1,6)

    print(f"Try: {count_tries} / Dice 1: {roll_1} / Dice 2: {roll_2}")

    if roll_1 == roll_2 and roll_1 == 1:
        both_equal_one = True


print(f"It took {count_tries}.")