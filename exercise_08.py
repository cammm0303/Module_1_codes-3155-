# Cameron Dennis Exercise 8

#Here we import and create the arrays:
import sys
List_all = []
List_multi = []

#make the inital Original list first:
for i in range(1,11):
    num = input('Enter number '+ str(i) + ' : ')
    num = int(num)

    List_all.append(num)

#Then we check the occurence of each element and make sure its not allready in the MUlti list.
#Then add that number to the multi list =:
for j in List_all:
    if List_all.count(j) > 1 and List_multi.count(j) == 0:
        List_multi.append(j)
            


#print the lists:      
print('Original List:',  List_all)
print('Nums that appear more than once:', List_multi)
