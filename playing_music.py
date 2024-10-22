import pygame
import tkinter as tk
from tkinter import filedialog

# Start the main loop of playing msuic or Pygame function
pygame.mixer.init()

# The menu to choice functions  on song
def play_music():
    pygame.mixer.music.load(current_file)
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def pause_music():
    pygame.mixer.music.pause()

def unpause_music():
    pygame.mixer.music.unpause()

# Choice the music/audio file.
def select_file():
    global current_file
    current_file = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
    if current_file:
        play_music()

# Set fixed window size and background color
root = tk.Tk()
root.title("Playing Songs")
root.geometry("380x450")     
root.configure(bg="#ADD8E6")   

# Define the buttons and their size
btn_open = tk.Button(root, text="Choice a song/file", command=select_file, bg="#FF6347", fg="white", font=("Arial", 14), width=20, height=2)
btn_open.pack(pady=10)

btn_play = tk.Button(root, text="Play :)", command=play_music, bg="#32CD32", fg="white", font=("Arial", 14), width=20, height=2)
btn_play.pack(pady=10)

btn_pause = tk.Button(root, text="Pause!", command=pause_music, bg="#FFD700", fg="black", font=("Arial", 14), width=20, height=2)
btn_pause.pack(pady=10)

btn_unpause = tk.Button(root, text="Continuoue", command=unpause_music, bg="#1E90FF", fg="white", font=("Arial", 14), width=20, height=2)
btn_unpause.pack(pady=10)

btn_stop = tk.Button(root, text="Stop", command=stop_music, bg="#DC143C", fg="white", font=("Arial", 14), width=20, height=2)
btn_stop.pack(pady=10)

# start the mainloop of given instruction 
root.mainloop()