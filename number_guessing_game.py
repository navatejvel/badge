import random
secret_number = random.randint(1, 100)
attempts = 0


print("Guess a number between 1 and 100. You have 10 attempts.")

while True:
        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        attempts += 1

        if guess == secret_number:
            print(f"🎉 Correct! You guessed it in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"❌ Out of attempts! The number was {secret_number}.")
