total = 0 # the end-total of all the even-valued terms

pastX = 1
currX = 1 # the current number to test
while currX <= 4000000:
    if currX%2 == 0: #check if even
        total = total + currX
    
    currX, pastX = currX + pastX, currX # step
    
print total