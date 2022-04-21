from tkinter import *
from function import *
from tkinter.messagebox import *
import pickle

import sys

LEN_GRID = 8
PADDING_GRID = 2  # Space between cells

'''
* Definition of background colors by cell type and by cell values through the use of dictionaries
* Definition of the writing font, its size and its type.
* Definition of up, down, left, right keys assigned to w, s, a, d or arrow keys
'''

FONT = ("Trebuchet", 20, "bold")
FONT2 = ("Trebuchet", 14, "bold")
KEY_UP = "'w'"
KEY_DOWN = "'s'"
KEY_LEFT = "'a'"
KEY_RIGHT = "'d'"
BG_GRID = "#2A251F"
BG_CELL_EMPTY = "#3F372F"
DICT_BG_CELL = {2: "#FAF1E8", 4: "#DACAAB", 8: "#D3F37A", 16: "#CEF368",
                   32: "#A8D03C", 64: "#8FB22F", 128: "#3662DB", 256: "#2C51B9",
                512: "#8F52F7", 1024: "#7B43DC", 2048: "#DC4343", 4096: "#CA3636", 8192: "#B52727", 16384: "#DCD72F", 32768: "#BCB500"}
DICT_FG_CELL = {2: "#7B6F62", 4: "#7B6F62", 8: "#7B6F62", 16: "#7B6F62",
                32: "#F7F3EE", 64: "#F7F3EE", 128: "#f9f6f2", 256: "#F7F3EE",
                512: "#F7F3EE", 1024: "#F7F3EE", 2048: "#F7F3EE", 4096: "#F7F3EE",
                8192: "#F7F3EE", 16384: "#F7F3EE", 32768: "#F7F3EE"}
FG_SCORE = "#F7F3EE"


class Grid2048(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.text = Label(text="Score", bg=BG_CELL_EMPTY, fg=FG_SCORE, font=FONT2, justify=CENTER, width=51, height=1)
        self.text.grid(row=0, sticky=N)
        self.textScore = Label(text="0", bg=BG_CELL_EMPTY, fg=FG_SCORE, font=FONT2, justify=CENTER, width=51, height=1)
        self.textScore.grid(row=1, sticky=N)

        self.grid()  # Creation of the position manager, grid cutting.
        self.master.title("32768")
        self.master.bind("<Key>", self.game)
        self.commands = {KEY_UP: up, KEY_DOWN: down, KEY_LEFT: left, KEY_RIGHT: right,
                         "'Up'": up, "'Down'": down, "'Left'": left, "'Right'": right}
        self.score = 0
        self.bestScore = 0
        self.cell_grid = []  # Initialize a list to store grid cells(Label)

        self.txtBestScore_txt = Label( text="Best score ", bg=BG_CELL_EMPTY, fg=FG_SCORE, font=FONT2, height=1)
        self.txtBestScore_txt.grid(row=0, sticky=NW)
        self.txtBestScore_score = Label( text="0", bg=BG_CELL_EMPTY, fg=FG_SCORE, font=FONT2, height=1)
        self.txtBestScore_score.grid(row=1, sticky=NW)

        self.newBtn = Label(text="New Game", fg=FG_SCORE, bg=BG_CELL_EMPTY, font=FONT2, height=1)
        self.newBtn.grid(row=0, sticky=NE)
        self.newBtn.bind("<Button-1>", self.new_game)
        Label(text="", bg=BG_CELL_EMPTY, font=FONT2, height=1).grid(row=1, sticky=NE)

        self.init_interface()
        self.init_grid()
        self.update_cell()
        self.mainloop()

    def init_interface(self):
        '''
        Creation of the grid, attribution of the background color + by empty cell and attribution of font + options
        '''
        background = Frame(self, bg=BG_GRID)
        background.grid()
        
        for i in range(LEN_GRID):
            row_grid = []

            for j in range(LEN_GRID):
                case = Frame(background, bg=BG_CELL_EMPTY)
                case.grid(row=i, column=j, padx=PADDING_GRID, pady=PADDING_GRID)
                t = Label(master=case, text="", bg=BG_CELL_EMPTY, justify=CENTER, font=FONT, width=4, height=2)
                t.grid()
                row_grid.append(t)

            self.cell_grid.append(row_grid)

    def init_grid(self):
        '''
        init_grid() loads the existing grid
        Otherwise, create the 2048 grid with 2 cells of value 2 or 4 at the start.
        '''
        with open("./Database/data_nick.dat", "rb") as user_file:
            obj = pickle.load(user_file)
            stuff = obj['V3']
            
            if stuff == {}:
                self.grid = init_game(LEN_GRID)
                self.grid = addTile(self.grid)
                self.grid = addTile(self.grid)
            else:
                self.grid = stuff['grid']
                self.score = stuff['score']
                self.bestScore = stuff['bestScore']
                self.textScore.config(text=str( self.score ))
                self.txtBestScore_score.config(text=str( self.bestScore ))
            
            user_file.close()

    def update_score(self, score, grid):
        self.textScore.config(text=str(score))

        # Insert the game data to database
        with open("./Database/data_nick.dat", "rb") as user_file:
            obj = pickle.load(user_file)
            user_file.close()

        if score < self.bestScore:
            with open("./Database/data_nick.dat", "wb") as progress_file:
                data = {"grid": grid, "score": score, "bestScore" : self.bestScore}
                obj.update( {'V3' : data} )
                
                pickle.dump(obj, progress_file)
                progress_file.close()
        
        if score >= self.bestScore:
            self.bestScore = score
            self.txtBestScore_score.config(text=str(score))
            
            with open("./Database/data_nick.dat", "wb") as progress_file_1:
                data1 = {"grid": grid, "score": score, "bestScore" : score}
                obj.update( {'V3' : data1} )

                pickle.dump(obj, progress_file_1)
                progress_file_1.close()
            


    def update_cell(self):
        '''
        Update cells (colors/values)
        '''
        for i in range(LEN_GRID):
            for j in range(LEN_GRID):
                value_cell = self.grid[i][j]

                if value_cell == 0:
                    self.cell_grid[i][j].configure(text="", bg=BG_CELL_EMPTY)

                else:
                    if value_cell <= 8192:
                        self.cell_grid[i][j].configure(
                            text=str(value_cell), bg=DICT_BG_CELL[value_cell], fg=DICT_FG_CELL[value_cell])
                    else:

                        if value_cell == 16384:
                            self.cell_grid[i][j].configure(
                                text="16K", bg=DICT_BG_CELL[value_cell], fg=DICT_FG_CELL[value_cell])
                        else:
                            self.cell_grid[i][j].configure(
                                text="32K", bg=DICT_BG_CELL[value_cell], fg=DICT_FG_CELL[value_cell])

    def new_game(self, event):
        '''
        Restart the game
        '''
        with open("./Database/data_nick.dat", "rb") as user_file:
            obj = pickle.load(user_file)
            user_file.close()


        with open("./Database/data_nick.dat", "wb") as progress_del:
            self.grid = init_game(LEN_GRID)
            self.grid = addTile(self.grid)
            self.grid = addTile(self.grid)
            
            new_data = {'grid': self.grid, 'score' : 0,'bestScore' : self.bestScore}
            obj.update( {'V3' : new_data} )
            pickle.dump( obj , progress_del)
            

        self.destroy()
        self.text.destroy()
        self.textScore.destroy()
        self.txtBestScore_txt.destroy()
        self.txtBestScore_score.destroy()
    
        if event != None:
            game = Grid2048()

    def game(self, event):
        '''
        A key has been pressed: tests, dedicated actions and status of the game in progress
        '''
        keySwitch = repr(event.keysym)

        if keySwitch in self.commands:
            self.grid, status_action, tmp_score = self.commands[keySwitch](self.grid)  # function (para)

            if status_action == True:
                self.score += tmp_score
                self.grid = addTile(self.grid)
                self.update_cell()

                self.update_score(self.score, self.grid)

                status_action = False
                if state(self.grid) == 'Win':
                    question = askretrycancel("Play again?", "You win! Well done! Do you want to play again?")

                    if question == True:
                        self.new_game(None)
                        game = Grid2048()
                    else:
                        self.new_game(None)
                        sys.exit(0)

                if state(self.grid) == 'Lose':
                    question = askretrycancel("Replay?", "You lose! Pity! Do you want to replay?")

                    if question == True:
                        self.new_game(None)
                        game = Grid2048()
                    else:
                        self.new_game(None)
                        sys.exit(0)


if __name__ == '__main__':
    root = Tk()
    root.resizable(False, False)
    root.iconbitmap("./Games/V3/2048_logo.ico")
    root.rowconfigure(0)
    root.rowconfigure(1)

    def on_closing():
        if askyesno("Close Game", "Do you want to close the game?"):
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    game = Grid2048()