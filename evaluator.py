from chess import Board, Move, WHITE, BLACK
from stockfish import Stockfish


class Evaluator:
    _engine = Stockfish(
        path="/stockfish/stockfish-windows-x86-64-modern.exe",
        depth=18,
        parameters={"Threads": 4, "Hash": 2048},
    )

    @classmethod
    def find_great_move(
            cls,
            board: Board,
            cp_diff: int = 150,
            mate_moves_diff: int = 3
    ) -> Move | None:
        """
        Finds great move on the given board

        :param board: Board to find great move
        :param cp_diff: Amount of centipawns that differ great move from the second-best move (100 by default)
        :param mate_moves_diff: Number of moves to mate that differ the best move from the second-best move (default 1)
        :return: Great move if exists (else None)
        """
        fen = board.fen()
        cls._engine.set_fen_position(fen)
        top_moves = cls._engine.get_top_moves(2)
        if len(top_moves) == 0:
            return None
        elif len(top_moves) == 1:
            return Move.from_uci(top_moves[0]["Move"])

        first_move, second_move = top_moves

        # Best moves can contain this information
        # {'Move': 'f5h7', 'Centipawn': None, 'Mate': 1},
        # {'Move': 'f5d7', 'Centipawn': 713, 'Mate': None},

        if first_move["Mate"] is not None:
            # If the color to move will be mated, there is no great move.
            if Evaluator.eval_for_moving_color(board, first_move["Mate"]) < 0:
                return None

            # abs() is used to ignore which side is it to move
            if second_move["Mate"]:
                if abs(second_move["Mate"] - first_move["Mate"]) >= mate_moves_diff:
                    return Move.from_uci(first_move["Move"])
            else:
                return Move.from_uci(first_move["Move"])
        else:
            # If the color to move is losing, there is no great move.
            if Evaluator.eval_for_moving_color(board, first_move["Centipawn"]) < -300:
                return None

            if second_move["Centipawn"] is not None:
                if abs(first_move["Centipawn"] - second_move["Centipawn"]) >= cp_diff:
                    return Move.from_uci(first_move["Move"])
            else:
                return Move.from_uci(first_move["Move"])

    @classmethod
    def find_best_move(cls, board: Board) -> Move | None:
        """
        Find the best move on the board

        :param board: Board to find the best move
        :return: Best move
        """
        fen = board.fen()
        cls._engine.set_fen_position(fen)
        best_move = cls._engine.get_best_move()
        if best_move is None:
            return None
        return Move.from_uci(best_move)

    @staticmethod
    def eval_for_moving_color(board: Board, evaluation: int) -> int:
        """
        Evaluate the position for the color to move

        :param board: Board instance with the evaluated position
        :param evaluation: Amount of moves to mate or centipawns
        :return: Evaluation for the moving color
        (positive evaluation means that the moving color is better, otherwise it's worse)
        """
        if board.turn == WHITE:
            return evaluation
        else:
            return evaluation * -1
