from chess import Board
from puzzle_finder import PuzzleFinder


if __name__ == "__main__":
    # with open("games/lichess_pgn_2023.08.17_michaelmaue_vs_xDhuman.9X4ApmjF.pgn") as pgn:
    #     finder = PuzzleFinder()
    #     finder.load(pgn)
    #     puzzles = finder.find_puzzles()
    #     puzzles.sort(key=lambda puzzle: len(puzzle.moves), reverse=True)
    #
    #     for found_puzzle in puzzles:
    #         found_puzzle.print()
    #         print()
    #     print(f"Found {len(puzzles)} puzzles")
    board = Board("2r3k1/5ppp/4p3/p7/Pp1N4/1P6/2b2KPP/4R3 w - - 2 32")
    PuzzleFinder.find_puzzle_in_position(board).print()
