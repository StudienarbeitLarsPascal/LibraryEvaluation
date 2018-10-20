# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 21:38:59 2018

@author: Schroeder
"""
import chess
import chess.svg

from IPython.display import SVG

board = chess.Board()
SVG(chess.svg.board(board=board))