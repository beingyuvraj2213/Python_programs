# Rock Paper Scissors

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game=[rock,paper,scissors]
game1=["Rock","Paper","Scissor"]

print("Welcome to rock,paper,scissors game : ")

name=input("Enter your name : ")

def gamee():

    round=int(input("How many games you want to play : 1,3,5 -> "))

    comp=0
    player=0

    for i in range(round):

        op=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors : "))
        print(f"You chose {game1[op]}")
        print(game[op])

        op2=random.randint(0,2)
        print(f"Computer choose {game1[op2]} \n")
        print(game[op2])
        
        if op==op2:
            print("Game tied")
            
        elif op==0 and op2==2:
            print("You won this round") 
            player+=1

        elif op==1 and op2==0:
            print("You won this round")
            player+=1

        elif op==2 and op2==1:
            print("You won this round")
            player+=1

        else:
            print("You lose this round")
            comp+=1

            

    print(f"\n\nFinal Score :-> {name} : {player} \t Computer : {comp} ")

    if player>comp:

        print("\nCongratulations! You won this series. Keep Going because WINNERS NEVER QUIT")

    elif player==comp:
        print("\nSeries tied")

    else:
        print("\nYou lost the series. Don't get demotivated. Keep trying as WINNERS NEVER QUIT")

gamee()

ne=1
while ne==1:
    new=int(input("\n\nWanna play one more time : 1-Yes , 0-No -> "))       
    if new==1:
        gamee()
        ne=1
    else:
        exit()
        



