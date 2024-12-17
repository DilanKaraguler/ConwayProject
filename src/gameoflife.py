import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt
import pandas as pd


def plotgrid(myarray):
    '''For a given 2D numpy array, plot the grid 
    with the alive cells in orange and the dead cells in gray'''
    
    x_range = np.linspace(0, myarray.shape[1]-1, myarray.shape[1]) 
    y_range = np.linspace(0, myarray.shape[0]-1, myarray.shape[0]) # repeat for the y/vertical axis
    
    x_indices, y_indices = np.meshgrid(x_range, y_range)
    
    dead_x = x_indices[myarray == 0];   
    dead_y = y_indices[myarray == 0]; 
    alive_x = x_indices[myarray == 1];   
    alive_y = y_indices[myarray == 1]; 
    
    plt.plot(dead_x, myarray.shape[0] - dead_y - 1, 's',color= 'gray' ,markersize=10)   
    plt.plot(alive_x, myarray.shape[0] - alive_y - 1, 's',color= 'orange',markersize=10)  # repeat for indices with fire 
    
    plt.xlim([-1,myarray.shape[1]])
    plt.ylim([-1,myarray.shape[0]]) 

    plt.tick_params(axis='both', which='both',
                    bottom=False, top=False, left=False, right=False,
                    labelbottom=False, labelleft=False)


def set_board(board_size=50, density=0.5):
    '''Create a random game board of a given size and density'''
    
    game_board = np.zeros((board_size,board_size),dtype='int64')
    
    for i in range(board_size):
        for j in range(board_size):
            if rand.random() <= density:
                game_board[i,j] = 1
    
    return game_board


def onBoard(i, j, image):
    '''Checks the given location (i,j) is on the board'''
    ni = image.shape[0] # number of pixels (height)
    nj = image.shape[1] # number of pixels (width)
    if i <= ni-1 and i >= 0: 
        if j<=nj-1 and j>=0:
            return True
        else:
            return False
    else:
        return False
    
    
def getNeighborValues(i,j, board, type='square'):
    '''Returns the values of the neighbors of a given pixel (i,j) on the given shaped board
    
    Type of board can be 'square', 'torus' or 'sphere' '''
    neighborhood = [(i-1,j-1), (i-1, j), (i-1, j+1) , (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i, j+1)]
    c_i , c_j = i , j
    ni = board.shape[0]
    nj = board.shape[1]
    neighbor_values = []
    for neighbor in neighborhood:
        i, j = neighbor
        if onBoard(i, j, board)==False:
            if type == 'square':
                pass
            if type == 'torus': 
                neighbor_values.append(board[i%ni,j%nj])
            if type == 'sphere':
                neighbor_values.append(board[c_j,c_i])
        else:
            neighbor_values.append(board[i,j])
    
    return neighbor_values


def advance_board(game_board,type='square'):
    '''Advances the game board by one step according to the rules of the game of life for the given type of board'''
    new_board = np.zeros_like(game_board)
    
    for i in range(0,game_board.shape[1]):
        
        for j in range(0,game_board.shape[0]):
            
            if game_board[i,j]==0:
                #Rule 1: Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
                values = getNeighborValues(i,j,game_board,type)
                if sum(values) == 3:
                    new_board[i,j]=1
                else:
                    new_board[i,j]=0
                
            elif game_board[i,j]==1:
                values = getNeighborValues(i,j,game_board,type)
                #Rule 2: Any live cell with fewer than two live neighbours dies, as if by underpopulation.
                #Rule 3: Any live cell with two or three live neighbours lives on to the next generation.
                #Rule 4: Any live cell with more than three live neighbours dies, as if by overpopulation
                if sum(values) < 2:
                    new_board[i,j]=0
                if sum(values) == 2 or sum(values) == 3:
                    new_board[i,j]=1
                else:
                    new_board[i,j]=0
           
    return new_board


