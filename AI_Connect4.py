import numpy as np
# initial values for alpha and beta
MAX, MIN = 100000, -100000 
ROWS,COLUMNS=6,7
def creatBoard():
  board = np.zeros((ROWS,COLUMNS))
  return board
def printBoard(board):
	print(np.flip(board, 0))
def minimax(depth, nodeIndex, maximizingPlayer,board, alpha, beta):
    # leaf node is reached  
    if depth == 7:  
        return board[nodeIndex]  

    if maximizingPlayer:  
       
        best = MIN 
  
        # Recur for left and right children  
        for i in range(0, 2):  
              
            val = minimax(depth + 1, nodeIndex * 2 + i,  
                          False, board, alpha, beta)  
            best = max(best, val)  
            alpha = max(alpha, best)  
  
            # Alpha Beta Pruning  
            if beta <= alpha:  
                break 
           
        return best  
       
    else: 
        best = MAX 
  
        # Recur for left and  
        # right children  
        for i in range(0, 2):  
           
            val = minimax(depth + 1, nodeIndex * 2 + i,  
                            True, board, alpha, beta)  
            best = min(best, val)  
            beta = min(beta, best)  
  
            # Alpha Beta Pruning  
            if beta <= alpha:  
                break 
           
        return best 
        
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