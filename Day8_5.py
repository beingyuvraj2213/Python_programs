# Encoding-Decoding
# fruits=["apple","banana"] , x=fruits.index("apple")

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def encrypt(text,shift):
    new_text=""

    for i in range(0,len(text)):
        #  for m in range(0,26):
        #     if text[i]==alphabet[m]:
        m=alphabet.index(text[i])
        change=m+shift

        if change>25:
            change=change-26

 
        new_text+=alphabet[change]
    print(f"The encoded text is {new_text}")

def decrypt(text,shift):

    new_text=""

    for i in range(0,len(text)):
    
        m=alphabet.index(text[i])
        change=m-shift

        if change<0:
            change=change+26

 
        new_text+=alphabet[change]
    print(f"The decoded text is {new_text}")

try_again=True

while try_again:

    direction=input("Type 'encode' to encrypt, type 'decode' to decrypt : \n")
    text=input("Type your message : \n").lower()
    shift=int(input("Type the shift number : "))

    if direction=="encode":
        encrypt(text,shift)
    if direction=="decode":
        decrypt(text,shift)  

    again=int(input("Press 1 to try again and 0 to exit : "))
    if again==1:
        try_again=True
    else :
        try_again=False



    