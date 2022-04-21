from tkinter import *
from PIL import Image, ImageTk, ImageSequence

class Intro:
    def __init__(self, parent):
        self.parent = parent
        self.canvas = Canvas(parent, width=500, height=500)
        self.canvas.pack()
        self.sequence = [ImageTk.PhotoImage(img)
                            for img in ImageSequence.Iterator( Image.open('2048.gif'))]
                                    
        self.image = self.canvas.create_image(0,0, anchor=NW , image=self.sequence[0])
        self.animate(1)

    def animate(self, counter):
        self.canvas.itemconfig(self.image, image=self.sequence[counter])
        self.parent.after(54, lambda: self.animate((counter+1) % len(self.sequence)))
