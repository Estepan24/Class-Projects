import time
import vlc

songs = {
    "1": ("Trueno - TRANKY FUNKY", "TRANKY FUNKY.mp3"),
    "2": ("Canserbero - Jeremías 17-5", "Jeremías 17-5.mp3"),
    "3": ("Hers - What Once Was", "What Once Was.mp3"),
    "4": ("Fox Stevenson - Get Through", "Get Through.mp3"),
    "5": ("Blur - Song 2", "Song 2.mp3")
}

def play_stop(user_input):
    if user_input in songs:
        song_name, file_name = songs[user_input]
        print(f"Playing: {song_name}")
        media = vlc.MediaPlayer(file_name)
        media.play()
        time.sleep(5)  # Play for 5 seconds
        media.stop()
    else:
        print("It's not a valid song!")

user_input = input("What song do you want to play? (1-5): ")
play_stop(user_input)

