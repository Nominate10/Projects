cost = input("Enter price: ")
payment = input("Enter payment: ")

change = payment-cost



if change < 0:
	print("Insufficient funds. "+str(cost-payment)+" more needed.")
else:
	# calculate change
	dollars = 0
	quarters = 0
	dimes = 0
	nickels = 0
	pennies = 0

	change = int(change * 100)

	if change >= 100:
		dollars = change/100
		change = change %100
	if change >= 25:
		quarters = change/25
		change = change%25
	if change >= 10:
		dimes = change/10
		change = change%10
	if change >= 5:
		nickels = change/5
		change = change%5
	if change >= 1:
		pennies = change

	print("Your change is:")
	print("Dollars: %d / Quarters: %d / Dimes: %d / Nickels: %d / Pennies: %d" % (dollars, quarters, dimes, nickels, pennies))