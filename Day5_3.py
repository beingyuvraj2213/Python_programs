# To print maximum and minimum number

marks=input("Enter the marks of student in the class : ").split()
for i in range(0,len(marks)):
    marks[i]=int(marks[i])

max=marks[i]
min=marks[i]

for i in range(0,len(marks)):
    if marks[i]>max:
        max=marks[i]
    if marks[i]<min:
        min=marks[i]

print(f"Maximum marks : {max}")
print(f"Minimum marks : {min}")