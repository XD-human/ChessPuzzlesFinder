from chess import Board
from puzzle_finder import PuzzleFinder


if __name__ == "__main__":
    # with open("games/lichess_pgn_2021.10.19_ArniZappa_vs_nilsonneuhaus.cn5KpVy5.pgn") as pgn:
    #     finder = PuzzleFinder()
    #     finder.load(pgn)
    #     puzzles = finder.find_puzzles()
    #     puzzles.sort(key=lambda puzzle: len(puzzle.moves), reverse=True)
    #
    #     for found_puzzle in puzzles:
    #         found_puzzle.print()
    #         print()
    board = Board("r1bq1rk1/1pp2ppp/p1n1p3/3n2N1/3P3Q/2PB4/PP1N2PP/R4RK1 b - - 0 13")
    PuzzleFinder.find_puzzle_in_position(board).print()
