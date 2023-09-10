# Cameron Dennis Exercise 4


import sys
#Gather inputs and create a array outside forloops:

n = int(input("Enter a Number: "))
new_list = []
Average = 0

#Ask and collect numbers and then add them to the array:
for i in range(int(n)):
    x = input('Enter Number '+ str(i+1)+ ' : ')
    new_list.append(x)

#Adds each item to Average to prepare for the divison:
for i in new_list:
    Average += float(i)

#regardless of the number entered the size will be determined after the array is finished being built above
#Then we divide by that size to get the final average. 
#Calc Average 
Average = Average / float(n)

#Print to console:
print('List: '+ str(new_list))
print('Average: '+ str(Average))
