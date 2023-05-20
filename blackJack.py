#BlackJack
#TO DO: 1. ace = 11 or 1; 2. add bet option for point system 
#3. add percent chance of win (a. probability of player busting >21, b. probability of dealer busting>21, probability of player winning at each deal or stay decision c. log of win vs loss
#https://www.youtube.com/watch?v=YDBeWh5hqP4

#AMERICAN BLACKJACK
#The dealer initially receives one card face up and one card face down (a hole card).
#The player is able to double-down on any initial hand.
#The player is allowed to surrender at any point during the hand.
#4) The dealer must stand on soft 17. 

import random
house, player = [],[]
card,deal,game= "","",""
valueDictionary={"2_\u2661":2,"3_\u2661":3,"4_\u2661":4,"5_\u2661":5,"6_\u2661":6,"7_\u2661":7,"8_\u2661":8,"9_\u2661":9,"10_\u2661":10,"JACK_\u2661":10,"QUEEN_\u2661":10,"KING_\u2661":10,"ACE_\u2661":11,
                 "2_\u25C6":2,"3_\u25C6":3,"4_\u25C6":4,"5_\u25C6":5,"6_\u25C6":6,"7_\u25C6":7,"8_\u25C6":8,"9_\u25C6":9,"10_\u25C6":10,"JACK_\u25C6":10,"QUEEN_\u25C6":10,"KING_\u25C6":10,"ACE_\u25C6":11,
                 "2_\u2663":2,"3_\u2663":3,"4_\u2663":4,"5_\u2663":5,"6_\u2663":6,"7_\u2663":7,"8_\u2663":8,"9_\u2663":9,"10_\u2663":10,"JACK_\u2663":10,"QUEEN_\u2663":10,"KING_\u2663":10,"ACE_\u2663":11,
                 "2_\u2660":2,"3_\u2660":3,"4_\u2660":4,"5_\u2660":5,"6_\u2660":6,"7_\u2660":7,"8_\u2660":8,"9_\u2660":9,"10_\u2660":10,"JACK_\u2660":10,"QUEEN_\u2660":10,"KING_\u2660":10,"ACE_\u2660":11,}

def newGame(house,player,valueDictionary):
    game = input("New game? (Y or N)")
    if game == "Y" or "y":
        house,player = [],[] #resetting house dealt cards, player dealt cards, and "shuffling deck"
        valueDictionary={"2_\u2661":2,"3_\u2661":3,"4_\u2661":4,"5_\u2661":5,"6_\u2661":6,"7_\u2661":7,"8_\u2661":8,"9_\u2661":9,"10_\u2661":10,"JACK_\u2661":10,"QUEEN_\u2661":10,"KING_\u2661":10,"ACE_\u2661":11,
                 "2_\u25C6":2,"3_\u25C6":3,"4_\u25C6":4,"5_\u25C6":5,"6_\u25C6":6,"7_\u25C6":7,"8_\u25C6":8,"9_\u25C6":9,"10_\u25C6":10,"JACK_\u25C6":10,"QUEEN_\u25C6":10,"KING_\u25C6":10,"ACE_\u25C6":11,
                 "2_\u2663":2,"3_\u2663":3,"4_\u2663":4,"5_\u2663":5,"6_\u2663":6,"7_\u2663":7,"8_\u2663":8,"9_\u2663":9,"10_\u2663":10,"JACK_\u2663":10,"QUEEN_\u2663":10,"KING_\u2663":10,"ACE_\u2663":11,
                 "2_\u2660":2,"3_\u2660":3,"4_\u2660":4,"5_\u2660":5,"6_\u2660":6,"7_\u2660":7,"8_\u2660":8,"9_\u2660":9,"10_\u2660":10,"JACK_\u2660":10,"QUEEN_\u2660":10,"KING_\u2660":10,"ACE_\u2660":11,}               
        blackJack(house,player,valueDictionary)

def dealAlgo(deal,player,valueDictionary):
    card = random.randint(0,len(valueDictionary)-1)
    print("Player is dealt: " + list(valueDictionary.keys())[card])
    player.append(list(valueDictionary.values())[card]) #----------
    del valueDictionary[str(list(valueDictionary.keys())[card])] #----------
    print(player)
    print("Player sum: " + str(sum(player)))
    deal = input("Deal card(D) or Stay(S).")
    return deal,player,valueDictionary

print("Welcome to BlackJack.")
def blackJack(house,player,valueDictionary):
    if sum(player)<21 and sum(house)<21:
        card = random.randint(0,len(valueDictionary)-1)
        print("House is dealt: " + list(valueDictionary.keys())[card]) #initial deal house
        house.append(list(valueDictionary.values())[card]) #----------
        del valueDictionary[str(list(valueDictionary.keys())[card])] #---------- #deletes entry from valueDictionary so card cannot be drawn again
        card = random.randint(0,len(valueDictionary)-1)
        print("House is dealt: " + list(valueDictionary.keys())[card])
        house.append(list(valueDictionary.values())[card]) #----------
        del valueDictionary[str(list(valueDictionary.keys())[card])] #----------
        print(house)
        print("House sum: " + str(sum(house)))
        if sum(house) >=17:
            fHouseSum = sum(house) #4) The dealer must stand on soft 17. 
        card = random.randint(0,len(valueDictionary)-1)
        print("Player is dealt: " + list(valueDictionary.keys())[card]) #initial deal player 
        player.append(list(valueDictionary.values())[card]) #----------
        del valueDictionary[str(list(valueDictionary.keys())[card])] #----------
        card = random.randint(0,len(valueDictionary)-1)
        print("Player is dealt: " + list(valueDictionary.keys())[card])
        player.append(list(valueDictionary.values())[card]) #----------
        del valueDictionary[str(list(valueDictionary.keys())[card])] #----------
        print(player)
        print("Player sum: " + str(sum(player)))

        if sum(house)==21 and sum(player)==21: #Push situation, draw, all bets returned
            print("Push, no winner.\n")
            newGame(house,player,valueDictionary)
        if sum(house)<21 and sum(player)==21: #Natural blackjack, automatic win
            print("Blackjack. Player wins.\n")
            newGame(house,player,valueDictionary)
        if sum(player)<21 and sum(house)==21: #Natural blackjack, automatic win
            print("Blackjack. House wins.\n")
            newGame(house,player,valueDictionary)
        
        #the following algorithm is to see who goes over 21 first (dealer or player)
        deal = input("Deal card(D) or Stay(S).")
        if deal =="D" or deal=="d": #needs multiple deal conditions
            card = random.randint(0,len(valueDictionary)-1)
            print("Player is dealt: " + list(valueDictionary.keys())[card])
            player.append(list(valueDictionary.values())[card]) #----------
            del valueDictionary[str(list(valueDictionary.keys())[card])] #----------
            print(player)
            print("Player sum: " + str(sum(player)))
            if sum(player)<21:
                deal = input("Deal card(D) or Stay(S).")
                if deal =="D" or deal=="d": #needs multiple deal conditions
                    dealAlgo(deal,player,valueDictionary) #DEAL ALGORITHM --> returns deal value D so stays in dealAlgo loop until S
                    
        if deal =="S" or deal=="s":
            while sum(house)<=16:
                card = random.randint(0,len(valueDictionary)-1)
                print("House is dealt: " + list(valueDictionary.keys())[card])
                house.append(list(valueDictionary.values())[card]) #----------
                del valueDictionary[str(list(valueDictionary.keys())[card])] #----------
                print(house)
                print("House sum: " + str(sum(house)))
            if sum(house) >=17 and sum(house) <= 21:
                fHouseSum = sum(house) #4) The dealer must stand on soft 17. 
                if fHouseSum>sum(player):
                    print(f"House wins, {fHouseSum} > {sum(player)}.\n")
                    newGame(house,player,valueDictionary)
                elif fHouseSum<sum(player):
                    print(f"Player wins, {sum(player)} > {fHouseSum}.\n")
                    newGame(house,player,valueDictionary)
                else:
                    print("Push, no winner.\n") #If the dealer and player in blackjack both have 20, who wins? In 99% of casinos, it's a tie (a “push") where neither player nor dealer win. 
                    newGame(house,player,valueDictionary)
            if sum(house)<21 and sum(house)>sum(player):
                print(f"House wins, {sum(house)} > {sum(player)}.\n")
                newGame(house,player,valueDictionary)
    if sum(house)>21:
        print("House busts. Player wins.\n")
        newGame(house,player,valueDictionary)
    if sum(player)>21:
        print("Player busts. House wins.\n")
        newGame(house,player,valueDictionary)
blackJack(house,player,valueDictionary)
