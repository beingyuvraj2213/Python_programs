import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty=input("Choose a difficulty. Type 'easy' or 'hard' : ")

if difficulty=="easy":
    attempt=10
if difficulty=="hard":
    attempt=5    

num=[]
for i in range(1,101):
    num.append(i)

number=random.choice(num)

game_over=False
while not game_over:

    guess=int(input("Make a guess : "))

    if guess==number:
        print("Excellent. You made the correct guess.")
        game_over=True
        break

    if guess-number>10:
        attempt-=1
        print(f"Too High \nGuess Again.\nYou have {attempt} attempts to guess the number. ")
    elif guess-number<-10:
        attempt-=1
        print(f"Too Low \nGuess Again.\nYou have {attempt} attempts to guess the number. ")
    elif guess<number:
        attempt-=1
        print(f"Its Low \nGuess Again.\nYou have {attempt} attempts to guess the number. ")
    else :
        attempt-=1
        print(f"Its high \nGuess Again.\nYou have {attempt} attempts to guess the number. ")        

    if attempt==0:
        print("Game Over")
        print(f"The number was {number}")



