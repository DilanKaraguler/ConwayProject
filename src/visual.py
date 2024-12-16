import numpy as np
import gameoflife 
from gameoflife import advance_board, set_board, plotgrid

from IPython.display import display, clear_output
import time  


def calc_stats(game_board):
    
    board_length= game_board.shape[0]*game_board.shape[1]
    
    frac_empty = len(np.where(game_board==0)[0])/board_length

    frac_alive = len(np.where(game_board==1)[0])/board_length
    
    return frac_empty, frac_alive


def simulator(board_size=50, density=0.5,type='square',plot=True):

    fig = plt.figure(figsize=(10, 10))
    
    game_board = set_board(board_size=board_size, density=density)
    
    plotgrid(game_board)

    alive = True
    iterations = 0
    #prev_frac_alive = None
    #frac_record =[] #keep track of fraction of alive cells in every iteration
    #new_borns = density*board_size**2 #keep track of new borns
    while alive == True:
        
        iterated_board = advance_board(game_board,type)
        
        #new_born = np.sum(np.maximum(iterated_board - game_board, 0))
        #new_borns+=new_born
        if plot == True:    
            plotgrid(game_board)
            time.sleep(0.03)
            clear_output(wait=True)
            display(fig)
            fig.clear()

        iterations += 1
        if np.array_equal(iterated_board, game_board)  or iterations ==200:
            alive = False
        else:
            game_board = iterated_board
    
    if plot == True:
        plt.close()
    frac_empty, frac_alive = calc_stats(iterated_board)
    return iterations , frac_alive
