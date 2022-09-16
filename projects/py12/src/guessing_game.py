import random as rd

def guess(x):
    random_number = rd.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
        
    print('You guessed a number! {} is the correct number!'.format(random_number))
        
guess(10)