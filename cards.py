import random
from player import Player


class Cards:

    
    def __init__(self):

        self.duque = self.duque()
        self.asesino = self.asesino()
        self.capitan = self.capitan()
        self.embajador = self.embajador()
        self.condesa = self.condesa()
        

    def duque(self):
        Player.money +=3
        print('')
        
    def asesino(self):
        if Player.money < 3:
            raise ValueError('You need 3 coins to use this card')
        else:
            Player.money -=3 
            n = int(input('select which player do you want to kill'))
            return n        
        
    def capitan(self):
        n = int(input('select from which player you want to steal coins'))
        if playern.money < 2:
            player.money += playern.money
        else :
            playern.money -=2
            player.money +=2

    def embajador(self):
        player.recieve_cards()
        print('select which card you want to discard')
        player.kill_card

    def condesa(self):
        


    
    
