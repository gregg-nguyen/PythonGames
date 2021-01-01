card_dic = {'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}
card_rank = list(card_dic.keys())
card_suit = ['heart','spade','diamond','club']

table = []

# Card Class
class Card():
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = card_dic[rank]
        
    def __repr__(self):
        return self.rank + ' ' + self.suit
        
import random

# Deck Class
class Deck():
    def __init__(self):
        self.all_card = []
        # create card object:
        for suit in card_suit:
            for rank in card_rank:
                card_object = Card(suit,rank)
                self.all_card.append(card_object)

                
    def shuffle(self):
        random.shuffle(self.all_card)
        
        
# Player Class
class Player():
    def __init__(self,name):
        self.name = name
        self.all_card = []
        
    def pop_card(self):
        self.all_card.pop(0)
        
    def add_card(self):
        self.all_card.extend(table)
    
   
# Game Logic:


while True:
    # Welcome to game:
    from IPython.display import clear_output
    clear_output()    
    
    print('Welcome to Simple Card Game! This game is for 2 players!')
    
    game_start = input('Do you want to play game?:  ')
    if game_start.upper().startswith('Y'):
        game_start = True
    else:
        game_start = False
        break

    round = 0  
    choose_player = 0
    
    while game_start:
        
        choose_player = int(input('Please choose Player1 or Player2. Type in "1" or "2": '))
    
        # create deck for game:
        deck_original = Deck()
        deck_original.shuffle()

        # create Players for game:
        Player1 = Player('Player1')
        Player2 = Player('Player2') 
       
        Player1.all_card = deck_original.all_card[:26]
        Player2.all_card = deck_original.all_card[26:]
    
        # in_game:
            
        while len(Player1.all_card) != 0 and len(Player2.all_card) != 0:
            
            round += 1
            
            print(f'This is Round No.{round}')
            
            print('Compare the next 1 pair of cards from each Player!')
            table.append(Player1.all_card.pop(0))
            table.append(Player2.all_card.pop(0))
            
            if len(Player1.all_card) == 0:
                print(f'Player2 has won after {round} rounds!')
                break
            
            elif len(Player2.all_card) == 0:
                print(f'Player1 has won after {round} rounds!')
                break
            
            # Compare cards:
            if table[(len(table)//2)-1].value > table[-1].value:
                print('Player1 got all cards on the table!')
                Player1.all_card.extend(table)
                table.clear()
            elif table[(len(table)//2)-1].value < table[-1].value:
                print('Player2 got all cards on the table!')
                Player2.all_card.extend(table)
                table.clear()
            
            
            # in war: 
            
            elif table[(len(table)//2)-1].value == table[-1].value:
                
                if len(Player1.all_card) >= 7 and len(Player2.all_card) >= 7:
                    # get 7 more pairs of cards:
                    print('Collect the next 7 cards from each player and compare the 7th cards of each!')
                    table.extend(Player1.all_card[0:6])
                    table.extend(Player2.all_card[0:6])
            
                    del (Player1.all_card[0:6])
                    del (Player2.all_card[0:6])
    
                elif len(Player1.all_card) < 7:
                    print(f'Player2 has won after {round} rounds!!')
                    break
                
                elif len(Player2.all_card) < 7:
                    print(f'Player1 has won after {round} rounds!!')
                    break
        
        
        reset = input('Do you want to restart the game? ')
        if reset.upper().startswith('Y'):
            game_start = True
        else:
            game_start = False
    break
       
