class tictactoe:

    def winners(self, player):
        if player == 'X':
            print("""
            =============================
            ||     PLAYER 1 WIN!!!     ||
            =============================""")
        else:
            print("""
            =============================
            ||     PLAYER 2 WIN!!!     ||
            =============================""")

    def matrix_board(self):
        matrix = """
                x1       x2       x3       
            _________________________
            |       |       |       |
        y1  |   {}   |   {}   |   {}   |
            |_______|_______|_______|
            |       |       |       |
        y2  |   {}   |   {}   |   {}   |
            |_______|_______|_______|
            |       |       |       |
        y3  |   {}   |   {}   |   {}   |
            |_______|_______|_______|

        """
        return matrix

    def show_default_board(self):
        board = [['_','_','_'],['_','_','_'],['_','_','_']]
        br = [item for sublist in board for item in sublist]
        matrix = self.matrix_board().format(br[0],br[1],br[2],br[3],br[4],br[5],br[6],br[7],br[8])
        print("\n    SIMPLE TIC TAC TOE GAME Player VS Player\n")
        print(matrix)

    def show_primary_board(self, board):
        br = [item for sublist in board for item in sublist]
        matrix = self.matrix_board().format(br[0],br[1],br[2],br[3],br[4],br[5],br[6],br[7],br[8])
        print(matrix)

    def check_result(self, board):
        #Horizontal Check
        H_X_check = [i.count('X') for i in board]
        H_O_check = [i.count('O') for i in board]
        
        #Vertical Check
        V_X_check = [i.count('X') for i in [[i[0] for i in board],[i[1] for i in board],[i[2] for i in board]]]
        V_O_check = [i.count('O') for i in [[i[0] for i in board],[i[1] for i in board],[i[2] for i in board]]]
        
        #Diagonal Check
        i, status, Left_Diag, Right_Diag = 0, '',[], []
        
        while i < len(board):
            Left_Diag.append(board[i][i])
            Right_Diag.append(board[i][(len(board)-1)-i])
            i += 1

        D_X_check = [i.count('X') for i in [Left_Diag,Right_Diag]]
        D_O_check = [i.count('O') for i in [Left_Diag,Right_Diag]]

        #Status
        if (3 in H_X_check) or (3 in V_X_check) or (3 in D_X_check):
            status = 'X'
        if (3 in H_O_check) or (3 in V_O_check) or (3 in D_O_check):
            status = 'O'
        return status

    def player(self, board):
        counter, x, y, val = 1, 0, 0, ''

        while True:

            if (counter % 2 == 1):
                value = input("First Player X (x,y), exp: 1,1 : ").split(',')
                y,x,val = int(value[0])-1, int(value[1])-1, 'X'
            else:
                value = input("Second Player O (x,y), exp: 1,1 : ").split(',')
                y,x,val = int(value[0])-1, int(value[1])-1, 'O'

            status_filled_value = self.check_filled_value(board,x,y)
            status_matrix_coordinate = self.check_matrix_coordinates(x,y)

            #Check Matrix Coordinates
            if status_matrix_coordinate == False:
                print("Matrix coordinates Numbers 1 to 3\n")
                continue
            
            #Check Filled Value in Board
            if status_filled_value:
                board[x][y] = val
            else:
                print("Already filled with other players\n")
                continue

            #Show Board
            self.show_primary_board(board)
            
            #Check result
            status = self.check_result(board)

            #Status result
            if (status in ['X','O']):
                self.winners(status)
                break

            counter += 1

    def check_filled_value(self, board, x, y):
        if (board[x][y] in ['X','O']):
            return False
        else:
            return True

    def check_matrix_coordinates(self, x, y):
        n_matrix = [1,2,3]
        if (x in n_matrix) and (y in n_matrix):
            return True
        else:
            False


if __name__=="__main__":
    #Matrix board
    board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    ttt = tictactoe()
    ttt.show_default_board()
    ttt.player(board)
    



