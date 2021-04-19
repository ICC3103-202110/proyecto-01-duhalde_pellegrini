import random
from game import Game
class Player:

    def __init__(self, name, money, cards):

        self.money = money
        self.name = name
        self.cards = cards
        self.action = 0

    def recieve_cards(self, v):
        self.cards.append(v)
        return

    def player_action(self):
        print('1) Ingreso')
        print('2) Ayuda externa')
        print('3) Coup')
        print('4) Capitan')
        print('5) Asesino')
        print('6) Embajador')
        print('7) Duque')
        print('8) Condesa')
        players_move = int(input('choose the number of the option you want: '))
        return players_move
    
    #no use yet
    def kill_card(self):
        kill_card = int(input('what card do you want to eliminate (1/2): '))
        return kill_card

    def coup(self):
        self.cards.remove(0)
        print('')

    
        
   
