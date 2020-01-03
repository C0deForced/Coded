reflist = {}
Items_to_search = []
while True:
    user = input("Enter the device info ")
    if user == "Enter the device info ":
        break
    elif user != '':
        user = user.split()
        reflist[(user[0])] = user[1]
    else:
        break

while True:
    user = input("Enter things to search ")
    if user == "Enter things to search ":
        break
    elif user != '':
        Items_to_search.append(user)
    else:
        break

for key in Items_to_search:
    x = reflist.get(key)

    print(key, x)
else:
    print("Done!")
