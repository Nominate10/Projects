import math

cost = float(raw_input("Enter the item cost: "))
rate = float(raw_input("Enter the tax rate: "))

totalTax = 0.0

for x in range(0,int(cost)):
  totalTax += rate
  
leftover = cost - int(cost)
totalTax += rate * leftover

totalTax = math.ceil(totalTax*100)/100

print "\nItem cost: " + str(cost)
print "Tax: " + str(totalTax)
print "Total cost: " + str(cost + totalTax)