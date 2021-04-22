import random

class Game:
    def __init__(self):
        self.cards = []
    
    def welcome_board(self):
        print("\n")
        print("|****************************|")
        print("|**|      Bienvenidos     |**|")
        print("|**|       a Coup         |**|")
        print("|****************************|")
        print("")
        pass
 
    def yes_no_board(self):
        print("choose a number")
        print("1) yes")
        print("2) no")
        option = int(input('what is your option: '))
        print('')
        return option
    
    def remove_losers(self, v, players):
        if not players[v].cards:
            return players.remove(players[v])
        else:
            return True
        
    def choose_random_player(self, v):
        if len(v) == 0:
            challenger = []
            return challenger
        else:
            challenger = random.choice(v)
            return challenger

    def ask_who_challenges(self, v, players):
        challenger = []
        probable_challenger = players
        back =  probable_challenger.pop(v)

        x = 0
        while len(probable_challenger)  != x:
            print(probable_challenger[x].name,'do you want to challenge?')
            option = game.yes_no_board()
            if option == 1:
                challenger.append(probable_challenger[x])
                x += 1
            elif option == 2:
                x += 1

        players.insert(v, back)
        challenger = self.choose_random_player(challenger)
        
        return challenger
        
    def ask_who_counts_challenge(self, v, players):
        challenge_counter = []
        probable_counter = players
        back =  probable_counter.pop(v)
        print(back.name)

        x = 0
        while len(probable_counter)  != x:
            print(probable_counter[x].name,'do you want to count the challenge?')
            option = game.yes_no_board()
            if option == 1:
                challenge_counter.append(probable_counter[x])
                x += 1
            elif option == 2:
                x += 1

        players.insert(v, back)
        challenge_counter = self.choose_random_player(challenge_counter)

        return challenge_counter

    def ask_who_counts_block(self, v, players):
        block_counter = []
        probable_counter = players
        back =  probable_counter.pop(v)
        print(back.name)

        x = 0
        while len(probable_counter)  != x:
            print(probable_counter[x].name,'do you want to count the block?')
            option = game.yes_no_board()
            if option == 1:
                block_counter.append(probable_counter[x])
                x += 1
            elif option == 2:
                x += 1

        players.insert(v, back)
        block_counter = self.choose_random_player(block_counter)

        return block_counter
    
    def ask_who_blocks_card(self, actual_turn, players):

        player_that_block = []
        
        
        probable_blocker = players
        back = probable_blocker.pop(actual_turn)
        

        x = 0
        while len(probable_blocker)  != x:
            print(probable_blocker[x].name,'do you want to block player?')
            option = game.yes_no_board()
            if option == 1:
                player_that_block.append(probable_blocker[x])
                x += 1
                
            elif option == 2:
                x += 1
        players.insert(actual_turn, back)
        player_that_block = self.choose_random_player(player_that_block)

        return player_that_block

    def winner(self, players):
        if len(players) == 1:
            print('the winner is', players[0].name)
            exit()
        else:
            return False

game = Game()
        
    
     

        







