# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import chess

board = chess.Board()

for move in board.legal_moves:
    print(board.uci(move))
    
print (board)

print (board.piece_at(chess.B1))