print("Welcome to MSD Pizza Deliveries")
size=input("What size pizza do you want? S,M,L : ")
add_pepperoni=input("Do you want pepperoni? Y,N : ")
extra_cheese=input("Do you want extra cheese? Y,N : ")
bill=0

if size=="S":
    bill=150
    if add_pepperoni=="Y":
        bill+=40
    if extra_cheese=="Y":
        bill+=40

if size=="M":
    bill=280
    if add_pepperoni=="Y":
        bill+=60
    if extra_cheese=="Y":
        bill+=40

if size=="L":
    bill=400
    if add_pepperoni=="Y":
        bill+=60
    if extra_cheese=="Y":
        bill+=40        

print(f"Your Final Bill Is : {bill}")