from typing import TextIO

from chess import Board, Move
import chess.pgn
from puzzle import Puzzle, PuzzleMove
from evaluator import Evaluator


class PuzzleFinder:
    def __init__(self):
        self._game: chess.pgn.Game | None = None
        self._board = Board()
        self.puzzles = []

    def load(self, game_pgn: TextIO):
        """
        Load PGN of a chess game

        :param game_pgn: PGN of the chess game
        :return: None
        """
        self._game = chess.pgn.read_game(game_pgn)

    def find_puzzles(self) -> list[Puzzle]:
        """
        Find all the positions which are starting to puzzles in the chess game

        :return: List of found puzzles
        """
        if self._game is None:
            raise ValueError("Game PGN was not loaded. Please load PGN using load() method")
        puzzles_out = []
        i = 1.0
        for move in self._game.mainline_moves():
            found_str = ""
            _puzzle = self.find_puzzle_in_position(self._board)
            if _puzzle.should_save_puzzle():
                puzzles_out.append(_puzzle)
                found_str = "found puzzle"
            self._board.push(move)
            i += 0.5
            if i.is_integer():
                print(i, found_str)
        return puzzles_out

    @staticmethod
    def find_puzzle_in_position(_board: Board) -> Puzzle:
        """
        Find chess puzzle in given position
        :param _board: Board on which it's needed to find a chess puzzle
        :return: Puzzle instance representing the found puzzle
        """
        _board = _board.copy()
        _puzzle = Puzzle.create_only_pgn(_board.fen())
        while True:
            if _board.is_repetition() or _board.can_claim_draw():
                # If the position is drawn
                # stop building puzzle
                break

            winner_move = Evaluator.find_great_move(_board)
            if winner_move is None:
                # If there is no great move, stop building puzzle
                break

            _board.push(winner_move)
            loser_move = Evaluator.find_best_move(_board)
            if loser_move is None:
                # If this is checkmate, add the move and stop building puzzle
                move = PuzzleMove(winner_move, Move.null())
                _puzzle.add_move(move)
                break

            _board.push(loser_move)

            move = PuzzleMove(winner_move, loser_move)
            _puzzle.add_move(move)

        return _puzzle
