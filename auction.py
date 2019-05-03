# Mubashir Haroon
# Mohsin Mehmood
# To run this program simply run "main()" in python shell
# This program is licensed under GNU General Public License version 3

# Declaring global variables and arrays
item_num = 0
item = [] # item name
item_desc = []
item_price =  []
item_id = []
sold = []
bids = [] # number of bid on an item
bid = [] # last bid on an item
buyer_id = []

def task1():
    global item_num
    
    item_num = int(input("Please enter number of items (minimum 10) "))
    print(chr(13))

    # continue in loop until items are at least 10
    while item_num<10: 
        item_num = int(input("please enter atleast 10 items "))

    # populating arrays with initial values
    for i in range(item_num):
        temp_item = input("Enter a item name ")
        item.append(temp_item)
        item_id.append(i)
        temp_item_desc = input("enter item description ")
        item_desc.append(temp_item_desc)
        temp_item_price = int(input("enter item price "))
        item_price.append(temp_item_price)
        bids.append(0)
        bid.append(0)
        sold.append("False")
        print(chr(13))

def task2():
    print("Welcome to Auction Buyer!!")

    # getting buyer's id and placing it in array if it doesn't exist in array yet
    temp_id = input("Please enter your ID ")
    if temp_id not in buyer_id:
        print("You are not registered, and would be registered now")
        buyer_id.append(temp_id)
    else:
        print("Welcome buyer", temp_id)

    print(chr(13))
    print("Following is the list of all products")

    # Showing all items which are not sold
    for i in range(item_num):
        if sold[i] == "False":
            print("item name is", item[i])
            print("item id is", item_id[i])
            print("item description is", item_desc[i])
            print("Current bid is", bid[i])
            print(chr(13))

    appr = "y" # rogue value

    # if more bids are to be placed then continue
    while appr == "y" or appr == "Y":
        temp_id = int(input("Please enter item id for which you want to place a bid ")) # getting item's id

        # checking if inputted id is correct
        while temp_id not in item_id:
            temp_id = int(input("Please enter a valid item id "))

        
        temp_bid = int(input("Enter a bid ")) # getting bid

        # checking if bid is greater than last bid
        while temp_bid<=bid[temp_id]:
            print("Last bid is,", bid[temp_id], ", Please enter a bid greater than last bid.")
            temp_bid = int(input("Enter a bid "))

        bid[temp_id] = temp_bid # replacing last bid of that item with new bid; the id is also same as index position so it is used for that as well
        bids[temp_id] += 1 # number of bids for that item is incremented 

        print(chr(13))
        appr = input("Do you want to place more bids? (y/n) ")

def task3():
    total = 0.0
    intrest = 0.0
    sold_no = 0 # number of items sold
    nobid_no = 0
    withbid_no = 0
    RATE = 1/10 # 10% auction company intrest rate
    
    for i in range(item_num):
        # check if reserved price is lesser or equal to last bid to deduce of it is sold or not
        if item_price[i]<=bid[i]:
            sold[i] = "True"
            total += bid[i] # add last bid to total and save it in total

    intrest = total*RATE # calculate the intrest
    total += intrest # calculate total fee of auction company (total bids + auction company intrest)

    print("Total fee for auction company is", total)
    print(chr(13))

    for i in range(item_num):
        # items which are not sold
        if sold[i] == "False":
            # items which didn't received any bid
            if bids[i] == 0:
                print("item", item_id[i], "didn't received any bids")
                nobid_no += 1
            else:
                # items which received bids but didn't reached reserved price
                print("item", item_id[i], "didn't reached reserved price with", bid[i], "as last bid")
                withbid_no += 1
        else:
            # when first 'if' is false, item is sold so increment number of items sold
            sold_no += 1

    print(sold_no, "item(s) were sold")
    print(nobid_no, "item(s) didn't received any bid")
    print(withbid_no, "didn't reached reserved price")
    print(chr(13))

def main():
    print("Welcome To Auction")
    
    # call all the three tasks together
    task1()
    appr = "y" # rogue value

    # continue to run task2() until no more bidders are left (appr = n or anything else)
    while appr == "y" or appr == "Y":
        task2()
        appr = input("Are there any more bidders? (y/n) ")
    task3()

    print("Thanks for comming to Auction")
    print("Good bye")
    
