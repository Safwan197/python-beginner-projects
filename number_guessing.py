# Number Guessing Game

import random
numbers = [] # Empty list to store Numbers
n = int(input("Enter Numbers You want to generate : "))
for i in range(1,n+1):
    numbers.append(i)

print(numbers)

points = 0  
guess = 0

guessed = random.choice(numbers) # Generate Random Numbers

while guess <= 5 :
    userInput = int(input("Enter Number: "))
    if(guessed == userInput):
        print("🎉You guessed it! The number was : ",userInput)
        guess+=1 
        points+=1
        print("Your Score : ",points)

    else:
        print("❌ Try again")
    guess+=1 

print("Game Finished")
