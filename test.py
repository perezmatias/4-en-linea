import unittest
from cuatro_en_linea import *

class testCuatroEnLinea(unittest.TestCase):
    def test_board(self):
        game = Game()
        self.assertEqual(len(game.board), 8)
        self.assertEqual(len(game.board[0]), 8)
    
    def test_player_change(self):
        game = Game()
        game.player_change()
        self.assertEqual(game.player, False)
        game.player_change()
        self.assertEqual(game.player, True)

    def test_insert_token(self):
        game = Game()
        game.insert_token(3)
        game.insert_token(5)
        game.insert_token(6)
        game.insert_token(6)
        self.assertEqual(game.board[7][3],"x")
        self.assertEqual(game.board[7][5],"o")
        self.assertEqual(game.board[7][6],"x")
        self.assertEqual(game.board[6][6],"o")
        with self.assertRaises(ColumnOutOfRange):
            game.insert_token(9)
        
        with self.assertRaises(FullColumn):
            game.insert_token(3)
            game.insert_token(3)
            game.insert_token(3)
            game.insert_token(3)
            game.insert_token(3)
            game.insert_token(3)
            game.insert_token(3)
            game.insert_token(3)
            game.insert_token(3)
    
    def test_column_winner(self):
        game = Game()
        game.insert_token(3)
        game.insert_token(5)
        game.insert_token(3)
        game.insert_token(6)
        game.insert_token(3)
        game.insert_token(7)
        game.insert_token(3)
        self.assertEqual(game.column_winner(), True)
    
    def test_row_winner(self):
        game = Game()
        game.insert_token(3)
        game.insert_token(1)
        game.insert_token(4)
        game.insert_token(1)
        game.insert_token(5)
        game.insert_token(3)
        game.insert_token(6)
        game.insert_token(6)
        self.assertEqual(game.row_winner(),True)
    
    def test_decreasing_diagonal_winner(self):
        game = Game()
        game.insert_token(3)#x
        game.insert_token(3)#o
        game.insert_token(3)#x
        game.insert_token(3)#o
        game.insert_token(4)#x
        game.insert_token(4)#o
        game.insert_token(5)#x
        game.insert_token(4)#o
        game.insert_token(7)#x
        game.insert_token(5)#o
        game.insert_token(7)#x
        game.insert_token(6)#o
        self.assertEqual(game.decreasing_diagonal_winner(),True)

    def test_growing_diagonal_winner(self):
        game = Game()
        game.insert_token(0)#x
        game.insert_token(1)#o
        game.insert_token(1)#x
        game.insert_token(2)#o
        game.insert_token(2)#x
        game.insert_token(3)#o
        game.insert_token(2)#x
        game.insert_token(3)#o
        game.insert_token(3)#x
        game.insert_token(5)#o
        game.insert_token(3)#x
        self.assertEqual(game.growing_diagonal_winner(),True)

    def test_growing_diagonal_winner2(self):
        game = Game()
        game.insert_token(0)
        game.insert_token(1)
        game.insert_token(2)
        game.insert_token(3)
        game.insert_token(4)
        game.insert_token(5)
        game.insert_token(6)
        game.insert_token(7)
        game.insert_token(0)
        game.insert_token(1)
        game.insert_token(2)
        game.insert_token(3)
        game.insert_token(5)
        game.insert_token(6)
        game.insert_token(7)
        game.insert_token(0)
        game.insert_token(1)
        game.insert_token(2)
        game.insert_token(3)
        game.insert_token(4)
        game.insert_token(5)
        game.insert_token(6)
        game.insert_token(7)
        game.insert_token(0)
        game.insert_token(1)
        game.insert_token(0)
        game.insert_token(2)
        game.insert_token(0)
        game.insert_token(1)
        game.insert_token(0)
        game.insert_token(3)
        self.assertEqual(game.column_winner(), True)
        self.assertEqual(game.row_winner(), False)
        self.assertEqual(game.growing_diagonal_winner(), False)
        self.assertEqual(game.decreasing_diagonal_winner(), False)

if __name__ == '__main__':
    unittest.main()