from game import Game
from board import Board
from card import Card

        
#iniciando cartas
cards = {}
cards[0] = Card(2, 'images/2.png') #2 #Utilizando a matrícula de João Kishimoto (223116024)
cards[1] = Card(2, 'images/2.png')
cards[2] = Card(2, 'images/2.png') #2
cards[3] = Card(2, 'images/2.png')
cards[4] = Card(3, 'images/3.png') #3
cards[5] = Card(3, 'images/3.png')
cards[6] = Card(1, 'images/1.png') #1
cards[7] = Card(1, 'images/1.png')
cards[8] = Card(1, 'images/1.png') #1
cards[9] = Card(1, 'images/1.png')
cards[10] = Card(6, 'imagens/6.png') #6
cards[11] = Card(6, 'imagens/6.png')
cards[12] = Card(0, 'imagens/0.png') #0
cards[13] = Card(0, 'images/0.png')
cards[14] = Card(2, 'images/2.png') #2
cards[15] = Card(2, 'images/2.png')
cards[16] = Card(4, 'images/4.png') #4
cards[17] = Card(4, 'images/4.png')
cards[18] = Card('D', 'imagens/D.png') #'D' #Utilizando o nome de Dimytri
cards[19] = Card('D', 'imagens/D.png')
cards[20] = Card('i', 'imagens/i.png') #'i'
cards[21] = Card('i', 'imagens/i.png')
cards[22] = Card('m', 'imagens/m.png') #'m'#
cards[23] = Card('m', 'imagens/m.png')
cards[24] = Card('y', 'imagens/y.png') #'y'
cards[25] = Card('y', 'imagens/y.png')
cards[26] = Card('t', 'imagens/t.png') #'t'
cards[27] = Card('t', 'imagens/t.png')
        
screenSize = (1080, 720)

board = Board(cards)
board.setBoard()
game = Game(board, screenSize)
game.run()