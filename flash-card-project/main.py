# ---------------------------------------------- MODULES & CONSTANTS ------------------------------------------------- #
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
# ---------------------------------------------------- LOAD DATA ----------------------------------------------------- #
try:
    new_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/japanese_vocab.csv")
    word_dict = data.to_dict(orient="records")
else:
    word_dict = new_data.to_dict(orient="records")
word = {}
flip = 0

# ---------------------------------------------------- FUNCTIONS ----------------------------------------------------- #

def word_generator():
    global word, flip
    word = random.choice(word_dict)
    hiragana = word["Hiragana"]
    category1 = word["Category"]
    if pandas.isna(word["Tic"]):
        tic = ""
    else:
        tic = word["Tic"]
    canvas_front.itemconfig(word_canvas, text = hiragana, fill = "black")
    canvas_front.itemconfig(title_canvas, text="Japanese", fill="black")
    canvas_front.itemconfig(category_canvas, text=f"Category: {category1}", fill="black")
    canvas_front.itemconfig(img_canvas, image=card_front)
    canvas_front.itemconfig(tic_canvas, text = tic)
    flip = 1

def card_flip():
    global word, flip
    meaning = word["Meaning"]
    hiragana = word["Hiragana"]
    pronunciation = word["Pronunciation"]
    category1 = word["Category"]
    if flip > 0:
        canvas_front.itemconfig(title_canvas, text = "English", fill = "white")
        canvas_front.itemconfig(img_canvas, image = card_back)
        canvas_front.itemconfig(word_canvas, text=meaning, fill="white")
        canvas_front.itemconfig(category_canvas, text=f"Pronunciation: {pronunciation}", fill="white")
    elif flip < 0:
        canvas_front.itemconfig(word_canvas, text=hiragana, fill="black")
        canvas_front.itemconfig(title_canvas, text="Japanese", fill="black")
        canvas_front.itemconfig(img_canvas, image=card_front)
        canvas_front.itemconfig(category_canvas, text=f"Category: {category1}", fill="black")
    flip *= -1

def correct_guess():
    global word
    try:
        len(word["Tic"])
    except TypeError:
        streak = 1
    else:
        streak = len(word["Tic"]) + 1


    word["Tic"] = streak * "✔"
    new_data1 = pandas.DataFrame(word_dict)
    new_data1.to_csv("data/words_to_learn.csv", index= False)
    word_generator()

def wrong_guess():
    global word
    word["Tic"] = ""
    new_data1 = pandas.DataFrame(word_dict)
    new_data1.to_csv("data/words_to_learn.csv", index=False)
    word_generator()

# ---------------------------------------------------- UI SETUP ------------------------------------------------------ #
window = Tk()
window.config(pady=50, padx=50, bg= BACKGROUND_COLOR)
window.title("Flash Cards")

card_front = PhotoImage(file= "images/card_front.png")
card_back = PhotoImage(file= "images/card_back.png")

canvas_front = Canvas(width=800, height=526, highlightthickness= 0, background=BACKGROUND_COLOR)
img_canvas = canvas_front.create_image(400, 263, image = card_front)
title_canvas = canvas_front.create_text(400, 150, text="Japanese", font= ("Arial", 40, "italic"))
word_canvas = canvas_front.create_text(400, 263, text="Word", font=("Arial", 60, "bold"), width=750)
category_canvas = canvas_front.create_text(400, 390, text = "Category", font= ("Arial", 40, "italic"), width = 750)
tic_canvas = canvas_front.create_text(400, 450, text= "", font= ("Arial", 20, "italic"), fill= "green")
canvas_front.grid(row=0, column=0, columnspan= 3)

right_img = PhotoImage(file= "images/right.png")
wrong_img = PhotoImage(file= "images/wrong.png")
flip_img = PhotoImage(file="images/flip_card.png")

right_btn = Button(image= right_img, highlightthickness= 0, command=correct_guess)
right_btn.grid(row= 1, column= 2)
wrong_btn = Button(image= wrong_img, highlightthickness= 0, command=wrong_guess)
wrong_btn.grid(row=1, column= 0)
flip_btn = Button(image= flip_img, highlightthickness= 0, command=card_flip)
flip_btn.grid(row=1, column=1)

window.bind("a", lambda event: wrong_guess())
window.bind("s", lambda event: card_flip())
window.bind("d", lambda event: correct_guess())
word_generator()


window.mainloop()
