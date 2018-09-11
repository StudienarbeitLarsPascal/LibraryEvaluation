# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 21:38:59 2018

@author: Schroeder
"""
import chess
import chess.svg

from IPython.display import SVG

board = chess.Board()

#saves moves as uci
legal_moves_uci = [];
for move in board.legal_moves:
    legal_moves_uci += [board.uci(move)]
    
#extracts moves starting from g2
moves_from_g1 = [k for k in legal_moves_uci if k.startswith("g2")]

#extracts reachable fields from moves string
reachableSquaresUCI = [];
for move in moves_from_g1:
    reachableSquaresUCI += [move[-2:]]
    
#creates SquareSet from reachableSquaresUCI List
squares = chess.SquareSet()
for square in reachableSquaresUCI:
    #gettattr transforms square string to matching chess square constant
    squares.add(getattr(chess, square.upper()))

#prints board as SVG
SVG(chess.svg.board(board=board, squares=squares))  


