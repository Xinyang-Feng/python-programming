# define a function to store city and country names
# store this function in a file called city_functions.py

def city_info(city, country):
    print("The city " + city + " is in " + country + ".")


# create a test function to test if city_info functions well
import unittest # import the defualt test module in python
from city_functions import city_info # import the function we are going to test

class CityInfoTest(unittest.TestCase):
    '''Test for city_functions.py'''

    def test_city_country(self):
        """Do names like 'Beijing China' work?"""
        formatted_sent = city_info('Beijing', 'China')
        self.assertEqual(formatted_sent, "The city Beijing is in China.")


unittest.main()


help(unittest.TestCase.setUp)














