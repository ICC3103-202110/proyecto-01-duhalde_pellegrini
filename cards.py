import random
from player import Player


class Cards:

    
    def __init__(self):

        self.duke = self.duke()
        self.assasin = self.assasin()
        self.captain = self.captain()
        self.ambassador = self.ambassador()
        self.contessa = self.contessa()
        

    def duke(self):
        players[game.actual_turn].money += 3
        print(players[game.actual_turn].name,'monedas: ',players[game.actual_turn].money)
                
        
    def assasin(self):
        if Player.money < 3:
            raise ValueError('You need 3 coins to use this card')
        else:
            Player.money -=3 
            n = int(input('select which player do you want to kill'))
            return n        
        
    def captain(self):
        n = int(input('select from which player you want to steal coins'))
        if playern.money < 2:
            player.money += playern.money  #playern es al jugador que le quita, arreglar después 
        else :
            playern.money -=2 #lo mismo que arriba
            player.money +=2

    def ambassador(self):
        player.recieve_cards()
        print('select which cards you want to discard')
        player.kill_card
        player.kill_card

    def condesa(self):
        


    
    
