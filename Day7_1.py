import random

word_list=["algebra","python","java","tiger"]
chosen_word=random.choice(word_list)

guess=input("Guess a letter : ").lower()

for i in range(0,len(chosen_word)):
    if guess==chosen_word[i]:
        print("Right")
    else:
        print("Wrong")
