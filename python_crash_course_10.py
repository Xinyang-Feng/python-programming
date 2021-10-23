# # combine the above two programmes
# import json

# def greet_user():
#     # Load the user name, if it has been stored previously
#     # Otherwise, prompt for the username and store it.
#     filename = 'username.json'
#     try:
#         with open(filename) as f_obj:
#             username = json.load(f_obj)
#     except FileNotFoundError:
#         username = input("What is your name?")
#         with open(filename, 'w') as f_obj:
#             json.dump(username, f_obj)
#             print("We will remember when you come back, " + username + "!")
#     else:
#         print("Welcome back, " + username + "!")


# greet_user()


# exercise
import json

def store_num():
    '''Ask the user's favorite number and store it in a file'''
    num_stored = input("What is your favorite number?")
    with open(num_stored, 'w') as f_obj:
        json.dump(num_stored, f_obj)
    return num_stored

def favorite_num():
    '''report the favorite number to the user'''
    # read the user's favorite number from num_stored.json
    num_stored = store_num()
    try:
        with open(num_stored) as f_obj:
            favorite_num = json.load(f_obj)
    # if the file does not exsit, call store_num() to prompt user to enter a number and store it  
    except:
        store_num()
    # if the try block works, load the number and print it
    else:
        print("Your favorite number is: ", + str(favorite_num) + "!")




































































