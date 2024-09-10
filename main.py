import art
import random
def play_game():
    greeting()
    original_number = select_range()
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard' ")
    if difficulty == 'easy':
        attempts = 10
        attempts_message(attempts)
        if make_a_guess(attempts,original_number) == 0:
            print("You've run out of guesses, you lose")
    elif difficulty == 'hard':
        attempts = 5
        attempts_message(attempts)
        if make_a_guess(attempts, original_number) == 0:
            print("You've run out of guesses, you lose")

def greeting():
    print(art.logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a random number between your range")

def select_range():
    first_num = int(input("Write your lower bound of range: "))
    second_num = int(input("Write your upper bound of range: "))
    return random.randint(first_num,second_num)

def attempts_message(attempts_left):
    print(f"You have {attempts_left} attempts remaining to guess the number.")

def make_a_guess(attempts,original_number):
    while attempts > 0:
            guess = int(input("Make a guess: "))
            if guess == original_number:
                print(f"You got it! The answer was {guess}")
                return attempts
            elif guess > original_number:
                print("Too high.")
                attempts -= 1
                continue
            elif guess < original_number:
                print("Too low")
                attempts -= 1
                continue
    return 0

while input("If you want to play type '1': ") == '1':
    play_game()