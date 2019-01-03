# -*- coding: utf-8 -*-
"""
Created on Thu Jan 03 16:33:27 2019

@author: Schroeder
"""

import chess
import csv
import random

HISTORY_FILE_LOC = "res/history.csv"


# pick random move out of legal moves
def getRandomMove(board):
    return random.choice(list(board.legal_moves))

# play chess game with only randomly picked moves
def playRandomChessGame(board):
    turnList = list()
    while not board.is_game_over():
        turnList.append(board.fen().split(" ")[0])
        board.push(getRandomMove(board))
    return turnList

# store the list of boards created during the game into csv history file
def storeGame(turnList, victoryStatus):
    # list of new turns mapped to victory status
    newTurnDict = dict.fromkeys(turnList, victoryStatus)
    # get existing board history
    with open(HISTORY_FILE_LOC, mode='r') as file:
        reader = csv.reader(file)
        historyDict = {rows[0]: int(rows[1]) for rows in reader}
    # merge existing history with new boards and sum the victory states
    mergedHistory = {k: newTurnDict.get(k, 0) + historyDict.get(k, 0) for k in set(newTurnDict) | set(historyDict)}
    # overwrite history csv with new, merged history
    with open(HISTORY_FILE_LOC, 'w', newline='') as file:
        for key, value in mergedHistory.items():
            writer = csv.writer(file, delimiter=',')
            writer.writerow([key, value])

def main():
    board = chess.Board()
    turnList = playRandomChessGame(board)
    # get victory status by turn status of board after match is over
    victoryStatus = 1 if board.turn else -1
    storeGame(turnList, victoryStatus)



