# Cameron Dennis Exercise 3 

#Gather inputs:

Cube_x = input("Enter an integer greater than 1: ")

#Change to int
Cube_x = int(Cube_x)

#Run through the loops with the varible i increasing and being cubed each time:
for i in range(Cube_x+1):
    print('The Cube of '+ str(i) + ' is: '+ str(i**3))

