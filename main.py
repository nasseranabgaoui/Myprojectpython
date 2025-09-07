# number_guess_game.py

import random

print("Welcome to the Number Guessing Game!")

# Générer un nombre aléatoire entre 1 et 50
secret_number = random.randint(1, 50)

# Initialiser le nombre d'essais
attempts = 0
max_attempts = 5

# Boucle principale du jeu
while attempts < max_attempts:
    guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Guess the number (1-50): "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
        break
else:
    print(f"Game over! The secret number was {secret_number}.")

# Statistiques simples
print(f"You made {attempts} attempt(s).")
if attempts <= 2:
    print("Great job! You are a pro guesser!")
elif attempts <= 4:
    print("Not bad! Keep practicing!")
else:
    print("Better luck next time!")

print("Thanks for playing!")
