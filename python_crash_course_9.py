# class Restuarant():
#     '''Restuarant Information'''

#     def __init__(self, restuarant_name, cuisine_type):
#         # initialize restuarant name and cuisine type
#         self.restuarant_name = restuarant_name
#         self.cuisine_type = cuisine_type

#     def describe_restuarant(self):
#         print(self.restuarant_name + " is famous for " + self.cuisine_type + " food.")

#     def open_restuarant(self):
#         print(self.restuarant_name + " is now open.")


# bistro = Restuarant("Buddha Bar", "casual")
# bistro.describe_restuarant()
# bistro.open_restuarant()


# class User():
#     '''User information'''

#     def __init__(self, first_name, last_name):
#         # initialize user's name and other information
#         self.first_name = first_name
#         self.last_name = last_name
    
#     # def describe_user(self):
#     #     # provide a summary of the user
#     #     profile = {}
#     #     profile["first name"] = self.first_name
#     #     profile["last name"] = self.last_name
#     #     return profile
    
#     def greet_user(self):
#         print("Hello " + self.first_name + "!")


# Xinyang = User("Xinyang", "Feng")
# # Xinyang.describe_user()
# Xinyang.greet_user()

class Car():
    '''A simple attempt to represent a car'''

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + "miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery():
    '''A simple attempt to model a battery for an electric car.'''

    def __init__(self, battery_size=70):
        '''Initialize the battery's attributes.'''
        self.battery_size = battery_size

    def describe_battery(self):
        '''Print a statement describing the battery size.'''
        print("This car has a " + str(self.battery_size) + "-kwh battery.")


class ElectricCar(Car):
    '''Represent aspects of a car, specific to electric vehicles.'''
    def __init__(self, make, model, year):
        '''Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        '''
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()















































