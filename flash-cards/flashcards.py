#import the json module from python3
import json
#importing the random library
import random

def flashCard():
    #make question random
    random.shuffle(data["cards"])
    #initialize the score as 0
    score = 0

    for i in data["cards"]:
        guess = input(i["q"] + ">")
    #print(guess)
        if guess.lower() == i["a"].lower():
            score += 1
            print(f"Correct! Current Score: {score}/{total}")
        else:
            print("Incorrect! the correct answer was" , i["a"])
            print(f"Current Score: {score}/{total}")

def playAgain():
    play = input("Do you want to play again? Enter Yes or No: ")
    if play.lower() == "yes":
        return True
    return False

#open the file and parse the json
with open('me-capitals.json', 'r') as f:
    data = json.load(f)
    #print(data)

#initialize the total length of the cards array
total = len(data["cards"])

keepGoing = True
#to run the game playAgain
while keepGoing:
    #call functions
    flashCard()
    keepGoing = playAgain()
