import random

num_dice = int(input("How many dices you want to roll: "))
num_die = int(input("How many sides each die will have: "))

amount_plays = random.randint(1, 10)

play = 0

print(f"There will be {amount_plays} rounds!")

while play <= amount_plays:
    input_play = input("Press enter to play, or 'q' to quit: ")
    if input_play == 'q':
        break

    print(f"Round {play + 1}: ")

    i = 0
    while i < num_dice:
        result = random.randint(1, num_die)
        print(f"Result dice {i + 1}: {result}")
        i += 1
    
    play += 1