from player import Player
from cards import Cards
from game import Game
from deck_cards import Deck_cards

deck = Deck_cards()
players = []
game = Game()
p1 = Player(0,0,0)
cards = Cards()

def start_game():

    game.welcome_board()
    p1.player_list = players
    final_turn = len(p1.player_list)
    actual_turn = 0
    

    while True:
        if actual_turn >= final_turn:
            actual_turn = 0 
            print('new round...')
             

        elif actual_turn != final_turn:
            
            print('its the turn of', players[actual_turn].name) 
            option = p1.player_action()
            while True:
                
                if option == 1:

                    print('you chose ingreso')
                    players[actual_turn].money += 1
                    print(players[actual_turn].name,'money: ',players[actual_turn].money)
                    break

                elif option == 2:

                    print('you chose ayuda externa')
                    cards.external_help(players,actual_turn)
                    break

                elif option == 3:

                    print('you chose Coup')
                    if players[actual_turn].money < 7:
                        print('you do not have enough money to use this option.')
                        print('choose another option')
                        actual_turn -= 1
                        break
                    else:
                        player.coup()

                elif option == 4:

                    print('you chose Capitan')
                    cards.captain(players,actual_turn)
                    
                    break

                elif option == 5:

                    print('you chose Asesino ')
                    if players[actual_turn].money >= 3:
                        cards.assasin(players,actual_turn)
                        players[actual_turn].money -= 3
                        break
                    else:
                        actual_turn -= 1
                        break

                elif option == 6: 

                    print('you chose Embajador') 
                    cards.ambassador(players,actual_turn)
                    break

                elif option == 7:  
                    print('you chose Duque') 
                    cards.duke(players,actual_turn)
                    break

                elif option == 8:  

                    print('you chose Condesa') 
                    print('this option is just to block assasination please choose again')
                    actual_turn -= 1
                    break
                
            game.winner(players)
            show_people()
            final_turn = len(players)
            actual_turn +=1
            print('')

            
        
def show_people():
    print("\nPeople Created: ")
    for (i, _) in enumerate(players):
        print(f"{i+1}: name: {players[i].name} - cards: {players[i].cards} - money: {players[i].money}")


def create_player(numero):
    n = 1
    while numero >= n:
        n +=1
        name = input('Whats your players name: ')
        p1 = Player(name, 2, [])
        print('')
        p1.recieve_cards(deck.deck_of_cards[0])
        deck.deck_of_cards.remove(deck.deck_of_cards[0])
        p1.recieve_cards(deck.deck_of_cards[0])
        deck.deck_of_cards.remove(deck.deck_of_cards[0])
        players.append(p1)
    return players

def show_coins():
    for (i, _) in enumerate(players):
        print(f"{i+1}: name: {players[i].name} -  money: {players[i].money}")

def print_menu_and_select():
    print("\nSelect one of these options")
    print("3. start game")
    print("2. show players")
    print("1. create players")
    print("0. exit")
    return int(input('what option are you selecting: '))

def menu():
    while True:
        selection = print_menu_and_select()
        if selection == 0:
            break
        elif selection == 1:
            while True:
                number_of_players = int(input('how many players are playing (3/4):  '))
                if number_of_players > 4 or number_of_players < 3:
                    False
                else:
                    final_turn = number_of_players
                    players = create_player(number_of_players)
                    
                    break
                    
        elif selection == 2:
            show_people()
        
        elif selection == 3:
            start_game()
            break
  

if __name__ == "__main__":
    menu()

