# Snake = 1
# Gun = 2
# Water = 3

import random


moveNames=["Snake", "Gun", "Water"]
choice = [ 0, 1, 2]
score = 0



gameMatrix= [
    ['D', 'L', 'W'],
    ['W', 'D', 'L'], 
    ['L', 'W', 'D']
    ]


while(True):
    userInput = int(input("Enter your options\n Snake = 0, Gun = 1, Water = 2: "))
    comp = random.choice(choice)
    if gameMatrix[userInput][comp] == 'W':
        print(f"Your Choice: {moveNames[userInput]} and computer Move: {moveNames[comp]}, You win!")
        score += 1
    elif gameMatrix[userInput][comp] == 'D':
        print(f"Your Choice: {moveNames[userInput]} and computer Move: {moveNames[comp]}, It's a Draw!")
        continue
    else:
        print(f"Your Choice: {moveNames[userInput]} and computer Move: {moveNames[comp]}, You Lose!")
        break

print("Total Score:", score)
