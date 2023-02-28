# Encoding-Decoding
# fruits=["apple","banana"] , x=fruits.index("apple")

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def crypt(text,shift,direction):
    new_text=""

    if direction=="decode":
        shift*=-1
        

    for i in range (0,len(text)):

        if text[i] in alphabet:
            m=alphabet.index(text[i])
            
            change=m+shift 

            while change>25 or change<0:
                change=change%26    

            new_text+=alphabet[change]

        else:
            new_text+=text[i]


    print(f"The {direction}d text is {new_text}")  
        



try_again=True

while try_again:

    direction=input("Type 'encode' to encrypt, type 'decode' to decrypt : \n")
    text=input("Type your message : \n").lower()
    shift=int(input("Type the shift number : "))

    crypt(text,shift,direction)

    again=int(input("Press 1 to try again and 0 to exit : "))
    if again==1:
        try_again=True
    else :
        print("GoodBye!")
        try_again=False
