import tkinter as tk
from PIL import Image, ImageTk
import random

root = tk.Tk()
root.geometry('400x400')
root.title("PythonGeeks - Roll the Dice")

dice = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']

# Load initial image
initial_image = ImageTk.PhotoImage(Image.open(random.choice(dice)))
label1 = tk.Label(root, image=initial_image)
label1.image = initial_image
label1.pack(expand=True)

def rolling_dice():
    # Load a new random image
    new_image = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # Update the label with the new image
    label1.configure(image=new_image)
    label1.image = new_image

button = tk.Button(root, text="Roll the dice", fg="green", command=rolling_dice)
button.pack(expand=True)

root.mainloop()
