# String Concatation
def Main():
    print("My Favorite Song\n")
    noun, noun2 = input("Enter a noun: "), input("Enter another noun: ")
    song_name = "Sun and Moon - Anees"
    lyrics = f"{noun.capitalize()}, {noun}, you're my sun and moon \n{noun2.capitalize()}, you're everything between \nA lot of pretty faces could waste my time \nBut you're my dream {noun2} \nYou make flowers bloom \n{noun2.capitalize()}, you make the stars collide \nAnd I don't know what I did to get lucky like this \nBut it sure feels fine...\n"
    print("\nPlaying: {1}... 🎵 \n\n{0}".format(lyrics, song_name))

if __name__ == '__main__':
    Main()