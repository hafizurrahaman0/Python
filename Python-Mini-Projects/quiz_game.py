def calculate_score(score):
    print("You got " + str(score) + " questions correct!")
    print("You got " + str((score / 4) * 100) + "%.")

print("Welcome to computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

print("1. Level One")
print("2. Level Two")
game_level = int(input("Enter 1 or 2: "))

if game_level == 1:
    answer = input("What does CPU stand for? ")
    if answer.lower() == "central processing unit":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        print("correct answer: central processing unit")

    answer = input("What does GPU stand for? ")
    if answer.lower() == "graphics processing unit":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        print("correct answer: graphics processing unit")

    answer = input("What does RAM stand for? ")
    if answer.lower() == "random access memory":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        print("correct answer: random access memory")

    answer = input("What does PSU stand for? ")
    if answer.lower() == "power supply unit":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        print("correct answer: power supply unit")

    calculate_score(score)

elif game_level == 2:    
    answer = input("What does IDE stand for? ")
    if answer.lower() == "integrated development environment":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        print("correct answer: Integrated Development Environment")

    answer = input("What does OOP stand for? ")
    if answer.lower() == "object oriented programming":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        print("correct answer: Object-Oriented Programming")

    answer = input("What does HTTP stand for? ")
    if answer.lower() == "hypertext transfer protocol":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        print("correct answer: Hypertext Transfer Protocol")

    answer = input("What does CLI stand for? ")
    if answer.lower() == "command line interface":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        print("correct answer:  Command Line Interface")

    calculate_score(score)

else:
    print("Invalid Game Level")