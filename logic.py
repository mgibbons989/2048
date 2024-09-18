import random

def start():
    mat = [] #game board
    for i in range(4):
        mat.append([0] * 4) #list of 4 lists of zeros
    add_new_2(mat)
    return(mat)

def add_new_2(mat):
    while(mat[r][c] != 0): #has to be an empty cell
        r = random.randint(0,3)
        c = random.randint(0,3) #choose a random row and column to put 2
    mat[r][c] = 2

def get_current(mat): #check positions if player has won
    for i in range(4):
        for j in range(4):
            if(mat[i][j] == 2048): #check if player won
                return 'WON'
            
    for i in range(4):
        for j in range(4):
            if(mat[i][j] == 0): #check if there's any empty cells
               return 'NOT OVER'
    
    for i in range(3):
        for j in range(3):
            if(mat[i][j] == mat[i + 1][j] or mat[i][j] == mat[i][j + 1]): #if the cell to the left or under of current cell is equal, we can merge them and create a new empty cell
                return 'NOT OVER'
    
    for j in range(3):
        if(mat[3][j] == mat[3][j + 1]): #bottom edge
            return 'NOT OVER'
    
    for i in range(3):
        if(mat[i][3] == mat[i + 1][3]): #right edge
            return 'NOT OVER'
    
    return 'LOST' #if none of the previous happened then we lost the game

def compress(mat):
    pass

def merge(mat):
    pass

def reverse(mat):
    pass

def transpose(mat):
    pass

def move_right(grid):
    pass

def move_up(grid):
    pass

def move_down(grid):
    pass

