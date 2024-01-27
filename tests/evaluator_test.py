import unittest
from chess import Board, Move
from evaluator import Evaluator


class FindGreatMoveTest(unittest.TestCase):
    def test_great_move_cp(self):
        fen = "8/8/4p3/2b1P1P1/3kNK2/3p3P/8/8 w - - 1 51"
        board = Board(fen)
        great_move = Evaluator.find_great_move(board)
        self.assertEqual(great_move, Move.from_uci("e4c5"))

    def test_great_move_mate_vs_cp(self):
        fen = "r4rk1/ppp3pp/3p1p2/8/3QPn1q/P1N2K2/1PP1BP2/R1B2R2 b - - 0 1"
        board = Board(fen)
        great_move = Evaluator.find_great_move(board)
        self.assertEqual(great_move, Move.from_uci("h4h3"))

    def test_great_move_mate(self):
        fen = "4Q3/2R2p1k/p2p1Ppp/1p6/5N2/P2r1r2/7K/8 w - - 2 40"
        board = Board(fen)
        great_move = Evaluator.find_great_move(board, mate_moves_diff=1)
        self.assertEqual(great_move, Move.from_uci("c7f7"))

    def test_great_move_cp_blacks_turn(self):
        fen = "8/8/7p/4p1p1/nk2P1P1/2p1BP1P/2K5/8 b - - 1 58"
        board = Board(fen)
        great_move = Evaluator.find_great_move(board)
        self.assertEqual(great_move, Move.from_uci("a4b2"))

    def test_no_great_move(self):
        fen = "rnbq1bnr/ppp3p1/6kp/3BQ3/4P2P/8/PPPP1PP1/RNB1K2R w KQ - 0 9"
        board = Board(fen)
        great_move = Evaluator.find_great_move(board)
        self.assertEqual(great_move, None)


class FindBestMoveTest(unittest.TestCase):
    def test_best_move_w(self):
        fen = "8/8/4p3/2b1P1P1/3kNK2/3p3P/8/8 w - - 1 51"
        board = Board(fen)
        best_move = Evaluator.find_best_move(board)
        self.assertEqual(best_move, Move.from_uci("e4c5"))

    def test_best_move_b(self):
        fen = "r1bqk1nr/pppp1ppp/2n5/2b1p3/2B1P3/2P2N2/PP1P1PPP/RNBQK2R b KQkq - 0 4"
        board = Board(fen)
        best_move = Evaluator.find_best_move(board)
        self.assertEqual(best_move, Move.from_uci("g8f6"))


if __name__ == '__main__':
    unittest.main()
