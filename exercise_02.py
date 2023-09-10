# Cameron Dennis Exercise 2 

#Gathers the strings:
String1 = input('Enter a String ')
String2 = input('Enter a String ')

#Use .__contains__ to check for one word in the other, then print boolean result:
if String2.__contains__(String1) or String1.__contains__(String2):
    print('True')
else:
    print('False')