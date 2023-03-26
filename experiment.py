from PIL import Image, ImageTk
import requests
import json
import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import Label
import random

API_KEY = 'ccc88e97060b44fd87149d75d5ddac0b'
root = tk.Tk()
varGenre = tk.StringVar(root)
varGenre.set("Choose a genre from the drop down below!")
varTag = tk.StringVar(root)
varTag.set("Choose a tag from the drop down below!")
varMetacritic = tk.IntVar(root)
x = random.randint(0,20)

def get_game_by_genre_tag_metacritic(genre, tag, metacritic):
    url = f'https://api.rawg.io/api/games?genres={genre}&page_size=20&page={x}&tags={tag}&min_metacritic={metacritic}&max_metacritic={metacritic}&key={API_KEY}'
    response = requests.get(url)
    data = json.loads(response.text)
    return data['results'][0]


def on_image_click(event):
    global label, genre_dropdown, tag_dropdown, metacritic_slider
    if label is None and genre_dropdown is None and tag_dropdown is None and metacritic_slider is None:
        label = tk.Label(root, text="Select a genre:")
        label.pack()
        label.config(font=("Courier", 24))

        genre_options = ["action", "adventure", "casual", "strategy", "shooter", "racing", "sports", "puzzle"]
        genre_dropdown = tk.OptionMenu(root, varGenre, *genre_options)
        genre_dropdown.pack()
        genre_dropdown.config(font=("Courier", 14))
        
        tag_options = ["singleplayer", "multiplayer", "comedy", "free-to-play", "fantasy", "survival", "controller", "space", "cinematic"]
        tag_dropdown = tk.OptionMenu(root, varTag, *tag_options)
        tag_dropdown.pack()
        tag_dropdown.config(font=("Courier", 14))
        
        label = tk.Label(root, text="Choose '1' for N/A (Slider)")
        metacritic_slider = tk.Scale(root, from_=1, to=100, orient='horizontal', variable=varMetacritic)
        
        
        metacritic_slider.pack()
    x = random.randint(0,20)
    game = get_game_by_genre_tag_metacritic(varGenre.get(), varTag.get(), varMetacritic.get())
    if game:
        messagebox.showinfo("Game Suggestion", game['name'])
    else:
        messagebox.showerror("Error", "Failed to get game information")


label = None
genre_dropdown = None
tag_dropdown = None
metacritic_slider = None


img = PhotoImage(file="presentyeah.png")
panel = tk.Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")


panel.config(width=150, height=150)


gif_path = "new.gif"
gif = Image.open(gif_path)
gif.seek(0) 

def update_gif():
    gif.seek(gif.tell()+1) 
    img = ImageTk.PhotoImage(gif)
    panel.config(image=img)
    panel.image = img
    root.after(40, update_gif) 

root.after(0, update_gif)


def animate():
    
    root.after(1000, animate)

root.after(1000, animate)
panel.bind("<Button-1>", on_image_click)

root.mainloop()