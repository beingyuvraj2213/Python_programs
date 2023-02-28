import random

word_list=["algebra","python","java","tiger"]
chosen_word=random.choice(word_list)


word=[]
length=len(chosen_word)

for i in range(0,length):
    word+="_"
print(word)    

end_of_game=False

while not end_of_game:
    guess=input("Guess a letter : ").lower()

    for i in range(length):
        if guess==chosen_word[i]:
            word[i]=guess
              
    print(word)

    if "_" not in word:
        end_of_game=True
        print("Congratulations! you have completed the game successfully")






