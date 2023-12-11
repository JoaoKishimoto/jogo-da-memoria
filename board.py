import pygame as pg
import random
from card import Card

class Board():
    
    #Constructor
    def __init__(self, cards):
        self.size = [4, 7]
        self.cards = cards
        self.numRight = 0
        self.setBoard()
    
    #ajeita a 'mesa'
    def setBoard(self):
        random.shuffle(self.cards)
        self.board = []
        i = 0
        for row in range(self.size[0]):
            row = []
            for col in range(self.size[1]):
                row.append(self.cards[i])
                i += 1
            self.board.append(row)
            
    #retorna a carta com o respectivo index no grid de cartas
    def getCard(self, index):
        return self.board[index[0]][index[1]]
    
    #retorna o tamanho do tabuleiro
    def getSize(self):
        return self.size