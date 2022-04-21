from tkinter import *
import pickle
from tkinter.messagebox import *
import os

FONT = ("Trebuchet", 20, "bold")
FONT2 = ("Trebuchet", 14, "bold")
BG_CLIENT = "#57407C"
FG_CLIENT = "#EEEBF1"


class Password_Box:
    def __init__(self, master):
        self.master = master
        self.password_label = Label(self.master, text="Your password: ",
                                    bg=BG_CLIENT, fg=FG_CLIENT, font=FONT, width=28, height=1)
        self.password_label.grid(row=3, sticky=N)

        self.__password = ""
        self.password_input = Entry(self.master, fg=BG_CLIENT, font=FONT2, width=32, show="*")
        self.password_input.grid(row=4, sticky=N, pady=5)

        Button(self.master, text="OK", fg=BG_CLIENT, font=FONT2, width=13,
               command=self.validate_pass).grid(column=0, row=5, sticky=W, padx=62, pady=20)

        Button(self.master, text="Cancel", fg=BG_CLIENT, font=FONT2, width=13,
               command=self.master.destroy).grid(column=0, row=5, sticky=E, padx=62, pady=20)

        Button(self.master, text= "Forgot Password", fg=BG_CLIENT, font=FONT2, width=13, command=self.forgot_pass).grid(row=6, sticky=N)

    def validate_pass(self):

        self.__password = self.password_input.get()

        with open("./Database/data_nick.dat", "rb") as user_profile:
            profile = pickle.load(user_profile)
            user_profile.close()

        if profile["password"] == self.__password:
            profile.update( { "validation" : True } )
            
            with open("./Database/data_nick.dat", "wb") as modify_profile:
                pickle.dump(profile, modify_profile)
                modify_profile.close()
            
            self.master.destroy()
        else:
            showerror("2048", "Password Invalid !!")

    def forgot_pass(self):
        system = os.name
        if system == 'nt':
            com = 'python ./Games/Client/Password_Box(2).py'
        elif system == 'posix':
            com = 'python3 ./Games/Client/Password_Box(2).py'
        os.system(com)


if __name__ == '__main__':

    new_window = Tk()
    new_window.title("2048")
    new_window.iconbitmap("./Games/Client/2048_logo.ico")
    new_window.config(bg="#57407C")
    new_window.rowconfigure(0)
    new_window.resizable(False, False)
    new_window.geometry('+510+300')

    Password_Box(new_window)
    new_window.mainloop()
