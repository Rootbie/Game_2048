import pickle
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *
import os

# sys.path.append(os.path.abspath(os.path.join(".", "")))
# import menu

FONT = ("Trebuchet", 20, "bold")
FONT2 = ("Trebuchet", 14, "bold")
BG_CLIENT = "#57407C"
FG_CLIENT = "#EEEBF1"

class List_User:
    def __init__(self, master):
        self.master = master
        self.master.rowconfigure(0)
        self.master.columnconfigure(0)

        self.chosen_name = ''
        self.text = Label(text="WHO ARE YOU?", bg=BG_CLIENT, fg=FG_CLIENT, font=FONT, width=28, height=1)
        self.text.grid(row=0, sticky=N)

        # create a list box
        users = user_storage()
        users_var = StringVar( value = users)
        self.listbox = Listbox(self.master, listvariable=users_var, activestyle=NONE, selectmode=SINGLE, justify=CENTER, font=FONT2, selectbackground=BG_CLIENT, fg=BG_CLIENT, width=32)
        self.listbox.grid(row=1, sticky=N, pady=10)
        self.listbox.bind('<<ListboxSelect>>', self.users_selected)

        # button
        self.createBtn = Button(text="Create New", fg=BG_CLIENT, font=FONT2, width=13, command=self.create_func)
        self.createBtn.grid(column=0, row=3, sticky=W, padx=62, pady=10)

        self.deleteBtn = Button(text="Delete", fg=BG_CLIENT, font=FONT2, width=13, command=self.detele_user)
        self.deleteBtn.grid(column=0, row=3, sticky=E, padx=62, pady=10)

        self.okBtn = Button(text="OK", fg=BG_CLIENT, font=FONT2, width=13, command=self.clickOK)
        self.okBtn.grid(column=0, row=4, sticky=W, padx=62, pady=10)

        self.cancelBtn = Button(text="Cancel", fg=BG_CLIENT, font=FONT2, width=13, command=self.master.destroy)
        self.cancelBtn.grid(column=0, row=4, sticky=E, padx=62, pady=10)



    def create_func(self):
        system = os.name
        if system == 'nt':
            com = 'python ./Games/Client/New_User.py'
        elif system == 'posix':
            com = 'python3 ./Games/Client/New_User.py'
        os.system(com)
        List_User(self.master)


    def users_selected(self, event):
        """ 
        handle user selected event
        """
        self.chosen_name = self.listbox.get(ANCHOR)
        
    def clickOK(self):
        if self.chosen_name != '':
            
            profile = {}
            with open("./Database/data_progress.dat", "rb") as view_storage:
                data = pickle.load(view_storage)
                for obj in data:
                    if obj['username'] == self.chosen_name:
                        profile = obj

                view_storage.close()

            with open("./Database/data_nick.dat", "wb") as user_profile:
                pickle.dump( profile , user_profile)
                user_profile.close()
            

            system = os.name
            if system == 'nt':
                com = 'python ./Games/Client/Password_Box.py'
            elif system == 'posix':
                com = 'python3 ./Games/Client/Password_Box.py'
            os.system(com)

            # check validation in data_nick
            with open("./Database/data_nick.dat", "rb") as view_validation:
                checkUser = pickle.load(view_validation)
                
                if checkUser["validation"] == True:
                    self.master.destroy()
                view_validation.close()



    def detele_user(self):
        if self.chosen_name != '':
            if askyesno( "Delete Player", "Are you sure you want to permanently detele this player?"):
                
                with open("./Database/data_progress.dat", "rb") as view_storage:
                    data = pickle.load(view_storage)
                    view_storage.close()

                for elem in data:
                    if elem['username'] == self.chosen_name:
                        data.remove(elem)
                
                with open("./Database/data_progress.dat", "wb") as del_storage:
                    pickle.dump(data, del_storage)
                    del_storage.close()
                
                List_User(self.master)




def user_storage():
    try:
        with open("./Database/data_progress.dat", "rb") as view_storage:
            data = pickle.load(view_storage)
            users = []
            for obj in data:
                users.append( obj['username'])
            
            view_storage.close()
        return tuple(users)

    except:
        with open("./Database/data_progress.dat", "wb") as new_storage:
            listUser = []
            pickle.dump( listUser , new_storage)
            new_storage.close()


if __name__ == "__main__":
    root = Tk()
    root.title("2048")
    root.iconbitmap("./Games/Client/2048_logo.ico")
    root.config(bg="#57407C")
    root.resizable(False, False)
    root.geometry('+510+100')

    List_User(root)
    root.mainloop()

