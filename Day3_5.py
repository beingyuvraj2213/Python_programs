ht=int(input("Enter your height in cm : "))
bill=0
if ht>120 :
    print('You can ride the rollercoaster')
    age=int(input("Enter your age : "))
    if age>18 :
        bill=100
        print(f"Adult Tickets - {bill} rupees")
    elif age>=12:
        bill=70
        print(f"Youth Tickets - {bill} rupees")
    else :
        bill=50
        print(f"Child Tickets - {bill} rupees")
    want_Photo=input("Do you want photo of your ride. Press Y or N : ")
    if want_Photo=='Y':
        bill+=20
        print(f"Your total bill : {bill}")

    print(f"Your total bill : {bill}")
else :
    print("Sorry, you cannot the rollercoaster ride")            