# Secret Auction Program
import os

# clear()
print("Welcome To Blind Auction Program ")
auction={}
bidding_finished=False

def find_highest_bidder(bidding_record):
    max=0
    for thing in bidding_record:
        if int(bidding_record[thing])>max:
            best_bidder=thing
            best_bid=bidding_record[thing]

    print(f"The highest bidder is {best_bidder} with a bid of {best_bid}")            
        

while not bidding_finished:
    name=input("Enter your name : ")
    bid=input("Enter your bid : ₹")

    
    auction[name]=bid

    are_more_bidders=input("Are there more bidders : 1 for Yes & 2 for No")
    if are_more_bidders=="2":
        bidding_finished=True
    elif are_more_bidders=="1":
        clear = lambda: os.system('cls')
        clear()

print(auction)        

find_highest_bidder(auction)




