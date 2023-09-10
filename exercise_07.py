# Cameron Dennis Exercise 7

#Here we import and create the arrays:
import sys
List_all = []
List_even = []

#Set the Answer to string initaily to avoid errors when checking for QUIT first. 
#Then set a while loop to break out of asking for a number when a QUIT is detected.:
answer = ''
while answer != 'QUIT':
    answer = input('Enter Number or QUIT to quit: ')
    if answer == 'QUIT':
        break

#Here after making sure there is not a quit request, we can find the remainder and distingush 
# the evens from the odds:         
    if int(answer) % 2 == 0:
        List_all.append(int(answer))
        List_even.append(int(answer))
    else:
        List_all.append(int(answer))

#Print the arrays:
print('List_all:', List_all)
print('List_even:', List_even)


