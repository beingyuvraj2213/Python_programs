
row1=["","",""]
row2=["","",""]
row3=["","",""]

map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")

position=input("Where do you want to put the treasure? ")
hr=int(position[0])-1
vr=int(position[1])-1

map[hr][vr]="Treasure"
print(f"{row1}\n{row2}\n{row3}")