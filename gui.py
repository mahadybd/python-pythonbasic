from cProfile import label
import tkinter
from random import randint
from tkinter import messagebox

low = 0
high = 20
rand = randint(low, high)
print(rand)

def check(guess):
    if guess < rand:
        tkinter.Label(tk, text = f"{guess} is too low").pack()
    elif guess > rand:
        tkinter.Label(tk, text = f"{guess} is too high").pack()
    else:
        tkinter.messagebox.showinfo("You Win" f"{guess} is currect")

tk = tkinter.Tk()
tk.title("Guessing Game")

label = tkinter.Label(tk, text=f"Guess a number {low} to {high} (inclusive)")
label.pack()

entry = tkinter.Entry(tk)
entry.pack()

button = tkinter.Button(tk, text="Guess", command=lambda: check(int(entry.get())))
button.pack()


tk.mainloop()