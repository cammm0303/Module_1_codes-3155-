# Cameron Dennis Exercise 6

#Gather inputs:
Row = input('Enter a Row num from 1 to 5: ')
Col = input('Enter a Column num from 1 to 5: ')

#Cast the inputs as integers:
Row = int(Row)
Col = int(Col)

#Check the range and bounds of the inputs:
if (Row or Col) > 5 or (Row or Col) < 1:
    print('Out of range!')

#Here we first check the range:
else:
    print('\n')
    for r in range(1, 6):

        #Here we iterate through using 1-6 to keep track properly, 
        #also nest the for-loops to make the matrix refering to the coloumn and row iterations, 
        #to check for the index of where to put the '1':
        for c in range(1, 6):
            if r == Row and c == Col:
                print('1 ', end=' ')
            else:
                print('0 ', end=' ')
        print('\n')
    
           

