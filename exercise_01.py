# Cameron Dennis Exercise 1 

Grade1 = input('Enter a Grade from 1-100 ')
print('Entered: ' + Grade1)
#Changes the input from string to int:
Grade1 = int(Grade1)
#Checks if the number is too large or small:
if int(Grade1) > 100 or int(Grade1) < 0:
    {
        print('Grade value is out of bounds!')
    }
#Checks for grade using the bottom end of the Scale
else :
        if Grade1 < 60:
            print('Final letter grade: F')
        elif Grade1 < 70:
            print('Final letter grade: D')
        elif Grade1 < 80:
            print('Final letter grade: C')
        elif Grade1 < 90:
            print('Final letter grade: B')
        elif Grade1 <= 100:
            print('Final letter grade: A')










