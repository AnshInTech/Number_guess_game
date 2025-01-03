import os

def clear_terminal():
    # Clear command for Windows
    if os.name == 'nt':
        os.system('cls')

clear_terminal()
logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""
print(logo)
import random
game = False
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
level =input("Choose a difficulty. Type 'easy' or 'hard':").lower()
ran = random.randint(0,100)
count_h = 5
count_e = 10   
if level == "hard":
    while count_h>0:
        print(f"You have {count_h} attempts remaining to guess the number.")
        user = int(input("Input your number :"))
        count_h-=1
        if ran == user:
            print(f"You got it! The answer was {ran}.")
            count_h = -1
        if ran < user:
            print("Too High\nGuess again.")
        elif ran>user:
            print("Too low\nGuess again.")
        if count_h == 0 :
            print("You've run out of guesses, you lose.") 
              
if level == "easy":
    while count_e>0:
        print(f"You have {count_e} attempts remaining to guess the number.")

        user = int(input("Input your number : "))
        count_e-=1
        if ran == user:
            print(f"You got it! The answer was {ran}.")
            count_e = -1   
        elif ran < user:
            print("Too High\nGuess again.")
        elif ran>user:
            print("Too low\nGuess again.")
        elif count_e == 0 :
            print("You've run out of guesses, you lose.") 
