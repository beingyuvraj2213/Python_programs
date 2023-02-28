import random

word_list=["algebra","python","java","tiger"]
chosen_word=random.choice(word_list)


word=[]
length=len(chosen_word)

for i in range(0,length):
    word+="_"
print(word)    

guess=input("Guess a letter : ").lower()

for i in range(length):
    if guess==chosen_word[i]:
        word[i]=guess

print(word)










# for i in range(0,len(chosen_word)):
#     if guess==chosen_word[i]:
#         print("Right")
#     else:
#         print("Wrong")

