# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 03:07:57 2018

@author: Schroeder
"""

import chess
import chess.svg
import random 

board = chess.Board()

PAWN_VALUE = 1
ROOK_VALUE = 5
KNIGHT_VALUE = 3
BISHOP_VALUE = 3
QUEEN_VALUE = 9
KING_VALUE = 20

# returns the value of a piece type for the given type
def assignPieceValue(pieceType):
    return {
        1: PAWN_VALUE,
        2: KNIGHT_VALUE,
        3: BISHOP_VALUE,
        4: ROOK_VALUE,
        5: QUEEN_VALUE,
        6: KING_VALUE
    }[pieceType]
    
# sums value of all pieces of given color multiplied with their value
def getValueByColor(color):
    boardValue = 0
    for pieceType in chess.PIECE_TYPES: 
        boardValue += len(board.pieces(pieceType, color)) * assignPieceValue(pieceType)
    return boardValue

# calculates value of white pieces and subtracts value of black pieces => calculates board value
def getBoardValue():
    whiteValue = getValueByColor(chess.WHITE)
    blackValue = getValueByColor(chess.BLACK)
    
    return whiteValue - blackValue

# calculates how many figures are attacked by given color and assigns a value for every attacked figure
def getAttackedPiecesValueByColor(attackerColor, defenderColor):
    # filters squares for attacked squares, on which a figure of defender is placed
    attackedSquares = filter(lambda square : board.is_attacked_by(attackerColor, square) and not board.piece_at(square) is None and board.piece_at(square).color is defenderColor, chess.SQUARES)
    # maps piece type to attacked figure
    attackedPieces = map(lambda square : board.piece_at(square).piece_type, attackedSquares)
    # maps piece value to attacked pieces
    value = map(assignPieceValue, attackedPieces)
    # sums piece value of all attacked pieces
    return sum(value)
     
# calculates value of attacked black pieces and subtracts value of attacked white pieces => calculates attacked pieces value
def getAttackedPiecesValue():
    whiteValue = getAttackedPiecesValueByColor(chess.WHITE, chess.BLACK)
    blackValue = getAttackedPiecesValueByColor(chess.BLACK, chess.WHITE)
    
    return whiteValue - blackValue


###########################################  
############## GAME SECTION ###############
###########################################  
   
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
    print(getBoardValue())
    print(getAttackedPiecesValue())
    print()
    
    if board.turn:
        board.push(getUserMove())
        print("Your Move: ")
    else:
        board.push(getRandomMove())
        print("AIs Move:")



