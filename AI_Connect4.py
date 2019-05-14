import numpy as np
import math
import random
from winning import *
# initial values for alpha and beta
MAX, MIN = math.inf, -math.inf 
ROWS,COLUMNS=6,7
def creatBoard():
  board = np.zeros((ROWS,COLUMNS))
  return board
def printBoard(board):
	print(np.flip(board, 0))

def children(board):
  return board.copy()
	# play(bCopy,row, col,2)
def play(board,row,col,val):
  board[row][col] = val
def getNextRow(board,col):
  for r in range(ROWS):
    if board[r][col] == 0:
      return r
def isValidLocation(board, col):
  return board[ROWS-1][col] == 0
def getPossibleLocations(board):
  valid_locations = []
  for col in range(COLUMNS):
    if isValidLocation(board, col):
      valid_locations.append(col)
  return valid_locations
def minimax(depth,maximizingPlayer,board, alpha, beta):
    possibleLocations=getPossibleLocations(board)
    # leaf node is reached 
    isterminal=isTerminal(board)
    if depth == 7 or isTerminal:
      if isterminal:
        # AI wins
        if winning(board, 2):
          return (None, math.inf)
        # player wins
        elif winning(board,1):
          return (None, -math.inf)
        else: # Game is over, no more valid moves
          return (None, 0)
      # depth is 7 
      else:
        return (None, utility(board,2))
    if maximizingPlayer:  
      val = MIN
      column=random.choice(possibleLocations)
      # Recur  
      for col in possibleLocations:
          row=getNextRow(board,col)
          newBoard=children(board)
          play(newBoard,row,col,2)
          newVal=minimax(depth + 1,False, newBoard, alpha, beta)[1]
          if newVal > val:
            val = newVal
            column = col

          alpha = max(alpha, val)
          # Alpha Beta Pruning 
          if alpha >= beta:
            break

      return column,val 
       
    else: 
      val = MAX 
      column = random.choice(possibleLocations)
      # Recur
      for col in possibleLocations:
        row=getNextRow(board,col)
        newBoard=children(board)
        play(newBoard,row,col,2)
        newVal = minimax(depth + 1,True, newBoard, alpha, beta)  
        if newVal < val:
          val = newVal
          column = col

        beta = min(beta, val)
        # Alpha Beta Pruning  
        if beta <= alpha:
          break 
      return column,val 
        
if __name__ == "__main__":
  board = creatBoard()
  printBoard(board)
  gameOver = False
  turn = 0
  while not gameOver:
    # ask for player one col input
    if turn==0:
      col=input("first player selection (0-6): ")
      # checking for  the next available row
      # then drop the ball into board[row][col]
        # check if it's the winning move or not 
        # flip the gameOver flag if it's the winning move 
    else:
      pass
      # get the AI's row and col of the best move 
      # then drop the ball into board[row][col]
      # check if it's the winning move or not 
        # flip the gameOver flag if it's the winning move 
    # flip the the turns
    turn +=1
    turn = turn % 2