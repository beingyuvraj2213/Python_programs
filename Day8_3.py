import math 

test_h=int(input("Height of wall : "))
test_w=int(input("Width of wall : "))
coverage=5

def num_of_cans(h,w,c):
    count=(h*w)/c
    count=math.ceil(count)
    return count

cans=num_of_cans(test_h,test_w,coverage)

print(f"Number of cans required : {cans}")