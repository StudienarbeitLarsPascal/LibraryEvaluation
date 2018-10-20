# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 21:35:34 2018

@author: Schroeder
"""

import chess

board = chess.Board()

print ("Possible Moves:")
for move in board.legal_moves:
    print(board.uci(move))