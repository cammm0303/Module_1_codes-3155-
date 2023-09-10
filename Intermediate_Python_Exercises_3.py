import sys
#Cameron Dennis 

#Function to check for number of lowercase letters:
def letter_count(string):
    letter_dict = {}
    #Forloop lowers all letters before checking for multiples:
    for char in string.lower():
        #this if statement leaves out spaces:
        if char != " ":
            letter_dict[char] = letter_dict.get(char, 0) + 1
    return letter_dict

#user input and function call:
string = input('Enter a string: ')
letter_dict = letter_count(string)
print(letter_dict)