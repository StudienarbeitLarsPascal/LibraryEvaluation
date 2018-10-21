# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 21:38:59 2018

@author: Schroeder
"""
import chess
import chess.svg

from IPython.display import SVG

board = chess.Board()

print("Please enter field:")
field = input()
    
# extracts moves starting from input
movesFromSpecField = list(filter(lambda move: move.from_square is chess.SQUARE_NAMES.index(field), board.legal_moves))
# maps targeted squares from specified field
squareNums = list(map(lambda move: move.to_square, movesFromSpecField))

# creates square set and adds every targeted square from specified field
squares = chess.SquareSet()
for squareNum in squareNums : squares.add(squareNum)

# prints board as SVG
SVG(chess.svg.board(board=board, squares=squares))