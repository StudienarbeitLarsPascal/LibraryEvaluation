# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 22:38:23 2018

@author: Schroeder
"""
import chess
import chess.svg
import random
board = chess.Board()

# print user possible moves and read in chosen move
def getUserMove():
    print("Possible Moves: ")
    print(getLegalMovesUCI())
    
    print("Enter your move:")
    move = input()
        
    return chess.Move.from_uci(move)

# get random move out of legal moves list
def getRandomMove():
    return random.choice(list(board.legal_moves))

def getLegalMovesUCI():
    return list(map(board.uci, board.legal_moves))

# while game is not over alternate user & ai input
while (not board.is_game_over()):
    print("---------------")
    print(board)
    print("---------------")
    print()
	
    if board.turn:
        board.push(getUserMove())
        print("Your Move: ")
    else:
        board.push(getRandomMove())
        print("AIs Move:")
