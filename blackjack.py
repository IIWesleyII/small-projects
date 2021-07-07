import random
playing = True

while playing:

    cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    deck = [(c, s, v) for c, v in zip(cards, values) for s in ['♠', '♥', '♦', '♣']]
    
    curr_deck = deck
    random.shuffle(curr_deck)
    
    p1_card_count = 0
    dealer_card_count = 0
    stay_p1 = False
    stay_dealer = False
    p1_deck = []
    dealer_deck = [] 
    ## initialize starting hands with two cards each [('J', '♣', 10), ('2', '♦', 2)]
    p1_deck.append(curr_deck.pop(0))
    p1_deck.append(curr_deck.pop(0))
    dealer_deck.append(curr_deck.pop(0))
    dealer_deck.append(curr_deck.pop(0))

    p1_card_count +=  p1_deck[0][2] + p1_deck[1][2] 
    dealer_card_count += dealer_deck[0][2] + dealer_deck[1][2]
    print('♠♥♦♣♠♥♦♣♠♥♦♣♠♥♦♣♠♥♦♣♠♥♦♣♠♥♦♣♠♥♦♣♠♥♦♣♠♥♦♣')
    print('Welcome to Blackjack!')
    print('Type \'E\' at any time to exit\n')
    print(f'Player 1: {p1_card_count}')
    p1_str = f'|{p1_deck[0][0]} {p1_deck[0][1]}| |{p1_deck[1][0]} {p1_deck[1][1]}|'
    print(f'Dealer : {dealer_card_count}')
    dealer_str = f'|{dealer_deck[0][0]} {dealer_deck[0][1]}| |{dealer_deck[1][0]} {dealer_deck[1][1]}|'

    
    print(p1_str)
    print(dealer_str)
   

    
    


    while p1_card_count <= 21 or (stay_p1 and stay_dealer):
        # problems I'll face
        # i) Ace counting as 1 or 11
        #   X   ii)  How do i represent a 52 card deck, I need to implement sometinh that will pop cards off the deck
        # iii) how to represent suit, four cards with the same value but different suit
        # iv) all face cards worth 10, except Ace == 11 or 1
        # v) how do i randomly select cards off the deck
        # vi) how to represent the dealer
        # vii) initialize each player with a starting hand of two cards


        try:
            
            user_input = input('Type \'hit me\' to recieve a card or \'stay\' to keep your hand: ')
            if user_input == 'hit me':
                p1_deck.append(curr_deck.pop(0))
                p1_card_count += p1_deck[-1][2]
                p1_str += f' |{p1_deck[-1][0]} {p1_deck[-1][1]}|'
            elif user_input == 'stay':
                stay_p1 = True
            elif user_input == 'E':
                playing = False
                break
            else:
                raise Exception
        except:
            print('Wrong input, try again!')

        # dealers decision
        if(dealer_card_count < 17):
            dealer_deck.append(curr_deck.pop(0))
            dealer_card_count += dealer_deck[-1][2]
            dealer_str += f'|{dealer_deck[-1][0]} {dealer_deck[-1][1]}|'
        else:
            stay_dealer = True
        
        print(f'Player 1: {p1_card_count}\n{p1_str}')
        print(f'Dealer : {dealer_card_count}\n{dealer_str}')
        print(dealer_str)
    if dealer_card_count > p1_card_count and dealer_card_count <= 21:
        print('Dealer wins\n\n')
    

       



        