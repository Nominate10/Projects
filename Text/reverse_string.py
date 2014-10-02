string = raw_input("Enter the string you'd like to reverse:\n>")


newStr = ""
for i in range(len(string), 0, -1):
  newStr = newStr + string[i-1]
  
print newStr