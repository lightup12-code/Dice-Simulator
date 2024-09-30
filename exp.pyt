import tkinter as tk
from PIL import Image, ImageTk
import random

window = tk.Tk()
window.geometry("500x360")
window.title("Dice Roll")
# add location of the image of the dice in place of "E:/"
dice = ["E:/dice1.png","E:/dice2.png","E:/dice3.png","E:/dice4.png","E:/dice5.png","E:/dice6.png"]
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1 = tk.Label(window,image=image1)
label2 = tk.Label(window,image=image2)

label1.image = image1
label2.image = image2

label1.place(x=100,y=100)
label2.place(x=300,y=100)

def dice_roll():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image = image1)
    label1.image = image1

    image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label2.configure(image = image2)
    label2.image = image2
button = tk.Button(window,text="ROLL",bg = "grey", fg="white",font="Time 15 bold", command=dice_roll)
button.place(x=220,y=10)

window.mainloop()