import random
from game import Game
from verify_inputs import Verify

game = Game()
class Player:

    def __init__(self, name, money, cards):

        self.money = money
        self.name = name
        self.cards = cards
        self.action = 0
        self.player_list = []
    '''
    @property
    def money(self):
        return self.__money
    @property
    def name(self):
        return self.__name
    @property
    def cards(self):
        return self.__cards
    '''
    def recieve_cards(self, v):
        self.cards.append(v)
        return
    
    def player_action(self):
        print('1) Entry')
        print('2) External help')
        print('3) Coup')
        print('4) Captain')
        print('5) assasin')
        print('6) ambassador')
        print('7) duke')
        print('8) contessa')
        print('9) view my cards')
        print('---------------------')
        players_move = int(input('choose the number of the option you want: '))
        return players_move
    
    #no use yet
    def kill_card(self):
        kill_card = int(input('what card do you want to eliminate (1/2): ')) -1 
        if Verify.verify_choice_card(kill_card) == True:
            kill_card = player.cards.pop(kill_card)
            return 
        else : 
            kill_card = int(input('what card do you want to eliminate (1/2): ')) -1 
            kill_card = player.cards.pop(kill_card)
            return 

    def return_card_to_deck(self):
        kill_card = int(input('what card do you want to return to deck : ')) -1 
        deck.deck_of_cards.append(player[actual_turn].cards[kill_card])
        kill_card = player[actual_turn].cards.pop(kill_card)
        return
    '''
    def coup(self, players):
        if len(players) == 3:
            print('you do you want to kill:')
            print('1) kill', players[0].name)
            print('2) kill', players[1].name)
            print('3) kill', players[2].name)

            kill = int(input('select the number in here: '))
            if Verify.verify_choice_player == True:
                players[kill-1].cards.pop(0)
                print(players[kill-1].name, 'cards:',players[kill-1].cards)
                return
            else :
                kill = int(input('select the number in here: '))
                players[kill-1].cards.pop(0)
                print(players[kill-1].name, 'cards:',players[kill-1].cards)
                return
            

        elif len(players) == 4:

            print('who you do you want to kill:')
            print('1) kill', players[0].name)
            print('2) kill', players[1].name)
            print('3) kill', players[2].name)
            print('4) kill', players[3].name)

            kill = int(input('select the number in here: '))
            if Verify.verify_choice_player == True:
                players[kill-1].cards.pop(0)
                print(players[kill-1].name, 'cards:',players[kill-1].cards)
                return
            else :
                kill = int(input('select the number in here: '))
                players[kill-1].cards.pop(0)
                print(players[kill-1].name, 'cards:',players[kill-1].cards)
                return
        
        elif len(players) == 2:
            print('who you do you want to kill:')
            print('1) kill', players[0].name)
            print('2) kill', players[1].name)

            kill = int(input('select the number in here: '))
            if Verify.verify_choice_player == True:
                players[kill-1].cards.pop(0)
                print(players[kill-1].name, 'cards:',players[kill-1].cards)
                return
            else :
                kill = int(input('select the number in here: '))
                players[kill-1].cards.pop(0)
                print(players[kill-1].name, 'cards:',players[kill-1].cards)
                return
    '''
    def coup(self, players, summary):
        if len(players) == 3:
            print('you do you want to kill:')
            print('1) kill', players[0].name)
            print('2) kill', players[1].name)
            print('3) kill', players[2].name)

            kill = int(input('select the number in here: '))
            x = str(players[kill-1].name) + " Lost an influence because of option Coup"
            summary.append(x)
            players[kill-1].cards.pop(0)
            
            return
            
        elif len(players) == 4:

            print('who you do you want to kill:')
            print('1) kill', players[0].name)
            print('2) kill', players[1].name)
            print('3) kill', players[2].name)
            print('4) kill', players[3].name)

            kill = int(input('select the number in here: '))
            x = str(players[kill-1].name) + " Lost an influence because of option Coup"
            summary.append(x)
            players[kill-1].cards.pop(0)
            
            return
        
        elif len(players) == 2:
            print('who you do you want to kill:')
            print('1) kill', players[0].name)
            print('2) kill', players[1].name)

            kill = int(input('select the number in here: '))
            x = str(players[kill-1].name) + " Lost an influence because of option Coup"
            summary.append(x)
            players[kill-1].cards.pop(0)
            
            return
        
 

           
    

    
        
   
