import random

input_range = input("Type top range: ")

if input_range.isdigit():
    input_range = int(input_range)

    if input_range <= 0:
        print("Please type number larger than 0 next time")
        quit()

else:
    print("Please type number next time")
    quit()

random_number = random.randint(0, input_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", guesses, "guesses")