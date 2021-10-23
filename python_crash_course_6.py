username = {
    'full_name' : 'XinyangFeng',
    'first_name' : 'Xinyang',
    'family_name' : 'Feng',
    }

for key, value in username.items():
    print("\nKey: " + key)
    print("Value: " + value)

help(dict.items)

favorite_language = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
    }

friends = ['phil', 'sarah']
for name in favorite_language.keys():
    print(name.title())
    if name in friends:
        print("Hi " + name.title() + ", I see your favorite language is " +
        favorite_language[name].title() + "!")

for name in sorted(favorite_language.keys()):
    print(name.title() + ", thank you for taking the poll.")

for language in set(favorite_language.values()):
    print(language.title())

favorite_languages = {
    'jen' : ['python', 'ruby'],
    'sarah' : ['c'],
    'edward' : ['ruby', 'go'],
    'phil' : ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())


cargo = {
    'animal' : 'cat',
    'owner' : 'jason',
    }

sift = {
    'animal' : 'dog',
    'owner' : 'watase',
    }

pets = [cargo, sift]

for pet in pets:
    print("This is a " + pet['animal'] + 
    ", and it's owner is " + pet['owner'].title())
    


















