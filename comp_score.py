def score_comp (board):
    score = 0 
    #Horizontal
    for y in range(6):
        for x in range(4):
            if (board[y][x]==2):
                
                if (board[y][x+1]==board[y][x+2]==board[y][x+3]==0):
                    score += 1

                if (board[y][x+1]==2 and board[y][x+2]==board[y][x+3]==0 ):
                    score += 2
                        
                if (board[y][x+1]==board[y][x+2]==2 and board[y][x+3]==0):
                    score += 3


        for x in range(4,7,+1):

            if (board[y][x]==2):
                
                if (board[y][x-1]==board[y][x-2]==board[y][x-3]==0):
                    score += 1

                if (board[y][x-1]==2 and board[y][x-2]==board[y][x-3]==0 ):
                    score += 2
                        
                if (board[y][x-1]==board[y][x-2]==2 and board[y][x-3]==0):
                    score += 3


    #Vertical
    for x in range(7):
        for y in range(3):
            if (board[y][x]==2):
                
                if (board[y+1][x]==board[y+2][x]==board[y+3][x]==0):
                    score += 1

                if (board[y+1][x]== 2 and board[y+2][x]==board[y+3][x]==0):
                    score += 2 

                if (board[y+1][x]== board[y+2][x]== 2 and board[y+3][x]==0):
                    score += 3 


        for y in range(3,6,+1):

            if (board[y][x]==2):
                
                if (board[y-1][x]==board[y-2][x]==board[y-3][x]==0):
                    score += 1

                if (board[y-1][x]== 2 and board[y-2][x]==board[y-3][x]==0):
                    score += 2 

                if (board[y-1][x]== board[y-2][x]== 2 and board[y-3][x]==0):
                    score += 3 

    #Diagonally
    for x in range (5,0,-1):
        for y in range(6,0,-1):

            if (board[x][y] ==2 and  board[x-1][y-1] == board[x-2][y-2] == board[x-3][y-3]== 0):
                score += 1

            if (board[x][y] ==2 and  board[x-1][y-1] ==2 and  board[x-2][y-2] == board[x-3][y-3]== 0):
                score += 2

            if (board[x][y] ==2 and  board[x-1][y-1] == board[x-2][y-2] ==2 and board[x-3][y-3]== 0):
                score += 3




    for x in range(5,0,-1):
        for y in range(4):
            if (board[x][y]==2 and board[x-1][y+1]==board[x-2][y+2] == board[x-3][y+3]==0 ):
                score += 1


            if (board[x][y]==2 and board[x-1][y+1]==2 and board[x-2][y+2] == board[x-3][y+3]==0 ):
                score += 2

            if (board[x][y]==2 and board[x-1][y+1]== board[x-2][y+2]==2 and board[x-3][y+3]==0 ):



                score += 2


    return score 