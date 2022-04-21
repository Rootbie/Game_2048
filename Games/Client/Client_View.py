import pickle
from tkinter import *
import os

BG_CLIENT = "#57407C"
FG_CLIENT = "#EEEBF1"
FONT = ("Trebuchet", 20, "bold")


class Client_View:
    def __init__(self, master):
        self.master = master
        self.master.protocol("WM_DELETE_WINDOW", self.back)

        self.username = ''
        with open("./Database/data_nick.dat", "rb") as user_profile:
            profile = pickle.load(user_profile)
            if 'username' in profile:
                self.username = profile['username']
            user_profile.close()
        
        self.text = Label(text= 'Welcome, '+ self.username, bg=BG_CLIENT, fg=FG_CLIENT, font=FONT, height=1)
        self.text.pack(side=TOP, padx=5, pady=5)
        Button(self.master, text=' Version 2048 Original ', command= self.V1, width=20).pack(side=TOP, padx=5, pady=5)
        Button(self.master, text=' Version 2048 8x8 ', command= self.V2, width=20).pack(side=TOP, padx=5, pady=5)
        Button(self.master, text=' Version 32768 ', command= self.V3 , width=20).pack(side=TOP, padx=5, pady=5)
        Button(self.master, text=' Version 2048 Reverse ', command = self.V4, width=20).pack(side=TOP, padx=5, pady=5)
        Button(self.master, text=' Log out ', command=self.back ,width=20).pack(side=TOP, padx=5, pady=5)
    

    def V1(self):
        system = os.name
        if system == 'nt':
            com = 'python ./Games/V1/2048.py '
        elif system == 'posix':
            com = ' python3 ./Games/V1/2048.py '
        
        os.system(com)

    def V2(self):
        system = os.name
        if system == 'nt':
            com = 'python ./Games/V2/large2048.py '
        elif system == 'posix':
            com = ' python3 ./Games/V2/large2048.py '
        
        os.system(com)

    def V3(self):
        system = os.name
        if system == 'nt':
            com = 'python ./Games/V3/32768.py '
        elif system == 'posix':
            com = ' python3 ./Games/V3/32768.py '
        
        os.system(com)

    def V4(self):
        system = os.name
        if system == 'nt':
            com = 'python ./Games/V4/Reverse2048.py '
        elif system == 'posix':
            com = ' python3 ./Games/V4/Reverse2048.py '
        os.system(com)
    
    def back(self):
        self.update_db()
        self.master.destroy()
        
        system = os.name
        if system == 'nt':
            com = 'python menu.py '
        elif system == 'posix':
            com = ' python3 menu.py '
        os.system(com)


    def update_db(self):
        ''' Save all the game progress of each user to db'''
        with open("./Database/data_nick.dat", "rb") as view_user:
            obj = pickle.load(view_user)
            view_user.close()
        
        with open("./Database/data_progress.dat", "rb") as view_storage:
            db = pickle.load(view_storage)
            view_storage.close()

        obj.pop("validation")
        for i in range(len(db)):
            if db[i]['username'] == self.username:
                db[i] = obj
        
        
        with open("./Database/data_progress.dat", "wb") as modify_storage:
            pickle.dump( db, modify_storage)
            modify_storage.close()
