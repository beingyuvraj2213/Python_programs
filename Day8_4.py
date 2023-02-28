

def is_prime(x):
    
    c=0
    for i in range(1,x):
        if x%i==0:
            c+=1
    if c==1:
        print("It's a prime number")
    else:
        print("Its not a prime number")

num=int(input("Enter the number which you want to check : "))

is_prime(num)








        