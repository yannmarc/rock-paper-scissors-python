from multiprocessing import cpu_count
from pickle import FALSE
import random

# Declaring the variables for our to run
win = False
tie = False
playOn = True

game_list = ['R', 'P', 'C']
user_input = ''
cpu_input = ''
count = 0

while playOn:
    user_input = input('Hey Rock, Paper, or Scissors?: ').capitalize()
    cpu_input = random.choice(game_list)
    if user_input == cpu_input:
        playOn = False
        tie = True
        print("Hurray, It's a tie")
        break
    else:
        print(f"User Input: {user_input} , CPU: {cpu_input}")
        print("CPU won 😑")
        tie = False
    
    if user_input=='R' and cpu_input == 'C':
        playOn = False
        win = True
        print("Hurray, It's a win")
        break
    else:
        print(f"User Input: {user_input} , CPU: {cpu_input}")
        print("CPU won 😑")
        win = False
        
    if  user_input=='C' and cpu_input == 'P':
        playOn = False
        win = True
        print("Hurray, It's a win")
        break
    else:
        print(f"User Input: {user_input} , CPU: {cpu_input}")
        print("CPU won 😑")
        win = False
        
    if  user_input=='P' and cpu_input == 'R':
        playOn = False
        win = True
        print("Hurray, It's a win")
        break
    else:
        print(f"User Input: {user_input} , CPU: {cpu_input}")
        print("CPU won 😑")
        win = False
        