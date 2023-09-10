# Cameron Dennis Exercise 5

import sys
List_x = []
List_y = []
List_z = []

#Gather inputs and create a array outside forloops:
#populate the first/second array:
for i in range(5):
    x = input('Enter Number '+ str(i+1)+ ' For List 1: ')
    List_x.append(x)

for i in range(5):
    y = input('Enter Number '+ str(i+1)+ ' For List 2: ')
    List_y.append(y)


#We forloop through both arrays to find matches and dumps them into a third array (List_z) 
# if there is one that maches 
#since 'i' iterrates through once we'll use that to midigate mistakes:
for i in List_x:
    for j in List_y:
        if int(i) == int(j):
            List_z.append(i)

#Print to console:
print('List 1: '+ str(List_x))
print('List 2: '+ str(List_y))
print('Common List: '+ str(List_z))