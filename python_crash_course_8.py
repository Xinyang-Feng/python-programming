# 1
def make_album(artist, album, num_of_tracks = ""):
    '''Return an album's information'''

    album_info = {"artist name" : artist,
                  "album name" : album,}           
    if num_of_tracks:
        album_info["number of tracks"] = int(num_of_tracks)
    return album_info
    
    
# musician1 = make_album("Slayer", "Angel of death")
# musician2 = make_album("Megadeth", "Holy wars, the punishment due", 2)
# print(musician1)
# print(musician2)


# 2
state = True
while state:
    artist1 = input("\nWrite your favorite band's name")
    album1 = input("Write your favorite song of this band")
    print(make_album(artist1, album1))
    proceed_question = input("Do you want to write information of another your favorite band? (yes / no)")
    if proceed_question == "no":
        state = False


magicians = ["Mike", "Kobe", "Zion"]
def show_magicians(names):
    for name in names:
        print(name)

show_magicians(magicians)
        
copy_magicians = magicians[:]
def make_great(names):
    for name in names:
        name = "the Great " + name
        print(name)


def ordered_sandwich(*ingredient):
    print("\nThese are the sandwiches you have just ordered.")
    for i in ingredient:
        print(i + " Sandwich")

ordered_sandwich("tuna", "roast beef", "cheese")






















