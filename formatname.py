#defines the list and adds a place holder varible as the append function will delete the first variable
des = ['0']
#initilizing integers
total_names = 0
count = 1
#main loop used to input names into the list
while True:
    #input from the user of listed name
    user = input("Enter the list of names ")
    #checks to see if the input is blank and if so exits the loop
    if user == "Enter the list of names ":
       break
    elif user != '':
        #adds the user input to the list
        des.append(user)

#locating the total count for list
total_names = len(des)
#formating the script output
print('')
print('conf t')
#the next loop to run through the list
for name in des:
    if count == total_names:
        #print statement use to ID that the loop has finished
        print('Done!')
        break

    elif count < total_names:
        #More formatting of the output
        print('int ', count)
        print('name', des[count])
        count = count + 1