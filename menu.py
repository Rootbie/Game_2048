import pickle
from tkinter import *
from tkinter.messagebox import *
from intro import Intro
from Games.Client.Client_View import Client_View
import os

class Menu:
    def __init__(self, window):
        self.__window = window
        
        self.playBtn = Button(self.__window, text=' Play ', command=self.login, width=20)
        self.playBtn.pack(side=TOP, padx=5, pady=5)
        
        self.htpBtn = Button(self.__window, text=' How to play ', command= self.howToPlay, width=20)
        self.htpBtn.pack(side=TOP, padx=5, pady=5)
        
        self.quitBtn = Button(self.__window, text=' Quit ', command=self.exit ,width=20)
        self.quitBtn.pack(side=TOP, padx=5, pady=5)


    def login(self):
        with open("./Database/data_nick.dat", "wb") as write_profile:
            pickle.dump( {},write_profile)
            write_profile.close()

        system = os.name
        if system == 'nt':
            com = 'python ./Games/Client/List_User.py '
        elif system == 'posix':
            com = 'python3 ./Games/Client/List_User.py '
        os.system(com)
        
        with open("./Database/data_nick.dat", "rb") as user_profile:
            profile = pickle.load(user_profile)
            username = ''
            if 'username' in profile:
                username = profile['username']
            user_profile.close()

        if username != '':
            self.playBtn.pack_forget()
            self.htpBtn.pack_forget()
            self.quitBtn.pack_forget()
            Client_View(self.__window)


    def howToPlay(self):
        showinfo("How to play", "How to play: Use your W, A, S, D keys with your fingers to move the tiles. Tiles with the same number merge into one when they touch. Add them up to reach 2048!")

    def exit(self):
        if askyesno('Quit', 'Do you want to quit?'):
            self.__window.quit()
            

if __name__ == "__main__":
    window = Tk()
    window.title("2048")
    window.config(bg="#57407C")
    window.iconbitmap("2048_logo.ico")
    window.resizable(False, False)
    window.geometry('+500+20')

    Intro(window)
    Menu(window)
    window.mainloop()
