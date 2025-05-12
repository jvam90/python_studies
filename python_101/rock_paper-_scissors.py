import random

move_player = input("Enter your move: ")
moves = ['rock', 'paper', 'scissors']
move_cpu = random.choice(moves)

print(f"Player move: {move_player}")
print(f"CPU move: {move_cpu}")

if (move_player == 'rock' and move_cpu == 'scissors') or (move_player == 'scissors' and move_cpu == 'paper') or (move_player == 'paper' and move_cpu == 'rock'):
    print("PLAYER WON")
elif (move_player == 'scissor' and move_cpu == 'rock') or (move_player == 'paper' and move_cpu == 'scissors') or (move_player == 'rock' and move_cpu == 'paper'):
    print("CPU WON")
else:
    print("DRAW")