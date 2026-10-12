import random

def guessing_game(max_attempts=5):
    secret_number = random.randint(1, 100)
    attempts = 0


    print(f"Guess a number between 1 and 100. You have {max_attempts} attempts.")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        attempts += 1

        if guess == secret_number:
            print(f"🎉 Correct! You guessed it in {attempts} attempts.")
            return
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")

    print(f"❌ Out of attempts! The number was {secret_number}.")

if __name__ == "__main__":
    guessing_game()
