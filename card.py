import pygame

#Criando a classe carta
class Card():

    def __init__(self, valor, image):       #construtor
        self.valor = valor
        self.image = image
        self.isSelected = False
        self.isGone = False
        
    def getIsGone(self):                    #verifica se a carta já acharam o par da carta
        return self.isGone  
    
    def getIsSelected(self):                #verifica se a carta está selecionada
        return self.isSelected

    def getValor(self):                     #função que devolve o valor
        return self.valor
    
    def getImage(self):                     #função que devolve o o endereço da imagem
        return self.image
    
    def toggleClick(self):                        #função que seleciona ou desseleciona a carta
        self.isSelected = not self.isSelected
    
    def isEqualTo(self, anotherCard):         #função que compara cartas e retorna True quando forem iguais
        if self.valor == anotherCard.valor:
            return True
        return False
    