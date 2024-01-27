import chess
from chess import Move, Board, BLACK


def piece_letter(piece: chess.PieceType | None) -> str:
    if piece == chess.PAWN:
        return ""
    elif piece == chess.KNIGHT:
        return "N"
    elif piece == chess.BISHOP:
        return "B"
    elif piece == chess.ROOK:
        return "R"
    elif piece == chess.QUEEN:
        return "Q"
    elif piece == chess.KING:
        return "K"

    raise ValueError(f"{piece} is not a piece")


def move_representation(board: Board, move: Move) -> str:
    """
    Creates a representation of a given move on a board
    :param board: Position with the move
    :param move: Move to represent
    :return: String of a move containing piece name
    """
    if board.is_checkmate():
        return "MATE"

    moved_piece = board.piece_type_at(move.from_square)
    letter = piece_letter(moved_piece)
    if board.is_capture(move):
        _move = letter + move.uci()[:2] + "x" + move.uci()[2:4]
    else:
        _move = letter + move.uci()[:2] + "-" + move.uci()[2:4]

    if move.promotion:
        _move += "=" + piece_letter(move.promotion)

    if board.gives_check(move):
        _move += "+"

    return _move


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
        Print in stdout formatted puzzle. If there is no moves in puzzle, nothing will happen.

        :return: None
        """
        if not self.moves:
            return None
        board = Board(self.fen)
        print(board)
        print(self.fen)
        moves = self.moves
        first_move: PuzzleMove = moves[0]

        if board.turn == BLACK:
            print(f"1... {move_representation(board, first_move.winner_move)}")
            board.push(first_move.winner_move)
            move_idx = 2
            for i, move in enumerate(moves):
                l_move = move.loser_move
                move_str = f"{move_idx}. {move_representation(board, l_move)} "
                board.push(l_move)

                if i + 1 < len(moves):
                    w_move = moves[i + 1].winner_move
                    move_str += move_representation(board, w_move)
                    board.push(w_move)
                print(move_str)
                move_idx += 1
        else:
            move_idx = 1
            for move in moves:
                w_move = move.winner_move
                move_str = f"{move_idx}. {move_representation(board, w_move)} "
                board.push(w_move)

                l_move = move.loser_move
                move_str += move_representation(board, l_move)
                board.push(l_move)
                print(move_str)
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
