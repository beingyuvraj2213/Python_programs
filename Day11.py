# Black Jack Game
import random
import os
import art2
from art2 import logo

cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

def deal_card(): 
    """Returns a random card from the deck"""
    card=random.choice(cards)
    return card  

def calculate_score(cards):
    """Take a list of cards and returns the score calculated from the cards"""

    if sum(cards)==21 and len(cards)==2:
        return 0

    if sum(cards)>21 and 11 in cards:
            cards.remove(11)
            cards.append(1)    

    return sum(cards)  #sum(list)

def compare(user_score,computer_score):
    if user_score==computer_score:
        return "Draw"
    elif computer_score==0:
        return "Lose, opponent has Blackjack"
    elif user_score==0:
        return "Win with a Blackjack"
    elif user_score>21:
        return "You went over. You lose"
    elif computer_score>21:
        return "Opponent went over. You win"   
    elif user_score>computer_score:
        return "You win"
    else:
        return "You lose"     

def play_game():
    print(logo)

    user_cards=[]
    computer_cards=[]

    is_game_over=False

    for i in range(2):
        user_cards.append(deal_card())   #user_cards+=dealcard() -> can do this only if we are adding a list itself
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)

        print(f"Your cards : {user_cards}, current score {user_score}")
        print(f"Computer's first card : {computer_cards[0]}")

        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True

        else:
            user_should_deal=input("Type 'y' to get another card, type 'n' to pass : ")
            if user_should_deal=="y":
                user_cards.append(deal_card())
                # user_score=calculate_score(user_cards)
            else:
                is_game_over=True

    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)   

    print(f"Your final hand : {user_cards}, final score : {user_score}")
    print(f"Computer's final hand : {computer_cards}, final score : {computer_score}")

    print(compare(user_score,computer_score))    

while input("Do you want to play a game of Blackjack? Type 'y' or 'n' : ")=="y": 
    clear = lambda: os.system('cls')
    clear()
    play_game()
        
    

 





     
