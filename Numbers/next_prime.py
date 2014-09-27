print 'Prime Number Finder:'
num = 2
primes = []
while True:
  for div in range(1,num):
    if div != 1 and div != num:
      if num % div == 0: # is not prime
        num += 1
        continue
  print str(num) + ' is prime.'
  primes.append(num)
  
  
  # i feel like theres a simpler way to do this...
  keepGoing = raw_input("Would you like to keep going? (y/n) ")
  while True:
    if keepGoing == 'y' or keepGoing == 'yes':
      keepGoing = True
      break
    elif keepGoing == 'n' or keepGoing == 'no':
      keepGoing = False
      break  # out of the loop
    else:
      keepGoing = raw_input('Please reply with yes or no. ')
  if keepGoing:
    print '\n'
    num += 1
    continue
  else:
    break

strPrimes = ""
for n in primes:
  strPrimes = strPrimes + str(n) + "\t"
print "Here's all the prime numbers that were found: "
print strPrimes