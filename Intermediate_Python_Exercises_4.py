import sys
#Cameron Dennis 
#Looked up how to use try/catches in python

#Count makes sure that we know how many ints to take in and what the total sum is:
total = 0
count = 1

#Loops until 5 ints are taken 
while count <= 5:
   
   intInput = input("Please enter int " + str(count)+ ": " )
   
   #Check if input is an int
   try:
      val = int(intInput)
      total += val
      count += 1
    #Display the error message if input is not an int
   except ValueError:
      print("Error! Please enter a valid int.")

print("The total sum is: "  + str(total))