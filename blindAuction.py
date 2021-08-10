from replit import clear
bids= {}
biddingFinished = False

def highestBidder(biddingRecord):
    highestBid = 0
    for bidder in biddingRecord:
        bidAmount = biddingRecord[bidder]
        if bidAmount > highestBid:
            highestBid = bidAmount
            winner = bidder 
    print(f"Winner is {winner} with a bid of {highestBid}")



while not biddingFinished:
    name = input("Enter your name: \n")
    bidPrice = int(input("Enter your bid price: Rs."))
    bids[name] = bidPrice
    status = input("Are there any other bidders left? \n Type  'Yes' or 'No'")
    lowStatus = status.lower()
    if status == "no":
        biddingFinished = True
        highestBidder(bids)
    elif status == "yes":
        continue
    





