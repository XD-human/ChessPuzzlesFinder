from chess import Move, Board, BLACK


class PuzzleMove:
    def __init__(self, winner_move: Move, loser_move: Move):
        self.winner_move = winner_move
        self.loser_move = loser_move


class Puzzle:
    def __init__(self, fen: str, moves: list[PuzzleMove]):
        """
        Class representing a chess puzzle.

        :param fen: Starting position in FEN notation
        :param moves: List containing winner's and loser's moves in the PuzzleMove class
        """
        self.fen = fen
        self.moves = moves

    def print(self):
        """
        Print in stdout formatted puzzle.

        :return: None
        """
        board = Board(self.fen)
        print(board)
        print(self.fen)
        moves = self.moves
        first_move: PuzzleMove = moves[0]

        if board.turn == BLACK:
            print(f"1... {first_move.winner_move.uci()}")
            move_idx = 2
            for i, move in enumerate(moves):
                if i + 1 < len(moves):
                    winner_move = moves[i + 1].winner_move.uci()
                else:
                    winner_move = ""
                print(f"{move_idx}. {move.loser_move.uci()} {winner_move}")
                move_idx += 1
        else:
            move_idx = 1
            for move in self.moves:
                print(f"{move_idx}. {move.winner_move.uci()} {move.loser_move.uci()}")
                move_idx += 1

    def add_move(self, move: PuzzleMove):
        """
        Add a move to the puzzle

        :param move: PuzzleMove instance containing winner's and loser's moves
        :return: None
        """
        self.moves.append(move)

    def should_save_puzzle(self) -> bool:
        """
        Determine if the puzzle is worth saving

        :return: True if the chess puzzle should be saved, otherwise False
        """
        return bool(self.moves)

    @classmethod
    def create_only_pgn(cls, fen):
        """
        Create the chess puzzle containing no moves and only PGN.

        :param fen: FEN of the starting position
        :return: The chess puzzle with given PGN
        """
        return cls(fen, [])
