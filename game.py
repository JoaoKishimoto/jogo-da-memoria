import pygame
import os
from time import sleep
from card import Card

class Game():
    
    #constructor
    def __init__(self, board, screenSize):

        self.windowName = 'Jodo da memória'
        self.screenSize = screenSize
        self.board =  board
        self.cardSize = screenSize[0] // (self.board.getSize()[1] + 1), screenSize[1] // (self.board.getSize()[0] + 1)
        self.backImage = 'fundo-carta'
        self.loadImages()
        
    #rodando o jogo
    def run(self):
        pygame.init()
        pygame.display.set_caption('Jogo da Memória')
        pygame.display.set_icon(self.images["icon"])
        self.screen = pygame.display.set_mode(self.screenSize)
        running = True
        self.playersTurn = 0
        self.cardsSelected = []
        self.playersPoints = [0, 0]
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    leftClick = pygame.mouse.get_pressed()[0]
                    #Se o clique for válido, aumenta o número de cartas selecionadas em 1 e vira a carta selecionada
                    clickInfo = self.clickInfo(position)
                    if (clickInfo[0] and leftClick):
                        self.cardsSelected.append(clickInfo[1])
                        self.handleClick()
            self.draw()
            self.displayScore()
            pygame.display.flip()
            if(self.playersPoints[0] + self.playersPoints[1] == 14):
                if(self.playersPoints[0] > self.playersPoints[1]):  
                    pygame.display.set_caption("Jogador número 1 ganhou!")
                elif(self.playersPoints[0] < self.playersPoints[1]):
                    pygame.display.set_caption("Jogador número 2 ganhou!")
                else:
                    pygame.display.set_caption("O jogo empatou!")
                pygame.display.flip()
                sleep(5)
                running = False
        pygame.quit()
                 
    
    # Mostrando o Placar de cada jogador
    def displayScore(self):
        size = self.cardSize[0], self.cardSize[1]/2
        pos1 = (19, 636)
        pos2 = (1061 - 144, 636)
        score1 = pygame.image.load(self.getScoreFile(0))
        score2 = pygame.image.load(self.getScoreFile(1))
        score1 = pygame.transform.scale(score1, size)
        score2 = pygame.transform.scale(score2, size)
        self.screen.blit(score1, pos1)
        self.screen.blit(score2, pos2)
        
    
    # Setando a tela   
    def draw(self):
        topLeft = (19, 12)
        distanceBetweenCards = (16, 12)
        for row in range(self.board.getSize()[0]):
            for col in range(self.board.getSize()[1]):
                card = self.board.getCard((row, col))
                image = self.getImage(card)
                self.screen.blit(image, topLeft)
                topLeft = topLeft[0] + self.cardSize[0] + distanceBetweenCards[0], topLeft[1]
            topLeft = 19, topLeft[1] + self.cardSize[1] + distanceBetweenCards[1]
            
    #Cria um Array com as imagens carregadas
    def loadImages(self):
        self.images = {}
        for file in os.listdir("images"):
            if not file.endswith(".png"):
                continue
            image = pygame.image.load(r"images/" + file)
            image = pygame.transform.scale(image, self.cardSize)
            self.images[file.split(".")[0]] = image
            
            
    #seleciona a imagem a ser mostrada de cada carta
    def getImage(self, card):
        string = None
        if(card.getIsGone()):
            string = 'blank'
        elif (card.getIsSelected()):
            string = str(card.getValor()) if isinstance(card.getValor(), int) else card.getValor()
        else:
            string = self.backImage
        return self.images[string]
    
    
    #Seleciona a imagem do placar
    def getScoreFile(self, player):
        points = 'images/p' + str(player + 1) + '-' + str(self.playersPoints[player]) + '.png'
        return points
    
    
    #verifica se o clique é válido
    def clickInfo(self, position):
        x = 19
        y = 12
        card = 0
        row = 0 
        while (y <= self.screenSize[1]):
            x = 19
            col = 0
            while (x <= self.screenSize[0]):
                if (position[0] >= x and position[0] <= x + 135):
                    if(position[1] >= y and position[1] <= y + 144):
                        answer = [not self.board.getCard((row, col)).getIsSelected(), (row, col)]
                        return answer
                x += 135 + 16
                card += 1
                col += 1
            y += 144 + 12
            row += 1
        return (False, [])
    
    def handleClick(self):
        isEqual = False
        
        #Quando houverem 2 cartas selecionadas conferir se elas são iguais
        if (len(self.cardsSelected) == 2):
            isEqual = self.board.getCard(self.cardsSelected[0]).isEqualTo(self.board.getCard(self.cardsSelected[1]))
            self.board.getCard(self.cardsSelected[1]).toggleClick()
        else:
            self.board.getCard(self.cardsSelected[0]).toggleClick()
        
        self.draw()
        pygame.display.flip()
        
        #Se elas forem iguais, ponto pra quem acertar e cartas somem
        if (isEqual):
            sleep(2)
            self.playersPoints[self.playersTurn] += 1
            self.board.getCard(self.cardsSelected[0]).isGone = True
            self.board.getCard(self.cardsSelected[1]).isGone = True
            self.cardsSelected = []
            self.draw()
            pygame.display.flip()
            
        #caso houverem 2 cartas e elas forem diferentes, virar as 2 cartas de volta
        #e trocar a vez do jogador
        elif(len(self.cardsSelected) == 2):
            sleep(2)
            self.togglePlayersTurn()
            self.board.getCard(self.cardsSelected[0]).toggleClick()
            self.board.getCard(self.cardsSelected[1]).toggleClick()
            self.cardsSelected = []
            self.draw()
            pygame.display.flip()
            
            
    #Troca a vez do jogador
    def togglePlayersTurn(self):
        if (self.playersTurn == 0):
            self.playersTurn = 1
        else:
            self.playersTurn = 0