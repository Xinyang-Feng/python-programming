usernames = ['admin', 'Xinyang', 'Jason', 'Kobe', 'Shaq']

'''
for username in usernames:
    name_cache = usernames.pop(0)

A for loop will actually iterate over each item in the list, 
which will not work as the indices in the list will change with 
each deletion, and you will not end up getting all items.

However, a while loop will check a condition every time the loop
is run, and if it is still true, run the code again. Here we specify
that the length of the list has to be more than 0, i.e. there has
to be content in the list.
'''
while len(usernames) > 0:
    usernames.pop(0)

usernames
len(usernames)



current_users = ['admin', 'Xinyang', 'Jason', 'Kobe', 'Shaq']
new_users = ['Tracy', 'Dirk', 'Jason', 'Kobe', 'Michael']

for new_user in new_users:
    if new_user in current_users:
        print("Sorry, this username is currently unavailable.")
    else:
        print("Your username has just been created.")


num_list = list(range(1,10))

for num in num_list:
    if num == 1:
        print(str(num) + "st")
    elif num == 2:
        print(str(num) + "nd")
    elif num == 3:
        print(str(num) + "rd")
    else:
        print(str(num) + "th")












