import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list=["algebra","python","java","tiger"]
chosen_word=random.choice(word_list)


word=[]
length=len(chosen_word)

for i in range(0,length):
    word+="_"
print(word)    

end_of_game=False
m=6

while not end_of_game:
    guess=input("Guess a letter : ").lower()
    
    c=0
    

    for i in range(length):
        if guess==chosen_word[i]:
            word[i]=guess
            c+=1
    if c==0:
        print(f"Oops, Think Carefully {stages[m]}")   
        m-=1           
    print(word)

    if m==-1:
        print("You lose. Try Again")
        end_of_game=True

    if "_" not in word:
        end_of_game=True
        print("Congratulations! you have completed the game successfully")






