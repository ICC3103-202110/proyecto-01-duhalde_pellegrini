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
        if players[game.actual_turn].money < 3:
            raise ValueError('You need 3 coins to use this card')
        else:
            players[game.actual_turn].money += 3
            player.coup()        
        
    def captain(self):
        if len(players) == 3:
            print('1) steal from', players[0].name)
            print('2) steal from', players[1].name)
            print('3) steal from', players[2].name)
            steal = int(input('select from which player you want to steal coins'))
            if player[steal-1].money < 2:
                players[game.actual_turn].money += player[steal-1].money
            else :
                players[game.actual_turn].money += 2
            print(players[steal-1].name, 'coins:',players[steal-1].money)
            break
        elif len(players) == 4:
            print('1) kill', players[0].name)
            print('2) kill', players[1].name)
            print('3) kill', players[2].name)
            print('4) kill', players[3].name)
            steal = int(input('select from which player you want to steal coins'))
            if player[steal-1].money < 2:
                players[game.actual_turn].money += player[steal-1].money
            else :
                players[game.actual_turn].money += 2
            print(players[steal-1].name, 'coins:',players[steal-1].money)
            break
       
    def ambassador(self):
        player[game.actual_turn].recieve_cards()
        print('select which cards you want to discard')
        player[game.actual_turn].kill_card
        player[game.actual_turn].kill_card

    def contessa(self):
        #la condesa no hace cambios, solo bloquea.
        


    
    
