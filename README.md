# Game_2048
2048 (Admin version) with database, replaying game, forgot password

## Getting Started
1. Get Python >= 3.9
2. Install pygame:\
    ```$ pip install pygame```

3. Run the game:\
    ```$ python menu.py```

## Moves
1. 2048 is played on a gray 4×4 grid, with numbered tiles that slide when a player moves them using the **four arrow keys** or **W A S D**.
2. Click **New Game** to **restart** the game.
3. Join the numbers and get to **2048** to win!

## Game Rules
1. Every turn, a new tile will randomly appear in an empty spot on the board with a value of either 2 or 4.
2. Tiles slide as far as possible in the chosen direction until they are stopped by either another tile or the edge of the grid. 
3. If two tiles of the same number collide while moving, they will merge into a tile with the total value of the two tiles that collided.
4. The resulting tile cannot merge with another tile again in the same move. 
5. If a move causes three consecutive tiles of the same value to slide together, only the two tiles farthest along the direction of motion will combine. 
6. If all four spaces in a row or column are filled with tiles of the same value, a move parallel to that row/column will combine the first two and last two.

## Images
![image](https://user-images.githubusercontent.com/95699016/164433093-02a22215-a253-4d13-b910-58b716ea2763.png)
![image](https://user-images.githubusercontent.com/95699016/164433720-aad2b80a-4cfc-4bcf-a507-322516b5e0fe.png)

