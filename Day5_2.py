# Calculating average height
# split() -> splits a string into list
student_heights=input("Input a list of student heights ").split()
for n in range(0,len(student_heights)):
    student_heights[n]=int(student_heights[n])

# print(student_heights)    
sum=0
for n in range(0,len(student_heights)): #for height in student_heights:
    sum+=student_heights[n]

# add=sum(student_heights) can use this function

avg_height=round(sum/len(student_heights))
print(avg_height)