import random
str=input("Give me everybody's name separated by a comma : ")

str_new=str.split(",")

# length=len(str_new)
# temp=random.randint(0,length-1)

# payer=str_new[temp]
payer=random.choice(str_new)

print(f"{payer} will pay the bill")

input()