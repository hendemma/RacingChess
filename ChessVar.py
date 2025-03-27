class Piece:
    """
    A class that represents a piece in chess.
    """

    def __init__(self, name, color, icon):
        """
        Creates Piece object with a name, color and icon.
        """
        self._name = name
        self._color = color
        self._icon = icon

    def get_icon(self):
        """ Returns the Piece icon. """
        return self._icon

    def get_color(self):
        """ Returns the Piece color. """
        return self._color

    def get_name(self):
        """ Returns the Piece name. """
        return self._name


class ChessVar:
    """
    A class that represents a variant of chess.
    """

    def __init__(self):
        """
        Creates ChessVar object. Initializes white_turn to True, game_status to UNFINISHED,
        the pieces to Piece objects, and board dictionary to starting setup.
        """
        self._white_turn = True
        self._game_status = 'UNFINISHED'
        self._blank_space = Piece('blank', 'none', "_")
        self._white_king = Piece('king', 'white', "\u2654")
        self._white_rook = Piece('rook', 'white', "\u2656")
        self._white_bishop = Piece('bishop', 'white', "\u2657")
        self._white_knight = Piece('knight', 'white', "\u2658")
        self._black_king = Piece('king', 'black', "\u265A")
        self._black_rook = Piece('rook', 'black', "\u265C")
        self._black_bishop = Piece('bishop', 'black', "\u265D")
        self._black_knight = Piece('knight', 'black', "\u265E")
        self._board = {
            "a1": self._white_king,
            "a2": self._white_rook,
            "a3": self._blank_space,
            "a4": self._blank_space,
            "a5": self._blank_space,
            "a6": self._blank_space,
            "a7": self._blank_space,
            "a8": self._blank_space,
            "b1": self._white_bishop,
            "b2": self._white_bishop,
            "b3": self._blank_space,
            "b4": self._blank_space,
            "b5": self._blank_space,
            "b6": self._blank_space,
            "b7": self._blank_space,
            "b8": self._blank_space,
            "c1": self._white_knight,
            "c2": self._white_knight,
            "c3": self._blank_space,
            "c4": self._blank_space,
            "c5": self._blank_space,
            "c6": self._blank_space,
            "c7": self._blank_space,
            "c8": self._blank_space,
            "d1": self._blank_space,
            "d2": self._blank_space,
            "d3": self._blank_space,
            "d4": self._blank_space,
            "d5": self._blank_space,
            "d6": self._blank_space,
            "d7": self._blank_space,
            "d8": self._blank_space,
            "e1": self._blank_space,
            "e2": self._blank_space,
            "e3": self._blank_space,
            "e4": self._blank_space,
            "e5": self._blank_space,
            "e6": self._blank_space,
            "e7": self._blank_space,
            "e8": self._blank_space,
            "f1": self._black_knight,
            "f2": self._black_knight,
            "f3": self._blank_space,
            "f4": self._blank_space,
            "f5": self._blank_space,
            "f6": self._blank_space,
            "f7": self._blank_space,
            "f8": self._blank_space,
            "g1": self._black_bishop,
            "g2": self._black_bishop,
            "g3": self._blank_space,
            "g4": self._blank_space,
            "g5": self._blank_space,
            "g6": self._blank_space,
            "g7": self._blank_space,
            "g8": self._blank_space,
            "h1": self._black_king,
            "h2": self._black_rook,
            "h3": self._blank_space,
            "h4": self._blank_space,
            "h5": self._blank_space,
            "h6": self._blank_space,
            "h7": self._blank_space,
            "h8": self._blank_space,
        }

    def create_board(self):
        """
        Method takes no parameters and returns nothing.
        Prints the self._board dictionary as a chessboard visual.
        """
        print(f"      a   b   c   d   e   f   g   h  ")
        for i in reversed(range(8)):
            print(
                f"  {i + 1} | {self._board[f'a{i + 1}'].get_icon()} | {self._board[f'b{i + 1}'].get_icon()} | {self._board[f'c{i + 1}'].get_icon()} | {self._board[f'd{i + 1}'].get_icon()} | {self._board[f'e{i + 1}'].get_icon()} | {self._board[f'f{i + 1}'].get_icon()} | {self._board[f'g{i + 1}'].get_icon()} | {self._board[f'h{i + 1}'].get_icon()} |")

    def make_move(self, current, next):
        """
        Takes a current and next location as parameters.
        Checks if piece is able to move and calls move_check, put_opp_king_in_check and put_your_king_in_check methods.
        If not able to move, returns False.
        If able to move, moves piece in board dictionary, updates game status by calling update_game_state method,
        switches player turn and returns True.
        """

        # if the game is over, no more moves can be made.
        if self._game_status != 'UNFINISHED':
            return False

        # if white player's turn
        if self._white_turn is True:
            # if white tries to move black's piece
            if self._board[current].get_color() == "black":
                return False
            # if white tries to move where their piece is already
            elif self._board[next].get_color() == "white":
                return False
        # if black player's turn
        elif self._white_turn is False:
            # if black tries to move white's piece
            if self._board[current].get_color() == "white":
                return False
            # if black tries to move where their piece is already
            elif self._board[next].get_color() == "black":
                return False

        # call methods to check piece's moving path and if a king will be in check.
        piece_results = self.move_check(self._board, current, next)
        opp_king_results = self.put_opp_king_in_check(current, next)
        your_king_results = self.put_your_king_in_check(current, next)

        # if the move is possible/allowed
        if piece_results is True and opp_king_results is True and your_king_results is True:
            self._board[next] = self._board[current]  # moves piece to new location (erasing any piece that is there)
            self._board[current] = self._blank_space  # resets old location to blank
            #self.create_board()

            # if white player's turn
            if self._white_turn is True:
                # switch to black player's turn
                self._white_turn = False
                return True
            # if black player's turn
            if self._white_turn is False:
                # update game if necessary
                update_game = self.update_game_state()
                self._white_turn = True
                return True
        else:
            return False

    def move_check(self, board, current, next):
        """
        Takes a board and current and next locations as parameters.
        Checks what type of piece is being moved and returns the correct method.
        Otherwise, returns False.
        """
        if board[current].get_name() == "rook":
            return self.move_rook(board, current, next)
        elif board[current].get_name() == "bishop":
            return self.move_bishop(board, current, next)
        elif board[current].get_name() == "knight":
            return self.move_knight(current, next)
        elif board[current].get_name() == "king":
            return self.move_king(current, next)
        else:  # if piece is blank
            return False

    def move_rook(self, board, current, next):
        """
        Takes a board and current and next locations as parameters.
        If the rook can be moved, returns True. If not, returns False.
        """
        results = False

        # if there is a piece in the way if the move is vertical
        if current[0] == next[0]:
            for piece in board:
                if board[piece] != self._blank_space:  # if piece is not a blank space
                    if piece[0] == current[0] and piece[1] != current[1]:
                        on_path = piece  # piece on the path of the move
                        if current[1] < next[1]:  # if the move is going up
                            # if the piece is before the next location
                            if next[1] > on_path[1] > current[1]:
                                return False
                        elif current[1] > next[1]:  # if the move is going down
                            # if the piece is before the next location
                            if next[1] < on_path[1] < current[1]:
                                return False

        # if there is a piece in the way if the move is horizontal
        if current[1] == next[1]:
            for piece in board:
                if board[piece] != self._blank_space:  # if piece is not a blank space
                    if piece[1] == current[1] and piece[0] != current[0]:
                        on_path = piece  # piece on the path of the move
                        if current[0] < next[0]:  # if the move is going right
                            # if the piece is before the next location
                            if next[0] > on_path[0] > current[0]:
                                return False
                        elif current[0] > next[0]:  # if the move is going left
                            # if the piece is before the next location
                            if next[0] < on_path[0] < current[0]:
                                return False

        # if piece moves up, down, left, right any amount of spaces
        if current[0] == next[0] or current[1] == next[1]:
            results = True
        return results

    def move_bishop(self, board, current, next):
        """
        Takes a board and current and next locations as parameters.
        If the bishop can be moved, returns True. If not, returns False.
        """
        results = False

        # check if there is a piece in the way
        for index in range(1, 8):  # for every row of board
            for piece in board:
                if board[piece] != self._blank_space:  # if piece is not a blank space
                    # if piece there is a piece in the way diagonal right/forward
                    if ord(current[0]) + index == ord(piece[0]) and int(current[1]) + index == int(piece[1]):
                        on_path = piece  # piece on the path of move
                        # if the piece is before the next location
                        if on_path[0] < next[0] and on_path[1] < next[1]:
                            return False
                    # if piece there is a piece in the way diagonal left/forward
                    if ord(current[0]) - index == ord(piece[0]) and int(current[1]) + index == int(piece[1]):
                        on_path = piece  # piece on the path of move
                        # if the piece is before the next location
                        if on_path[0] > next[0] and on_path[1] < next[1]:
                            return False
                    # if piece there is a piece in the way diagonal left/backward
                    if ord(current[0]) - index == ord(piece[0]) and int(current[1]) - index == int(piece[1]):
                        on_path = piece  # piece on the path of move
                        # if the piece is before the next location
                        if on_path[0] > next[0] and on_path[1] > next[1]:
                            return False
                    # if piece there is a piece in the way diagonal right/backward
                    if ord(current[0]) + index == ord(piece[0]) and int(current[1]) - index == int(piece[1]):
                        on_path = piece  # piece on the path of move
                        # if the piece is before the next location
                        if on_path[0] < next[0] and on_path[1] > next[1]:
                            return False

            # if piece moves diagonal right/forward any amount of spaces.
            if ord(current[0]) + index == ord(next[0]) and int(current[1]) + index == int(next[1]):
                results = True
            # if piece moves diagonal left/forward any amount of spaces.
            elif ord(current[0]) - index == ord(next[0]) and int(current[1]) + index == int(next[1]):
                results = True
            # if piece moves diagonal left/backward any amount of spaces.
            elif ord(current[0]) - index == ord(next[0]) and int(current[1]) - index == int(next[1]):
                results = True
            # if piece moves diagonal right/backward any amount of spaces.
            elif ord(current[0]) + index == ord(next[0]) and int(current[1]) - index == int(next[1]):
                results = True
        return results

    def move_knight(self, current, next):
        """
        Takes current and next locations as parameters.
        If the knight can be moved, returns True. If not, returns False.
        """
        results = False
        # if piece moves up two and over one to the right
        if ord(current[0]) + 1 == ord(next[0]) and int(current[1]) + 2 == int(next[1]):
            results = True
        # if piece moves down two and over one to the right
        elif ord(current[0]) + 1 == ord(next[0]) and int(current[1]) - 2 == int(next[1]):
            results = True
        # if piece moves up one and over two to the right
        elif ord(current[0]) + 2 == ord(next[0]) and int(current[1]) + 1 == int(next[1]):
            results = True
        # if piece moves down one and over two to the right
        elif ord(current[0]) + 2 == ord(next[0]) and int(current[1]) - 1 == int(next[1]):
            results = True
        # if piece moves up two and over one to the left
        elif ord(current[0]) - 1 == ord(next[0]) and int(current[1]) + 2 == int(next[1]):
            results = True
        # if piece moves down two and over one to the left
        elif ord(current[0]) - 1 == ord(next[0]) and int(current[1]) - 2 == int(next[1]):
            results = True
        # if piece moves up one and over two to the left
        elif ord(current[0]) - 2 == ord(next[0]) and int(current[1]) + 1 == int(next[1]):
            results = True
        # if piece moves down one and over two to the left
        elif ord(current[0]) - 2 == ord(next[0]) and int(current[1]) - 1 == int(next[1]):
            results = True
        return results

    def move_king(self, current, next):
        """
        Takes current and next locations as parameters.
        If the king can be moved, returns True. If not, returns False.
        """
        results = False
        # if piece moves up one
        if ord(current[0]) == ord(next[0]) and int(current[1]) + 1 == int(next[1]):
            results = True
        # if piece moves down one
        elif ord(current[0]) == ord(next[0]) and int(current[1]) - 1 == int(next[1]):
            results = True
        # if piece moves to the right one
        elif ord(current[0]) + 1 == ord(next[0]) and int(current[1]) == int(next[1]):
            results = True
        # if piece moves to the left one
        elif ord(current[0]) - 1 == ord(next[0]) and int(current[1]) == int(next[1]):
            results = True
        # if piece moves diagonal upper right one
        elif ord(current[0]) + 1 == ord(next[0]) and int(current[1]) + 1 == int(next[1]):
            results = True
        # if piece moves diagonal lower right one
        elif ord(current[0]) + 1 == ord(next[0]) and int(current[1]) - 1 == int(next[1]):
            results = True
        # if piece moves diagonal lower left one
        elif ord(current[0]) - 1 == ord(next[0]) and int(current[1]) - 1 == int(next[1]):
            results = True
        # if piece moves diagonal upper left one
        elif ord(current[0]) - 1 == ord(next[0]) and int(current[1]) + 1 == int(next[1]):
            results = True
        return results

    def find_king(self, board, king):
        """
        Takes a board and a king as parameters.
        Returns the location of the king in the board.
        """
        location = None
        for piece in board:
            if board[piece] == king:
                location = piece
        return location

    def copy_board(self, current, next):
        """
        Takes current and next locations as parameters.
        Makes a copy of the board dictionary and moves the piece in the copy.
        Returns the copy of the board.
        """
        board_copy = dict(self._board)
        board_copy[next] = board_copy[current]
        board_copy[current] = self._blank_space
        return board_copy

    def put_opp_king_in_check(self, current, next):
        """
        Takes current and next locations as parameters.
        Makes a copy of the board dictionary, moves the piece by calling copy_board method
        Finds location of kings by calling find_king method.
        Checks if the next move would hit the opponents king by calling move_check method.
        If so, returns False. Otherwise, returns True.
        """

        # make copy of the board and move piece
        board_copy = self.copy_board(current, next)

        # find location of kings
        white_king_loc = self.find_king(board_copy, self._white_king)
        black_king_loc = self.find_king(board_copy, self._black_king)

        # if it is white player's turn
        if self._white_turn is True:
            # check if next move can hit black player's king
            move_results = self.move_check(board_copy, next, black_king_loc)
            if move_results is True:
                return False
            else:
                return True
        # if it is black player's turn
        if self._white_turn is False:
            # check if next move can hit white player's king
            move_results = self.move_check(board_copy, next, white_king_loc)
            if move_results is True:
                return False
            else:
                return True

    def put_your_king_in_check(self, current, next):
        """
        Takes current and next locations as parameters.
        Makes a copy of the board dictionary, moves the piece by calling copy_board method
        Finds location of kings by calling find_king method.
        Checks if there are any pieces on the board that can now hit your king.
        If so, returns False. Otherwise, returns True.
        """

        # make copy of the board and move piece
        board_copy = self.copy_board(current, next)

        # find location of kings
        white_king_loc = self.find_king(board_copy, self._white_king)
        black_king_loc = self.find_king(board_copy, self._black_king)

        # if it is white player's turn
        if self._white_turn is True:
            for piece in board_copy:
                if board_copy[piece].get_color() == "black":  # find all black pieces
                    # check if black piece can hit white king
                    move_results_2 = self.move_check(board_copy, piece, white_king_loc)
                    if move_results_2 is True:
                        return False
        # if it is black player's turn
        if self._white_turn is False:
            for piece in board_copy:
                if board_copy[piece].get_color() == "white":  # find all white pieces
                    # check if white piece can hit black king
                    move_results_2 = self.move_check(board_copy, piece, black_king_loc)
                    if move_results_2 is True:
                        return False
        return True

    def update_game_state(self):
        """
        Takes no parameters.
        Checks if either king has made it to the 8th row of the board.
        If so, updates the game status. Returns game status.
        """
        white_king_loc = self.find_king(self._board, self._white_king)
        black_king_loc = self.find_king(self._board, self._black_king)

        # if black king has made it to the 8th row but white king has not
        if black_king_loc[1] == "8" and white_king_loc[1] != "8":
            self._game_status = 'BLACK_WON'
        # if both the black and white king have made it to the 8th row
        elif black_king_loc[1] == "8" and white_king_loc[1] == "8":
            self._game_status = 'TIE'
        # if white king has made it to the 8th row but black king has not
        elif black_king_loc[1] != "8" and white_king_loc[1] == "8":
            self._game_status = 'WHITE_WON'
        else:
            self._game_status = 'UNFINISHED'
        return self._game_status

    def get_game_state(self):
        """
        Takes no parameters. Returns the status of the game.
        """
        return self._game_status
