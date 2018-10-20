# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 21:35:34 2018

@author: Schroeder
"""

import chess

board = chess.Board()
    
print ("\nBoard:")
print (board)

print ("\nPiece at B1:")
print (board.piece_at(chess.B1))