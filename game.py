# -----------------
# Game No one
# -----------------
""" 
score = 100
secret_number = 50
guess = int(input("Enter your guess: "))

if guess == secret_number:
    print("Correct!")
    score = score + 20
    print("Your Score:", score)

elif guess > secret_number:
    print("Too High!")
    score = score - 10
    print("Your Score:", score)

else:
    print("Too Low!")
    score = score - 10
    print("Your Score:", score)
"""
# -----------------
# Game No Two
# -----------------
""" 
print("MAGIC NUMBER GAME")

print("--------------------")

number = int(input("Enter a number: "))

result = number * 2 + 10

print("Your Magic Number is:", result)

answer = int(input("Guess the Magic Number: "))

if answer == result:
    print("You Win!")
else:
    print("You Lose!")
"""    