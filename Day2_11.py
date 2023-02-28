tbill=float(input("What was the total bill ? "))
tip=float(input("What percentage tip would you like to give ? 10, 12 or 15 : "))
person=int(input("How many people to split the bill? "))

amt=(tbill+(tbill*(tip/100)))/person
amt=round(amt,2)
amt="{:.2f}".format(amt)  #important
print(f"Each person should pay : {amt}")