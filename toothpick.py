name_player_1 = input("What is your name, player 1: ")
name_player_2 = input("What is your name, player 2: ")
current = name_player_1
num_toothpicks = 13

while num_toothpicks > 0:
    print(num_toothpicks * "|")
    print(f"There are {num_toothpicks} toothpicks left")    
    
    amount = int(input(f"How many do you take, {current}: "))
    while amount not in [1,2,3]:
        amount = int(input(f"You can only take 1, 2 or 3, {current}: "))
    num_toothpicks -= amount

    if num_toothpicks <=0:
        print(f"{current} wins!!!")
        print("GAME OVER!!!")


    current = name_player_2 if current == name_player_1 else name_player_1




