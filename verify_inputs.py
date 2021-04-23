from game import Game
class Verify:

    def __init__(self):

        self.verify_plays = verify_plays()
        self.verify_choice_player = verify_choice_player()
        self.verify_choice_card = verify_choice_card()
    
    #no use yet
 '''   def verify_inputs(self, v):
        value = v + 1
        verify_options = list(range(1, value))
        print(verify_options)
        return verify_options'''
    def verify_plays(self,value):
        if value > 8:
            print('The choice has to be between 1 and 8')
            return False
        if value < 1:
            print('The choice has to be between 1 and 8')
            return False
        else:
            return True 
    
    def verify_choice_player(self,value):
        if len(players) == 3:
            if value > 3 or value < 1:
                print('The choice has to be between 1 and 3')
                return False
            else:
                return True
        if len(players) == 4:
            if value > 4 or value < 1:
                print('The choice has to be between 1 and 4')
                return False
            else:
                return True
    def verify_choice_card(self,value):
        if value > len(player[actual_turn].cards):
            print('The choice has to be between 1 and ' + len(player[actual_turn].cards))
            return False
        if value < 1:
            print('The choice has to be between 1 and ' + len(player[actual_turn].cards))
            return False
        else:
            return True    
            
