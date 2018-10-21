# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 03:07:57 2018

@author: Schroeder
"""

import chess
import chess.svg

board = chess.Board()

PAWN_VALUE = 1
ROOK_VALUE = 5
KNIGHT_VALUE = 3
BISHOP_VALUE = 3
QUEEN_VALUE = 9
KING_VALUE = 20

# counts how many pieces of one pieceType and color are placed on the chessboard
def countPieces(pieceType, color):
    return len(board.pieces(pieceType, color))

# sums value of all pieces of given color multiplied with their value
def getValueByColor(color):
    pawns = countPieces(chess.PAWN, color)
    rooks = countPieces(chess.ROOK, color)
    knights = countPieces(chess.KNIGHT, color) 
    bishops = countPieces(chess.BISHOP, color)
    queens = countPieces(chess.QUEEN, color)

    return pawns * PAWN_VALUE + rooks * ROOK_VALUE + knights * KNIGHT_VALUE + bishops * BISHOP_VALUE + queens * QUEEN_VALUE

# calculates value of white pieces and subtracts value of black pieces => calculates board value
def getBoardValue():
    whiteValue = getValueByColor(chess.WHITE)
    blackValue = getValueByColor(chess.BLACK)
    
    return whiteValue - blackValue

# calculates how many pieces of given type are attacked by color
def getAttackedPieces(pieceType, attackerColor, defenderColor):
    attackedPieces = list(filter(lambda square : board.is_attacked_by(attackerColor, square) and not board.piece_at(square) is None and board.piece_at(square).color is defenderColor and board.piece_at(square).piece_type is pieceType, chess.SQUARES))
    return len(attackedPieces)
    
# sums value of all attacked pieces by given color multiplied with their value
def getAttackedPiecesValueByColor(attackerColor, defenderColor):
    attackedPawns = getAttackedPieces(chess.PAWN, attackerColor, defenderColor)
    attackedRooks = getAttackedPieces(chess.ROOK, attackerColor, defenderColor)
    attackedKnights = getAttackedPieces(chess.KNIGHT, attackerColor, defenderColor)
    attackedBishops = getAttackedPieces(chess.BISHOP, attackerColor, defenderColor)
    attackedQueens = getAttackedPieces(chess.QUEEN, attackerColor, defenderColor)
    attackedKings = getAttackedPieces(chess.KING, attackerColor, defenderColor)
    
    return attackedPawns * PAWN_VALUE + attackedRooks * ROOK_VALUE + attackedKnights * KNIGHT_VALUE + attackedBishops * BISHOP_VALUE + attackedQueens * QUEEN_VALUE + attackedKings * KING_VALUE
    
# calculates value of attacked black pieces and subtracts value of attacked white pieces => calculates attacked pieces value
def getAttackedPiecesValue():
    whiteValue = getAttackedPiecesValueByColor(chess.WHITE, chess.BLACK)
    blackValue = getAttackedPiecesValueByColor(chess.BLACK, chess.WHITE)
    
    return whiteValue - blackValue

    
# GAME SECTION
   
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
    if board.turn:
        board.push(getUserMove())
        print("Your Move: ")
    else:
        board.push(getRandomMove())
        print("AIs Move:")
    
    print("---------------")
    print(board)
    print("---------------")
    print(getBoardValue())
    print(getAttackedPiecesValue())
    print()



