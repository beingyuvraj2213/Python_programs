import random

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
cap_letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','&','_']



print("Welcome to Python Password Generator")

nr_letters=int(input("Number of small letters you want in your password : "))
nr_cap_letters=int(input("Number of capital letters you want in your password : "))
nr_numbers=int(input("Number of digits you want in your password : "))
nr_symbols=int(input("Number of symbols you want in your password : "))


a=[]
for i in range(0,nr_letters):
    a.append(letters[random.randint(0,26)])

for i in range(nr_letters,nr_letters+nr_cap_letters):
    a.append(cap_letters[random.randint(0,26)])  

for i in range(nr_letters+nr_cap_letters,nr_letters+nr_cap_letters+nr_numbers):     
    a.append(numbers[random.randint(0,9)])
    
for i in range(nr_letters+nr_cap_letters+nr_numbers,nr_letters+nr_cap_letters+nr_numbers+nr_symbols):     
    a.append(symbols[random.randint(0,5)])

random.shuffle(a)
code=""
for i in a:
    code+=i

print(f"Generated password is {code}")
