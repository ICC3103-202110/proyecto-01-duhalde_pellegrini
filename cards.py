from player import Player
from game import Game
from deck_cards import Deck_cards
from verify_inputs import Verify
game = Game()
p1  = Player(0,0,0)
deck = Deck_cards()
class Cards:

    
    def __init__(self):
        self.cards = []
        
        
        

    def duke(self,players,actual_turn) :
        players_that_challenge = []
        players_that_challenge = (game.ask_who_challenges(actual_turn, players))
        
        if not players_that_challenge:
            print('your play was succesfull, no one challenged you!')
            players[actual_turn].money += 3
        else:
            print('person that challenged: ',players_that_challenge.name)
            challenger = players.index(players_that_challenge)
                        
            if 'duque' in players[actual_turn].cards:

                print('your challenge has failed',players_that_challenge.name,'you loose a cards')
                players[actual_turn].money += 3

                x = players.index(players_that_challenge)
                players[x].cards.pop(0)
                y = players.index(players[actual_turn])
                game.remove_losers(x, players)
                
                
            else:

                print('you lost the challenge',players[actual_turn].name,'you loose a cards')

                players[actual_turn].cards.pop(0)
                y = players.index(players[actual_turn])
                game.remove_losers(y, players)
                
        
    def assasin(self,players,actual_turn):
        players_that_block = []
        players_that_block = (game.ask_who_blocks_card(actual_turn, players))


        if not players_that_block:
            print('your play was succesfull, no one blocked you!')
            p1.coup(players)
            return
        else:
            print('person that blocked: ',players_that_block.name)
            blocker = players.index(players_that_block)
            players_counts_block = []
            players_counts_block = (game.ask_who_counts_block(blocker, players))

            if not players_counts_block:
                print('no one counted the block')
                return

            else:  
                print(players_counts_block.name,'counted block')

                if 'condesa' in players_that_block.cards:
                    print('your count has failed',players_counts_block.name,'you loose a cards')

                    x = players.index(players_counts_block)
                    players[x].cards.pop(0)
                    game.remove_losers(x, players)
                    return           
                else:
                    print('you lost the count', players_that_block.name,'you loose a cards')
                    players[actual_turn].money += 2

                    players_that_block.cards.pop(0)
                    x = players.index(players_that_block)
                    game.remove_losers(x, players)
                    
                    return      
        
                    
    def captain(self,players,actual_turn):

        if len(players) == 3:
            print('1) steal from', players[0].name)
            print('2) steal from', players[1].name)
            print('3) steal from', players[2].name)

            steal = int(input('select from which player you want to steal coins: '))
            if players[steal-1].money >= 2:
                players[actual_turn].money += 2
                players[steal-1].money -= 2
            else:
                players[actual_turn].money += 2
            print(players[steal-1].name, 'coins:',players[steal-1].money)
            
        elif len(players) == 4:
            print('1) steal', players[0].name)
            print('2) steal', players[1].name)
            print('3) steal', players[2].name)
            print('4) steal', players[3].name)

            steal = int(input('select from which player you want to steal coins'))
            if player[steal-1].money <= 2:
                players[actual_turn].money += 2
                players[steal-1].money -= 2
            else :
                players[actual_turn].money += 2
            print(players[steal-1].name, 'coins:',players[steal-1].money)
        
        if len(players) == 2:
            print('1) steal from', players[0].name)
            print('2) steal from', players[1].name)

            steal = int(input('select from which player you want to steal coins: '))
            if players[steal-1].money <= 2:
                players[actual_turn].money += 2
                players[steal-1].money -= 2
            else:
                players[actual_turn].money += 2
            print(players[steal-1].name, 'coins:',players[steal-1].money)

        players_that_block = []
        players_that_block = (game.ask_who_blocks_card(actual_turn, players))


        if not players_that_block:
            print('your play was succesfull, no one blocked you!')
            return  
        else:
            print('person that blocked: ',players_that_block.name)
            blocker = players.index(players_that_block)
            players_counts_block = []
            players_counts_block = (game.ask_who_counts_block(blocker, players))

            if not players_counts_block:
                print('no one counted the block')
                players[actual_turn].money -= 2
                players[steal-1].money += 2
                return

            else:  
                print(players_counts_block.name,'counted block')

                if 'capitan' or 'embajador' in players_that_block.cards:
                    print('your count has failed',players_counts_block.name,'you loose a cards')
                    x = players.index(players_counts_block)
                    players[x].cards.pop(0)
                    game.remove_losers(x, players)
                    return           
                else:
                    print('you lost the count', players_that_block.name,'you loose a cards')
                    players_that_block.cards.pop(0)
                    x = players.index(players_that_block)
                    game.remove_losers(x, players)
                    return 
       
    def ambassador(self,players,actual_turn):
        players_that_block = []
        players_that_block = (game.ask_who_blocks_card(actual_turn, players))


        if not players_that_block:
            print('your play was succesfull, no one blocked you!')
            players[actual_turn].recieve_cards(deck.deck_of_cards[0])
            deck.deck_of_cards.remove(deck.deck_of_cards[0])
            players[actual_turn].recieve_cards(deck.deck_of_cards[0])
            deck.deck_of_cards.remove(deck.deck_of_cards[0])
            players[actual_turn].return_card_to_deck
            players[actual_turn].return_card_to_deck
            return
        else:
            print('person that blocked: ',players_that_block.name)
            blocker = players.index(players_that_block)
            players_counts_block = []
            players_counts_block = (game.ask_who_counts_block(blocker, players))

            if not players_counts_block:
                print('no one counted the block')
                return

            else:  
                print(players_counts_block.name,'counted block')

                if 'capitan' in players_that_block.cards:
                    print('your count has failed',players_counts_block.name,'you loose a card')
                    x = players.index(players_counts_block)
                    players[x].cards.pop(0)
                    game.remove_losers(x, players)
                    return           
                else:
                    print('you lost the count', players_that_block.name,'you loose a card')
                    players[actual_turn].recieve_cards(deck.deck_of_cards[0])
                    deck.deck_of_cards.remove(deck.deck_of_cards[0])
                    players[actual_turn].recieve_cards(deck.deck_of_cards[0])
                    deck.deck_of_cards.remove(deck.deck_of_cards[0])
                    players[actual_turn].return_card_to_deck
                    players[actual_turn].return_card_to_deck
                    players_that_block.cards.pop(0)
                    x = players.index(players_that_block)
                    game.remove_losers(x, players)
                     
                    return
        
    def contessa(self,players):
        return
        #contessa does not do anything just blocks assasin
    
    def external_help(self, players,actual_turn):

        players_that_block = []
        players_that_block = (game.ask_who_blocks_card(actual_turn, players))


        if not players_that_block:
            print(players[actual_turn].name,'your play was succesfull, no one blocked you!')
            players[actual_turn].money += 2
            return
        else:
            print('person that blocked: ',players_that_block.name)
            blocker = players.index(players_that_block)
            players_counts_block = []
            players_counts_block = (game.ask_who_counts_block(blocker, players))

            if not players_counts_block:
                print('no one counted the block')
                return

            else:  
                print(players_counts_block.name,'counted block')

                if 'duque' in players_that_block.cards:
                    print('your count has failed',players_counts_block.name,'you loose a cards')
                    x = players.index(players_counts_block)
                    players[x].cards.pop(0)
                    game.remove_losers(x, players)
                    return           
                else:
                    print('you lost the count', players_that_block.name,'you loose a cards')
                    players_that_block.cards.pop(0)
                    x = players.index(players_that_block)
                    game.remove_losers(x, players)
                    players[actual_turn].money += 2
                    return
    
    
        


    
    
