responses = {}

# Set a flag to indicate that polling is active
polling_active = True

while polling_active:
    # Prompt for the person's name and response
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb someday?")

    # store the response in a dictionary:
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
    
# Polling is complete. Show the results.
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")

# 2
sandwich_orders = ['tuna', 'seafood', 'egg', 'roast beef', 'ham']
finished_sandwiches = []

while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print("I made your " + finished_sandwich + " sandwich.")
    finished_sandwiches.append(finished_sandwich)

print("\nThe following sandwiches have been made.")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)


# 3
sandwich_orders = ['tuna', 'pastrami', 'pastrami','seafood', 'pastrami', 'egg', 'roast beef', 'ham']
print("Deli has run out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

for sandwich in sandwich_orders:
    print(sandwich)


# 4
dream_vacation = {}

state = True

while state:
    # ask the poller's name and his/her dreamed vacation place.
    name = input("\nWhat is your name?")
    place = input("Please enter one of your dream vacation places.")

    # store the name and the associated place in dream_vacation
    dream_vacation[name] = place

    # ask the poller if he/she want someone else to take part in the poll.
    # if the answer is yes, the loop continues, otherwise the loop ends.
    next_poll = input("\nWould you like someone else to take the poll? (yes / no) ")
    if next_poll == 'no':
        state = False

# when someone ends the input, show the information stored in dream_vacation
for name, vacation in dream_vacation.items():
    print("Name: " + name.title())
    print("Dreamed vacation place: " + vacation.title())




















