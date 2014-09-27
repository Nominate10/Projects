from random import randint


heads, tails = 0, 0



print '\t---Coin Flip Simulator---\n'

flips = int(raw_input("How many times would you like to flip the coin?\n>"))

for x in range(0,flips):
  flip = randint(0, 1)
  if flip == 1:
    heads += 1
  if flip == 0:
    tails += 1

print '  Heads: ' + str(heads) + '\t  Tails: ' + str(tails)