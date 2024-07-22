import random

rand_number = random.randint(1,20)

def number_guessing_game():
    while True:
        guess = input("Enter a number you think is correct: ")
        # N/B: Prompt the user to enter any response then check if it is really a number
        if not guess.isdigit():
            print("Please enter a valid digit: ")
            continue
        
        guess = int(guess)
        
        if guess > rand_number:
            print("The number you guessed is too high!")
        elif guess < rand_number:
            print("The number you guessed is too low!")
        else:
            print("The number is correct.")
            break
        
number_guessing_game()
        