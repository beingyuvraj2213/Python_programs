marks=input("Enter the marks of student in the class : ").split()
for i in range(0,len(marks)):
    marks[i]=int(marks[i])

max=max(marks)
min=min(marks) 
print(max)
print(min)   