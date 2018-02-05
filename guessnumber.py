import random

guesscount = 0
number = random.randint(1,100)

username = input("Hello, what's your name?")
print(f"Well, {username}, you will get 10 chances to guess the number between (1,100) ")

while guesscount < 10:
    print(f"{username}, take a guess:")
    guess = int(input())
    guesscount += 1

    if guess > number:
        print('Your guess is too high.')
    elif guess < number:
        print('Your guess is too low.')
    elif guess == number:
        print(f"Good Job {username}, you guessed the number in {guesscount} guesses!")
        break

if guess != number:
    print(f"Better luck next time. The number is {number}")
