from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"

# list for sharing card across functions
current_card = {}
# list that only includes all but correctly guessed cards to be repeated
to_learn = {}

# check if a file for all but correctly guessed cards exists. If not, creates one
# prevents alteration of primary data file
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/mandarin_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# when clicking on the buttons, flips the card back to starting side, chooses a new card and starts timer again
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(flashcard_img, image=flashcard_front)
    canvas.itemconfig(card_title, text="Mandarin", fill="black")
    canvas.itemconfig(card_word, text=current_card["Simplified"], fill="black")
    canvas.itemconfig(pinyin_label, text=current_card["Pinyin"], fill="black")
    flip_timer = window.after(3000, func=flip_card)


# after timer goes off, flips to answer side and fills with English translation
def flip_card():
    global current_card
    canvas.itemconfig(flashcard_img, image=flashcard_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(pinyin_label, text="")

# removes a correct guess from data and saves data to csv
# called from right button
# also calls next_card function
def right_card():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# setup window and timer
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# import images
flashcard_front = PhotoImage(file="images/card_front.png")
flashcard_back = PhotoImage(file="images/card_back.png")
right_check = PhotoImage(file="images/right.png")
wrong_x = PhotoImage(file="images/wrong.png")

# size and positioning of images, text, buttons
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flashcard_img = canvas.create_image(800/2, 526/2, image=flashcard_front)
card_title = canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"))
card_word = canvas.create_text(400, 300, text="", font=(FONT_NAME, 60, "bold"))
pinyin_label = canvas.create_text(400, 380, text="", font=(FONT_NAME,28, "normal"))
canvas.grid(row=0, column=0, columnspan=2)

# right (correct answer) button calls right_card function
right_button = Button(image=right_check, highlightthickness=0, command=right_card)
right_button.grid(row=1, column=1)

# wrong answer button calls next_card function
wrong_button = Button(image=wrong_x, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

# first instance
next_card()


window.mainloop()


