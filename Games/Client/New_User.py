import pickle
from tkinter import *
from tkinter.messagebox import *
import re

FONT = ("Trebuchet", 20, "bold")
FONT2 = ("Trebuchet", 14, "bold")
BG_CLIENT = "#57407C"
FG_CLIENT = "#EEEBF1"

class New_User:
    def __init__(self, master):
        self.master = master       
        self.master.rowconfigure(0)
        self.master.columnconfigure(0)

        self.text = Label(text="NEW USER",bg= BG_CLIENT , fg=FG_CLIENT, font= FONT, width=28, height=1)
        self.text.grid(row= 0, sticky=N)

        self.username_label = Label(text="Please enter your name:",bg= BG_CLIENT , fg=FG_CLIENT, font= FONT2, height=1)
        self.username_label.grid(row=1, sticky=N)

        self.username_entry = Entry(self.master, fg= BG_CLIENT, font=FONT2, width=32 )
        self.username_entry.grid(row=2, sticky=N, pady=5) 

        self.password_label = Label(text="Your password: ", bg= BG_CLIENT , fg=FG_CLIENT, font= FONT2, height=1)
        self.password_label.grid(row=3, sticky=N)

        self.password_entry = Entry(self.master, fg= BG_CLIENT, font=FONT2, width=32 )
        self.password_entry.grid(row=4, sticky=N, pady=5)

        self.okBtn = Button(text="OK", fg= BG_CLIENT, font=FONT2, width=13, command=self.create_user)
        self.okBtn.grid( column=0, row=5, sticky= W, padx=62, pady= 20)

        self.cancelBtn = Button(text="Cancel", fg= BG_CLIENT, font=FONT2, width=13, command=self.master.destroy)
        self.cancelBtn.grid( column=0, row=5, sticky= E, padx=62, pady= 20)



    def create_user(self):
        '''
        save new user to db
        '''
        with open("./Database/data_progress.dat", "rb") as view_storage:
            listUser = pickle.load(view_storage)
            view_storage.close()

        user = { 'username' : '', 'password': '', 'V1' : {}, 'V2' : {}, 'V3' : {}, 'V4' : {} }
        bool = False
        name = self.username_entry.get().strip()
        password =self.password_entry.get()

        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}$"
        pat = re.compile(reg)

        if len(name) < 6 :
            showerror("2048", "Your name must have at least 6 characters")
        elif re.search(pat, password) == None:
            showerror("2048", "Your password should have:\n- At least one number.\n- At least one Uppercase and one Lowercase character.\n- At least one special symbol.\n- 8 to 20 characters long.")
        else:
            for obj in listUser:
                if obj['username'].lower() == name.lower():
                    bool = True

            if bool == True:
                showerror("2048", "This user has already created")
            else:
                user["username"] = name
                user["password"] = password
                listUser.append(user)
                 
                with open("./Database/data_progress.dat", "wb") as insert_storage:
                    pickle.dump(listUser, insert_storage)
                    insert_storage.close()

                self.master.destroy()



if __name__ == "__main__":
    root = Tk()
    root.title("2048")
    root.iconbitmap("./Games/Client/2048_logo.ico")
    root.config(bg="#57407C")
    root.resizable(False, False)
    root.geometry('+510+300')

    New_User(root)
    root.mainloop()
