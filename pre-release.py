#!/usr/bin/env python3

## Pre Relese Material of May/June 2020
## Solution by Mubashir Haroon (O3-B)

## import distutils.util library to ask y/n questions
import distutils.util
import random

## initializing the totals of each day (required in payPrice() and main())
totalDay1 = totalDay2 = totalDay3 = totalDay4 = totalDay5 = totalDay6 = totalDay7 = 0.0

## generate parking number
def genCode():
    ## genetate random four digit number with appropriate zeros where necessary
    code = str(random.randint(0,9999)).zfill(4)

    ## seperate the digits
    i = int(code[0])
    ii = int(code[1])
    iii = int(code[2])
    iv = int(code[3])

    ## calculate check digit (mod11)
    chkDigit = 11 - (( i*5 + ii*4 + iii*3 + iv*2 ) % 11 )

    ## check if check digit is 10 or 11 and replace them with x and 0
    if chkDigit == 10:
        code = code+"X"
    elif chkDigit == 11:
        code = code+"0"
    else:
        code = code+str(chkDigit)

    return code
   
## Check if check digit of parking number is valid
def checkCode(code):
    ## seperate the check digit
    chkDigit = code[4]
    code = code[:-1:]
    
    ## seperate the digits
    i = int(code[0])
    ii = int(code[1])
    iii = int(code[2])
    iv = int(code[3])
    
    ## assign value of check digit
    if chkDigit == "X" or chkDigit == "x":
        v = 10
    elif chkDigit == "0":
        v = 11
    else:
        v = int(chkDigit)
    
    ## check the check digit
    if (( i*5 + ii*4 + iii*3 + iv*2 + v*1 ) % 11 ) == 0:
        return True
    else:
        return False

## get parking number from user and check it
def getCode():
	## ask user if they want to enter a Parking Number
	while True:
		choice = input("Do you have a Parking Number? [y/n]: ")
		try:
			choice = distutils.util.strtobool(choice)
			break;
		except:
			print("Please answer in yes or no only.")
	
	if choice == 1:
		while True:
			code = input("Enter your five digit Parking Number: ")
			try:
				## get parking number again if not of 5 digits
				if len(code) == 5:
					## get parking number again if first four digits are not number
					if code[:-1:].isdigit():
						## get parking number again if check digit don't contain 0-9 or x
						if code[4] in ( "0", "2", "3", "4", "5", "6", "7", "8", "9", "x", "X" ):
							return code
						else:
							print("Last digit of Parking Number should be a valid mod11 check digit")
							return Error
					else:
						print("First four digits of Parking Number should only contain numbers.")
						return Error
				else:
					print("Parking Number should contain five digits only.")
					return Error
			except:
				pass
	else:
		return False

## Get day from user (day)
def getDay():
	print("""
1) Monday
2) Tuesday
3) Wendesday
4) Thursday
5) Friday
6) Saturday
7) Sunday
	""")
	while True:
		choice = input("Enter the day number: " )
		## check if input is in range and a integer
		try:
			choice = int(choice)
			if choice in range(1,8):
				return choice
			else:
				return Error
		except:
			print("Chose valid day from list only")

		
## Get arrival hour from user (arrivalTime)
def getTime():
	while True:
		choice = input("Enter hour of arrival: ")
		try:
			choice = int(choice)
			if choice in range(24):
				if choice not in range(8):
					return choice
				else:
					print("Sorry but you can't park between midnight and 8am")
					return False
			else:
				return Error
		except:
			print("Enter valid hour only")

## get number of hours person wants to stay (timePre16 for 8am to 4pm
##											 timePost16 for 4pm onwards)
def getHours(day, arrivalTime):
	choice = int(input("Enter the ammount of time you want to stay: "))
	
	if day in (1,2,3,4,5):
		## if he arrives between 8am and 2pm, he can only stay for 2 hours
		if arrivalTime > 7 and arrivalTime < 14:
			while choice > 2:
				print("Sorry but you can't park for more than two hours")
				choice = int(input("Enter the ammount of time you want to stay: "))
			
			timePre16 = choice
			timePost16 = 0
		## if he arrives between 2pm and midnight, he can stay for 10 hours at max (all the time)
		## because 2pm to 4pm is 2 hours, and after that they can stay till midnight
		elif arrivalTime >= 14 and arrivalTime < 24:
			while arrivalTime+choice > 24:
				print("Sorry but you can't stay past midnight")
				choice = int(input("Enter the ammount of time you want to stay: "))
							
			if arrivalTime >= 16:
				timePre16 = 0
				timePost16 = choice																
			elif arrivalTime < 16:
				timePre16 = 16 - arrivalTime
				timePost16 = choice - timePre16
				
	elif day == 6:
		## if he arrives between 8am and 12 noon, he can only stay for 4 hours
		if arrivalTime > 7 and arrivalTime < 12:
			while choice > 4:
				print("Sorry but you can't park for more than four hours")
				choice = int(input("Enter the ammount of time you want to stay: "))
			
			timePre16 = choice
			timePost16 = 0
		## if he arrives between 12 noon and midnight, he can stay for 12 hours at max (all the time)
		## because 12 noon to 4pm is 4 hours, and after that they can stay till midnight
		elif arrivalTime >= 12 and arrivalTime < 24:
			while arrivalTime+choice > 24:
				print("Sorry but you can't stay past midnight")
				choice = int(input("Enter the ammount of time you want to stay: "))

			if arrivalTime >= 16:
				timePre16 = 0
				timePost16 = choice																
			elif arrivalTime < 16:
				timePre16 = 16 - arrivalTime
				timePost16 = choice - timePre16
	else:
		## if he arrives between 8am and midnight, he can stay for 16 hours at max (all the time)
		## because 8am to 4pm is 8 hours, and after that they can stay till midnight
		while arrivalTime+choice > 24:
			print("Sorry but you can't stay past midnight")
			choice = int(input("Enter the ammount of time you want to stay: "))
		
		if arrivalTime >= 16:
			timePre16 = 0
			timePost16 = choice																
		elif arrivalTime < 16:
			timePre16 = 16 - arrivalTime
			timePost16 = choice - timePre16
				
	return timePre16, timePost16
	
## calculate cost based on time and day		
def calCost(day, timePre16, timePost16):
	if timePost16 == 0:
		costPost16 = 0
	else:
		costPost16 = 2
		
	if day in (1,2,3,4,5):
		costPre16 = timePre16 * 10
	elif day == 6:
		costPre16 = timePre16 * 3
	else:
		costPre16 = timePre16 * 2
		
	return costPre16, costPost16

## calculate discount on before and after 4pm cost, if parking number is valid (discount is True)
def calDiscount(discount, costPre16, costPost16):
	if discount is False:
		## no discount
		discountPre16 = 0.0
		discountPost16 = 0.0
	else:
		## 10% discount on arrival before 4pm
		discountPre16 = costPre16 * 0.1
		## 50% discount on arrival after 4pm
		discountPost16 = costPost16 * 0.5
	
	return discountPre16, discountPost16
	
## get payed from user
def payPrice(day, totalPrice):
	global totalDay1, totalDay2, totalDay3, totalDay4, totalDay5, totalDay6, totalDay7
	
	while True:
		payed = input("Please enter the ammount you would pay. (Warning, no change is returned): ")
		try:
			payed = float(payed)
			if payed >= totalPrice:
				if day == 1:
					totalDay1 += payed
				elif day == 2:
					totalDay2 += payed
				elif day == 3:
					totalDay3 += payed
				elif day == 4:
					totalDay4 += payed	
				elif day == 5:
					totalDay5 += payed						
				elif day == 6:
					totalDay6 += payed			
				elif day == 7:
					totalDay7 += payed
				break;
			else:
				print("You can't pay less!")
		except:
			print("Please input valid ammount: ")

def main():
	print("Welcome to Car Park Payment Simulation 2020\n")
	
	while True:
		## ask if customers are availabel
		## this is done to simulate end of day total printing
		customersAvail = input("Are there any customers? [y/n]: ")
		try:
			customersAvail = distutils.util.strtobool(customersAvail)
			if customersAvail == 1:
				## ask user for day
				print("\nPlease select the day from the list:")
				day = getDay()
				#print("\n")
				## ask for time
				arrivalTime = getTime()
				## if it is between midnight and 8am, skip everything as parking in those hours is not allowed
				if arrivalTime == False:
					pass
				else:
					## get the ammount of time they will stay before and after 4pm
					timePre16, timePost16 = getHours(day, arrivalTime)
					## ask for parking number
					code = getCode()
					## if no parking number, no discount
					if code == False:
						discount = False
					else:
						## verify the checkdigit of parking number
						codeValid = checkCode(code)
						if codeValid is False:
							print("Your Parking Number could not be verified.\nNo discount will be given.")
							discount = False
						else:
							print("Parking Number verified.")
							discount = True
					
					## calculate costs based on day and time before and after 4pm		
					costPre16, costPost16 = calCost(day, timePre16, timePost16)
					## calculate discount if available on costs
					discountPre16, discountPost16 = calDiscount(discount, costPre16, costPost16)
					
					## calculate total cost
					totalCost = costPre16 + costPost16
					## calculate total discount
					totalDiscount = discountPre16 + discountPost16
					## calculate total price
					totalPrice = (costPre16 - discountPre16) + (costPost16 - discountPost16)
					
					print("------------------")
					print("Total Cost: ", totalCost)
					print("Total Discount: ", totalDiscount)
					print("Total Ammount payable: ", totalPrice)
					print("------------------")
					
					## ask user to pay			
					payPrice(day, totalPrice)
					
					print("------------------")
					print("Thanks for stopping by, have a nice Day")
					
					## give user a parking number for use next time
					if discount == False:
						code = genCode()
						print("Next time, you can use this Parking Number for discoun: ", code, "\n------------------")
					else:
						pass
			else:
				## when no customers are there, print the totals of each day
				print("------------------")
				print("Here is the total of payments")
				print("Monday: ", totalDay1)
				print("Tuesday: ", totalDay2)
				print("Wendesday: ", totalDay3)
				print("Thursday: ", totalDay4)
				print("Friday: ", totalDay5)
				print("Saturday: ", totalDay6)
				print("Sunday: ", totalDay7)
				break;
				
		except:
			print("Please answer in yes or no only.")

#main()
