from random import *
from pygame import mixer

mixer.init()

def init_game(n):
    grid = []

    for i in range(n):
        grid.append([0] * n)

    return grid


def addTile(grid):
    '''
    Add a square of value 2, on a random position in the corresponding size
    has the grid, and in a coordinate not already containing a value other than 0
    0 being a free square (without a tile).
    '''

    x = randint(0, len(grid) - 1)
    y = randint(0, len(grid) - 1)

    while (grid[x][y] != 0):
        x = randint(0, len(grid) - 1)
        y = randint(0, len(grid) - 1)

    ran = randint(1, 12)
    if ran <= 4 or ran >= 8:
        grid[x][y] = 2

    elif ran == 5 or ran == 7:
        grid[x][y] = 4

    else:
        grid[x][y] = 8

    return grid



def state(grid):
    '''
    At each step, a state of the current game is checked.
    * If a cell contains a value equal to 32768, the user wins.
    * If there is a solution left in a full grid, the user does not lose
    * If there remains a cell with a value equal to 0 (equivalent to empty cell), the user has not lost.
    * If there is a solution left in the grid, not finished for the last 2 for.
    * If no test returns an answer, then it returns lost, meaning that none of the conditions for wins / moves to play are validated.
    '''
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 32768:
                return 'Win'

    for i in range( len(grid) -1 ):
        for j in range( len(grid[0]) -1 ):
            if grid[i][j] == grid[i+1][j] or grid[i][j+1] == grid[i][j]:
                return 'Not finished'
    
    for i in range( len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return 'Not finished'

    for i in range( len(grid) - 1):
        if grid[ len(grid) -1 ][i] == grid[ len(grid) -1 ][i+1]:
            return 'Not finished'

    for j in range( len(grid) -1 ):
        if grid[j][ len(grid) - 1] == grid[j+1][ len(grid)-1 ]:
            return 'Not finished'

    return 'Lose'

def inversion(grid):
    '''
    B = A^-1, such as: AB = BA = In
    This function can only be used on a square grid.
    '''
    temp = []
    for i in range( len(grid) ):
        temp.append([])
        for j in range( len(grid[0]) ):
            temp[i].append(grid[i][ len(grid[0]) -1 -j ])

    return temp

def transpose(grid):
    '''
    The transpose A^T of a grid A is obtained by axial symmetry with respect to the main diagonal of the grid.
    The transpose of the transpose (A^T)^T is the original A grid.
    '''
    temp = []

    for i in range(len(grid[0])):
        temp.append([])

        for j in range(len(grid)):
            temp[i].append(grid[j][i])

    return temp


def secondGrid(grid):
    temp = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [
        0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

    status_action = False

    for i in range(len(grid)):
        count = 0

        for j in range(len(grid)):
            if grid[i][j] != 0:
                temp[i][count] = grid[i][j]
                
                if j != count:
                    status_action = True
                
                count += 1
    
    return (temp ,status_action)

def fusion(grid):
    '''
    The fusion code manages the cell fusion, if the position [i] [j] == [i] [j + 1], then we multiply the value of [i] [j] * 2
    '''
    status_action = False
    tmp_score = 0

    for i in range(len(grid)):
        for j in range(len(grid) - 1):
            if grid[i][j] == grid[i][j+1] and grid[i][j] != 0:
                grid[i][j] *= 2
                grid[i][j+1] = 0
                status_action = True
                tmp_score += grid[i][j] * 10

    return (grid, status_action, tmp_score)


def up(grid):
    grid = transpose(grid)

    grid, status_action= secondGrid(grid)
    temp = fusion(grid)
    grid = temp[0]
    status_action = status_action or temp[1]
    tmp_score = temp[2]
    grid = secondGrid(grid)[0]
    
    grid = transpose(grid)

    mixer.music.load("./Games/V3/8bitgame10.wav")
    mixer.music.play(loops=0)

    return (grid, status_action, tmp_score)


def down(grid):
    grid = inversion(transpose(grid))

    grid, status_action = secondGrid(grid)
    temp = fusion(grid)
    grid = temp[0]
    status_action = status_action or temp[1]
    tmp_score = temp[2]
    grid = secondGrid(grid)[0]

    grid = transpose( inversion(grid) )

    mixer.music.load("./Games/V3/8bitgame10.wav")
    mixer.music.play(loops=0)

    return (grid, status_action, tmp_score)


def left(grid):
    grid, status_action = secondGrid(grid)
    temp = fusion(grid)
    grid = temp[0]
    status_action = status_action or temp[1]
    tmp_score = temp[2]
    grid = secondGrid(grid)[0]

    mixer.music.load("./Games/V3/8bitgame10.wav")
    mixer.music.play(loops=0)

    return (grid, status_action, tmp_score)


def right(grid):
    grid = inversion(grid)
    
    grid, status_action = secondGrid(grid)
    temp = fusion(grid)
    grid = temp[0]
    status_action = status_action or temp[1]
    tmp_score = temp[2]
    grid = secondGrid(grid)[0]

    grid = inversion(grid)

    mixer.music.load("./Games/V3/8bitgame10.wav")
    mixer.music.play(loops=0)

    return (grid, status_action, tmp_score)
