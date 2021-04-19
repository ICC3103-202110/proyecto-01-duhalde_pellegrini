import random

class Game:
    def __init__(self):
        self.cards = []
        self.deck_of_cards = self.create_deck_cards()
        self.final_turn = 3
        self.actual_turn = 0
    
    def welcome_board(self):
        print("\n")
        print("|****************************|")
        print("|**|      Bienvenidos     |**|")
        print("|**|       a Coup         |**|")
        print("|****************************|")
        print("")
        pass
    
    def create_deck_cards(self):
        deck_of_cards = []
        duque = ["duque","duque","duque"]
        asesino = ["asesino","asesino","asesino"]
        capitan = ["capitan","capitan","capitan"]
        embajador = ["embajador","embajador","embajador"]
        condesa = ["condesa","condesa","condesa"]

        for v in range(1,2):
            for figure in duque:
               deck_of_cards.append(figure)
        for v in range(2,3):
            for figure in asesino:
                deck_of_cards.append(figure)
        for v in range(3,4):
            for figure in capitan:
                deck_of_cards.append(figure)
        for v in range(4,5):
            for figure in embajador:
                deck_of_cards.append(figure)
        for v in range(5,6):
            for figure in condesa:
                deck_of_cards.append(figure)
        random.shuffle(deck_of_cards)
        print('')
        print(deck_of_cards)
        return deck_of_cards
    
    #no use yet
    def verify_inputs(self, v):
        value = v + 1
        verify_options = list(range(1, value))
        print(verify_options)
        return verify_options


        
    
     

        







