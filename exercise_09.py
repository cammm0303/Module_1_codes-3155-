# get the input from the user
input_string = input("Enter a string: ")

# split the string into a list of single characters / initialize a list for the outer list
char_list = list(input_string)
outer_list = []

# loop through the list of characters and add each 3 of them to the inner lists and append the inner list to the outer list
while len(char_list) != 0:
    
    sub_list = char_list[:3]

    outer_list.append(sub_list)

    char_list = char_list[3:]

# print the outer list
print(outer_list)