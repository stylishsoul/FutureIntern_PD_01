import random

def guessing_game():
    ans = random.randint(0,100)

    while True:
        guess = int(input("What's Your Guess? "))

        if guess == ans:
            print(f"Congratulations!!! {guess} is Correct Answer")
            break

        if guess < ans:
            print(f"{guess} is too low")

        else:
            print(f"{guess} is too high")

guessing_game()