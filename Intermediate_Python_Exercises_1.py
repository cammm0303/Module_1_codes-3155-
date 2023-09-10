import sys
#Cameron Dennis 
#Creates the new List:
list_all = []

#Function Def:
#This takes in the list and filters the new numbers into new_list
def unique_list(data):
            new_list = []
            for item in data:
                if item not in new_list:
                    new_list.append(item)
            return new_list

#Function to be able to mak your own list to add to the Unique_list method:
while input != 'S':
    inputs = input("Enter a number to include in the list: *Enter S to Stop*")
    if inputs == "S":
        print (unique_list(list_all))
        break
    else:
          list_all.append(int(inputs))


        
        


    

