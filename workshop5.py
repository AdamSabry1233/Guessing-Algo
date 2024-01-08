import random 

def guess_random_number(tries, start, stop):
    target_number = random.randint(start, stop)

    while tries != 0:
        print(f'Tries remaining: {tries}')
        user_guess = int(input('Guess a number between 0-10: '))

        if user_guess == target_number:
            print("Success you've guessed the correct number!")
            return
        
        elif user_guess < target_number:
            print("Guess higher!")

        elif user_guess > target_number:
            print("Guess lower!")

        tries -= 1

    if tries == 0:
        print(f"Sorry you've run out of tries, the correct number was {target_number}")


import random

def guess_random_number_lin(tries, start, stop):
    target_number = random.randint(start, stop)

    for _ in range(tries):
        guess = random.randint(start, stop)
        print(f"The number for the program to guess is: {target_number}")
        print(f"Number of tries left: {tries}")
        print(f"The program is guessing: {guess}")

        if guess == target_number:
            print("Success! The computer has guessed the correct number!")
            return

        tries -= 1

    print("Sorry! The computer has run out of tries!")


def guess_random_num_binary(tries, start, stop):
    target_number = random.randint(start, stop)

    low, high = start, stop

    for _ in range(tries):
        guess = (low + high) // 2
        print(f"The number for the program to guess is: {target_number}")
        print(f"Number of tries left: {tries}")
        print(f"The program is guessing: {guess}")

        if guess == target_number:
            print("Success! The computer has guessed the correct number!")
            return
        elif guess < target_number:
            print("Guess higher!")
            low = guess + 1
        else:
            print("Guess lower!")
            high = guess - 1

        tries -= 1

    print("Sorry! The computer has run out of tries!")


#guess_random_number(5, 0, 10)
        
#guess_random_number_lin(5, 0, 10)

guess_random_num_binary(5, 0, 100)