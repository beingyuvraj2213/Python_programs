ht=int(input("Enter your height in cm : "))

if ht>120 :
    print('You can ride the rollercoaster')
    age=int(input("Enter your age : "))
    if age>18 :
        print("You will be charged 100 rupees")
    elif age>=12:
        print("You will be charged 70 rupees")
    else :
        print("You will be charged 50 rupees")
else :
    print("Sorry, you cannot the rollercoaster ride")            