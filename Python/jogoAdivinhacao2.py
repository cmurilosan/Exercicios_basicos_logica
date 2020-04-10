# Simple guessing game: introduction to Python and PyCharm

# Libraries used:
import random

# Introduction:
print("*********************")
print("Let's start our game!")
print("*********************")

# Drawing a secret number:
print("Try to guess what the secret number is. It's between 1 and 100")
secret_number = round(random.randint(1,99)) # Return a random integer N such that a <= N <= b.
total_attempt = 0

# Scoring the game:
scores = 1000
attempt = 0
lost_scores = abs(secret_number - attempt) # Return a absolute number.

# Choosing the level of difficulty:
print("What level of difficulty do you want?")
print("Type: (1) for easy, or (2) for moderate, or (3) for hard.")
difficulty_level = int(input("Type your level of difficulty: ")) # Passing from 'str' to 'int'.

if difficulty_level == 1:
    total_attempt = 15
elif difficulty_level == 2:
    total_attempt = 10
else:
    total_attempt = 5

# Game functions:
for attempt_count in range(1, total_attempt + 1):
    print("Attempt {} of {}".format(attempt_count, total_attempt)) # String interpolation.
    attempt = int(input("Enter your number: "))

    if attempt < 1 or attempt > 99: # Limiting the range of possible responses.
        print("You must type a number between 1 and 99")
        continue # Skip the the current iteration only.

    you_hit = attempt == secret_number
    bigger_hit = attempt > secret_number
    lower_hit = attempt < secret_number

    if you_hit:
        print("You got it right! And scored {} points!".format(scores))
        break # Terminates the loop.
    else:
        if bigger_hit:
            print("You were wrong, the secret number is less than this.")
            scores = scores - lost_scores
            print("Your Current points: {}".format(scores))
        elif lower_hit:
            print("You're wrong, the secret number is bigger than this!")
            scores = scores - lost_scores
            print("Your Current points: {}".format(scores))

print("The secret number was {}.".format(secret_number))
print("End Game!")