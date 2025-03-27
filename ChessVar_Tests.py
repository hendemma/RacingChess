import unittest
from ChessVar import Piece, ChessVar


class TestChessVar(unittest.TestCase):
    """ Contains unit tests for ChessVar class. """
    def test_1(self):
        """ Tests various game moves. """
        game = ChessVar()
        self.assertEqual(game.make_move("a2", "a3"), True)      # rook up
        self.assertEqual(game.make_move("g2", "h3"), True)      # bishop up/right diagonal
        self.assertEqual(game.make_move("c2", "b4"), True)      # knight up 2, left 1
        self.assertEqual(game.make_move("h3", "g4"), True)      # bishop up/left diagonal
        self.assertEqual(game.make_move("a1", "a2"), True)      # king up
        self.assertEqual(game.make_move("g4", "f3"), True)      # bishop down/left diagonal
        self.assertEqual(game.make_move("a3", "g3"), False)     # rook right jump
        self.assertEqual(game.make_move("c1", "d3"), True)      # knight up 2, right 1
        self.assertEqual(game.make_move("g1", "e3"), False)     # bishop up/left jump
        self.assertEqual(game.make_move("f1", "d2"), True)      # knight up 1, right 2
        self.assertEqual(game.make_move("b2", "c1"), True)      # bishop down/right diagonal
        self.assertEqual(game.make_move("g1", "g2"), False)     # bishop wrong move
        self.assertEqual(game.make_move("h2", "g2"), True)      # rook left
        self.assertEqual(game.make_move("c1", "e3"), False)     # bishop up/right jump
        self.assertEqual(game.make_move("a2", "b2"), True)      # king right
        self.assertEqual(game.make_move("g2", "e2"), False)     # rook left jump
        self.assertEqual(game.make_move("a3", "a4"), False)     # black move white's piece
        self.assertEqual(game.make_move("g2", "h2"), True)      # rook right
        self.assertEqual(game.make_move("b2", "b3"), False)     # white put own king in check with king
        self.assertEqual(game.make_move("d3", "e1"), True)      # knight down 2, right 1
        self.assertEqual(game.make_move("h1", "g2"), False)     # black put own king in check with king

    def test_2(self):
        """ Tests the game ending in a tie. """
        game = ChessVar()
        self.assertEqual(game.make_move("a2", "a4"), True)      # rook up
        self.assertEqual(game.make_move("g2", "a8"), True)      # bishop up/left diagonal
        self.assertEqual(game.make_move("a1", "a2"), True)      # king up
        self.assertEqual(game.make_move("h2", "h4"), True)      # rook up
        self.assertEqual(game.make_move("a2", "a3"), True)      # king up
        self.assertEqual(game.make_move("a8", "b7"), True)      # bishop down/right diagonal
        self.assertEqual(game.make_move("a4", "b4"), True)      # rook right
        self.assertEqual(game.make_move("h1", "h2"), True)      # king up
        self.assertEqual(game.make_move("a3", "a4"), True)      # king up
        self.assertEqual(game.make_move("b7", "c8"), True)      # bishop up/right diagonal
        self.assertEqual(game.make_move("b4", "b5"), False)     # white put own king in check with other piece
        self.assertEqual(game.make_move("a4", "a5"), True)
        self.assertEqual(game.make_move("h2", "g3"), True)
        self.assertEqual(game.make_move("b4", "b5"), True)
        self.assertEqual(game.make_move("g3", "g4"), True)
        self.assertEqual(game.make_move("b5", "b3"), True)
        self.assertEqual(game.make_move("g4", "g5"), True)
        self.assertEqual(game.make_move("b2", "a1"), True)
        self.assertEqual(game.make_move("c8", "h3"), True)
        self.assertEqual(game.make_move("a5", "a6"), True)
        self.assertEqual(game.make_move("g5", "g6"), True)
        self.assertEqual(game.make_move("b3", "b2"), True)
        self.assertEqual(game.make_move("g1", "h2"), True)
        self.assertEqual(game.make_move("a6", "a7"), True)
        self.assertEqual(game.make_move("g6", "g7"), True)
        self.assertEqual(game.make_move("a7", "a8"), True)      # white makes winning move
        self.assertEqual(game.get_game_state(), 'UNFINISHED')   # check game status is still unfinished
        self.assertEqual(game.make_move("g7", "g8"), True)      # black makes winning move
        self.assertEqual(game.get_game_state(), 'TIE')          # check game is tie
        self.assertEqual(game.make_move("b2", "a2"), False)     # check no more moves can be made

    def test_3(self):
        """ Tests various game moves. """
        game = ChessVar()
        self.assertEqual(game.make_move("a2", "a8"), True)      # rook up
        self.assertEqual(game.make_move("g2", "b7"), True)      # bishop up/left diagonal
        self.assertEqual(game.make_move("a1", "a2"), True)      # king up
        self.assertEqual(game.make_move("f2", "d1"), True)      # knight down 1, left 2
        self.assertEqual(game.make_move("a2", "a3"), True)      # king up
        self.assertEqual(game.make_move("h2", "h3"), False)     # black put white king in check
        self.assertEqual(game.make_move("h4", "h4"), False)     # same current and next
        self.assertEqual(game.make_move("h2", "h1"), False)     # black move where black piece is
        self.assertEqual(game.make_move("h1", "g2"), True)      # king upper left
        self.assertEqual(game.make_move("b2", "d4"), True)      # bishop up/right diagonal
        self.assertEqual(game.make_move("b7", "h1"), False)     # bishop down/right jump
        self.assertEqual(game.make_move("g2", "g3"), True)      # king up
        self.assertEqual(game.make_move("d4", "e5"), False)     # white put black in check
        self.assertEqual(game.make_move("a8", "a7"), True)      # rook down
        self.assertEqual(game.make_move("g3", "f3"), True)      # king left
        self.assertEqual(game.make_move("a7", "a1"), False)     # rook down jump
        self.assertEqual(game.make_move("a3", "b4"), True)      # king upper right
        self.assertEqual(game.make_move("f3", "g2"), True)      # king lower right
        self.assertEqual(game.make_move("d4", "g1"), True)      # bishop down/right capture
        self.assertEqual(game.make_move("g2", "g1"), True)      # king down capture
        self.assertEqual(game.make_move("c2", "e1"), True)      # knight down 1, right 2
        self.assertEqual(game.make_move("f1", "d2"), True)      # knight up 1, left 2
        self.assertEqual(game.make_move("h2", "h3"), False)     # white move black piece

    def test_4(self):
        """ Tests the game ending in white winning. """
        game = ChessVar()
        self.assertEqual(game.make_move("a2", "a8"), True)
        self.assertEqual(game.make_move("h2", "h8"), True)
        self.assertEqual(game.make_move("a1", "a2"), True)
        self.assertEqual(game.make_move("h1", "h2"), True)
        self.assertEqual(game.make_move("a2", "a3"), True)
        self.assertEqual(game.make_move("h2", "h3"), True)
        self.assertEqual(game.make_move("a3", "a4"), True)
        self.assertEqual(game.make_move("h3", "h4"), True)
        self.assertEqual(game.make_move("a4", "a5"), True)
        self.assertEqual(game.make_move("h4", "h5"), True)
        self.assertEqual(game.make_move("a5", "a6"), True)
        self.assertEqual(game.make_move("h5", "h6"), True)
        self.assertEqual(game.make_move("a6", "a7"), True)
        self.assertEqual(game.make_move("h8", "g8"), True)
        self.assertEqual(game.make_move("b2", "c3"), True)
        self.assertEqual(game.make_move("g8", "g4"), True)
        self.assertEqual(game.make_move("a7", "b8"), True)      # white makes winning move
        self.assertEqual(game.get_game_state(), 'UNFINISHED')   # check that game state is still unfinished
        self.assertEqual(game.make_move("h6", "h7"), True)      # black gets one more turn
        self.assertEqual(game.get_game_state(), 'WHITE_WON')    # check that white won
        self.assertEqual(game.make_move("b1", "a2"), False)     # check that no more moves can be made

    def test_5(self):
        """ Tests the game ending in black winning. """
        game = ChessVar()
        self.assertEqual(game.make_move("b2", "e5"), True)
        self.assertEqual(game.make_move("f2", "e4"), True)
        self.assertEqual(game.make_move("a2", "a5"), True)
        self.assertEqual(game.make_move("e4", "d2"), True)      # knight down 2, left 1
        self.assertEqual(game.make_move("a5", "c7"), False)     # rook move outside of path
        self.assertEqual(game.make_move("a5", "c5"), True)
        self.assertEqual(game.make_move("g2", "c6"), True)
        self.assertEqual(game.make_move("c5", "c7"), False)     # rook jump up
        self.assertEqual(game.make_move("c5", "b5"), True)
        self.assertEqual(game.make_move("c6", "a4"), False)     # bishop left/down jump
        self.assertEqual(game.make_move("h1", "g2"), True)
        self.assertEqual(game.make_move("b1", "c2"), False)     # white move piece where white is
        self.assertEqual(game.make_move("a1", "a2"), True)
        self.assertEqual(game.make_move("g1", "c5"), True)
        self.assertEqual(game.make_move("e5", "c3"), True)
        self.assertEqual(game.make_move("g2", "g3"), True)
        self.assertEqual(game.make_move("a2", "b2"), True)
        self.assertEqual(game.make_move("g3", "g4"), True)
        self.assertEqual(game.make_move("b2", "a1"), True)      # king lower left
        self.assertEqual(game.make_move("g4", "c4"), False)     # king move outside path
        self.assertEqual(game.make_move("g4", "g5"), True)
        self.assertEqual(game.make_move("c2", "d6"), False)     # knight move outside of path
        self.assertEqual(game.make_move("b1", "a2"), True)
        self.assertEqual(game.make_move("c5", "b6"), False)     # black put own king in check with another piece
        self.assertEqual(game.make_move("g5", "g6"), True)
        self.assertEqual(game.make_move("c3", "d2"), True)      # bishop capture knight
        self.assertEqual(game.make_move("g6", "g7"), True)
        self.assertEqual(game.make_move("a2", "b1"), True)
        self.assertEqual(game.make_move("g7", "g8"), True)      # black makes winning move
        self.assertEqual(game.get_game_state(), 'BLACK_WON')    # check game status changed to black won
        self.assertEqual(game.make_move("a1", "b2"), False)     # check no more moves can be made