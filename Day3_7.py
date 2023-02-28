# Love Calculator
# lower() converts string to lowercase
# count() counts frequency of a particular character in a string

print("Welcome to the Love Calculator")
name1=input("What is your name? \n")
name1=name1.lower()
name2=input("What is your love's name? \n")
name2=name2.lower()
temp_name=name1+name2

t=temp_name.count("t")
r=temp_name.count("r")
u=temp_name.count("u")
e=temp_name.count("e")

count1=t+r+u+e
count1=str(count1)

l=temp_name.count("l")
o=temp_name.count("o")
v=temp_name.count("v")
e=temp_name.count("e")

count2=l+o+v+e
count2=str(count2)

love_score=count1+count2

print(f"Your love score is {love_score}")

