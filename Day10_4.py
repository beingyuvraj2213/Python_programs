import art1
from art1 import logo

print(logo)

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2 

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2        

def calculator():

    close_fun=False
    num1=float(input("What's the first number : "))
    while not close_fun:

        operations={
            "+":add,
            "-":subtract,
            "*":multiply,
            "/":divide,
        }    

        

        for thing in operations:
            print(thing)

        op=input("Pick an operation from the line above : ")

        num2=float(input("What's the second number : "))

        op1=operations[op]
        ans=round(op1(num1,num2),2)

        # function=operations["*"]

        print(f"{num1} {op} {num2} = {ans}")

        cnt=input(f"Type 'y' to continue calculating with {ans}, or type 'n' to start a new calculation : ")
        if cnt=="y":
            num1=ans
        else:
            calculator()

calculator()            
