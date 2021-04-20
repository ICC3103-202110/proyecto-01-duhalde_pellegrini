from player import Player
from cards import Cards 

class Block:
    def __init__(self):
        self.block_duke = block_duke()
        self.block_ambassador = block_ambassador()
        self.block_captain = block_captain()
        self.block_contessa = block.contessa()
    
    def block_duke(self):
        Player.money -=3
        
    def block_ambassador(self):
        if player.money < 2:
            player.money += player.money
            playern.money -= player.money
        else :
            player.money +=2 
            playern.money -= 2
        
    def block_captain(self):
        block_ambassador()
    def block_contessa(self):
        #no hay cambios
        print('')
