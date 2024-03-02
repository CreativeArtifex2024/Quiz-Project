print("Test Your Knowledge : Quiz Quest")

playing = input("Do you Want to Play: ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's Play")
score = 0
answer = input("What is the capital city of France? ")

if answer.lower() == "paris":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input('Which planet is known as the "Red Planet?" ')

if answer.lower() == "mars":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input('Who wrote the play "Romeo and Juliet"? ')

if answer.lower() == "William Shakespeare":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What is the chemical symbol for water? ")

if answer.lower() == "h2o":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("Which mammal can fly without wings? ")

if answer.lower() == "bat":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("you got " + str(score) + " questions correct!")
print("you got " + str((score / 5) * 100) + "%.")

print("Done")
