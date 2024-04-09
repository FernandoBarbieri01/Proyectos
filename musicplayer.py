#import vlc

from playsound import playsound

def play_song(song_name):
    playsound(song_name)

def main():
    print("Please choose a song to play:")
    print("1. Song 1")
    print("2. Song 2")
    print("3. Song 3")
    print("4. Song 4")
    print("5. Song 5")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        play_song("son1.mp3")
        input()
    elif choice == "2":
        play_song("song2.mp3")
    elif choice == "3":
        play_song("song3.mp3")
    elif choice == "4":
        play_song("song4.mp3")
    elif choice == "5":
        play_song("song5.mp3")
    else:
        print("Invalid choice")

    print("Song Over")

if _name_ == "_main_":
    main()