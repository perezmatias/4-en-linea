#Perez Matias Agustin
#4 en Linea
#Contiene todo el juego

class FullColumn(Exception):
    pass

class ColumnOutOfRange(Exception):
    pass

class Game():
    def __init__(self):
        self.board = [[" " for i in range(8)] for i in range(8)] 
        self.player = True
        self.token = "x"
        self.game_winner = False
        self.playing = True

#Cambio de jugador
    def player_change(self):
        if self.player == True:
            self.player = False
            self.token = "o"
        else:
            self.player = True
            self.token = "x"

#Seleccion de la columna
    def insert_token(self,column):

        if column < 0 or column >= 8:
            raise ColumnOutOfRange('Columna fuera de rango')
        
        if self.board[0][column] != " ":
            raise FullColumn('Columna llena')
        
        else:    
            self.introduce_token(column)
            if self.winner():
                return True
            else:
                self.player_change()

#Colocar ficha
    def introduce_token(self, column):
        pos = 0
        next_pos = 1
        final = 7
        board = self.board
        
        for index in board:
            if board[final][column] == " ":
                board[final][column] = self.token
                
                return board 
            if board[pos][column] == " " and board[next_pos][column] != " ":
                board[pos][column] = self.token
                return board
            pos += 1
            next_pos += 1

#verificar fila
    def row_winner(self):
        #row
        winner = False
        column = 0
        change_row = 0
        board = self.board
        while change_row < 8:
            for index in board[change_row]:
                if board[change_row][column] == self.token and board[change_row][column + 1] == self.token and board[change_row][column + 2] == self.token and board[change_row][column + 3] == self.token:
                    winner = True
                    return winner

                if column == 4:
                    column = 0
                    break
                column += 1
            change_row += 1
        if winner == False:
            return False

#verificar columna
    def column_winner(self):
        #columns
        winner = False
        row = 0
        change_columns = 0
        board = self.board
        
        while change_columns < 8:
            for index in board:
                if board[row][change_columns] == self.token and board[row+1][change_columns] == self.token and board[row+2][change_columns] == self.token and board[row+3][change_columns] == self.token:
                    winner = True
                    return winner
                if row == 4:
                    row = 0
                    break

                row +=1
            change_columns +=1
        
        if winner == False:
            return False

#Verficar diagonal
    def decreasing_diagonal_winner(self):
        #diagonal hacia abajo
        
        winner = False
        row = 7
        column = 7
        board = self.board
        
        while row >= 0:
            for i in board:
                if board[row][column] == self.token and board[row-1][column-1] == self.token and board[row-2][column-2] == self.token and board[row-3][column-3] == self.token:
                    winner = True
                    return winner

                if column == 3:
                    column = 7
                    break
                column -= 1
            row -= 1

        if winner == False:
            return False

#verificar diagonal
    def growing_diagonal_winner(self):
        #diagonal hacia arriba
        winner = False
        row = 7
        column = 0
        board = self.board
        while row >= 0:
            for index in board:
                if board[row][column] == self.token and board[row-1][column+1] == self.token and board[row-2][column+2] == self.token and board[row-3][column+3] == self.token:
                    winner = True
                    return winner
                if column == 5:
                    column = 0
                    break
                column += 1
            row -= 1
            
        if winner == False:
            return False

#Define al ganador
    def winner(self):
        if self.column_winner() == True or self.row_winner() == True or self.growing_diagonal_winner() == True or self.decreasing_diagonal_winner() == True:
            self.game_winner = True
            return True
        else:
            self.game_winner = False
            return False


#Inicio del juego
def main():
    game = Game()
    print("\n...4 EN LÍNEA...")
    
    while game.playing:

        if game.player == True:
            print('\nTurno del Jugador 1')
        else:
            print('\nTurno del Jugador 2')
        col = int(input("\nIngresar la ficha [1|2|3|4|5|6|7|8]: "))
        
        try:
            game.insert_token(col-1)
            print('\n| 1 || 2 || 3 || 4 || 5 || 6 || 7 || 8 |')
            for row in game.board:
                print(row)
        except FullColumn:
            print('Vuelva a ingresar una ficha')
        except ColumnOutOfRange:
            print('Vuelva a ingresar una ficha')
        

        if game.game_winner == True: 
            if game.player == True:
                print(f'\n¡Jugador 1 has ganado!')
            else:
                print(f'\n¡Jugador 2 has ganado!')
            game.playing = False
    
    play_again = input('\n¿Revancha? (Y/N): ')
    
    while play_again != 'y' and play_again != 'n':
        play_again = input('\n¿Revancha? (Y/N): ')

    if play_again.lower() == 'y':
            main()
    else:
        print('\n¡Gracias por jugar!')

if __name__ == '__main__':
    main()