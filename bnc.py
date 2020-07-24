#cli-games/bnc.py
#import the random library
from random import randint

#make an array
roles = ["Bear", "Ninja", "Cowboy"]


player = False
while player == False:
#get player input
    player = input("Bear, Ninja, or Cowboy? > ")
    computer = roles[randint(0,2)]
#compare the computer and player role
#print(computer, player)
    if computer == player:
        print("Draw!")
    elif computer == "Cowboy":
        if player == "Bear":
            print("You Lose!", player, "is shot by", computer)
        else: #computer is cowboy, player is Ninja
            print("You Win!", player, "assasinates", computer)
    elif computer == "Bear":
        if player == "Cowboy":
            print("You Win!", player, "shoots", computer)
        else: #computer is bear, player is Ninja
            print("You lose!", player, "is eaten by", computer)
    elif computer == "Ninja":
        if player == "Cowboy":
            print("You Lose!", player, "is assasinated", computer)
        else:
            print("You Win!", player, "eats", computer)
    play_again = input("Would you like to play again? (yes/no) > ")
    if play_again == 'yes':
        player = False
        computer = roles[randint(0,2)]
    else:
        break
