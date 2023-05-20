#Poker - TO DO: percentage chance of winning - make 2 card draw condition, then 5 cards are drawn where both player and computer use to make combination; pair heirarchy; decrease code
import random #import the random module to generate random numbers

print("Poker, best hand wins")
pairDictionary={'':0,'2 of a kind':1,'2 pair':2,'3 of a kind':3,'4 of a kind':4,'straight':5,'flush':6,'straight-flush':7}
valueDictionary={'two':0,'three':1,'four':2,'five':3,'six':4,'seven':5,'eight':6,'nine':7,'ten':8,'jack':9,'queen':10,'king':11,'ace':12}
cardListH =["2_\u2661","3_\u2661","4_\u2661","5_\u2661","6_\u2661","7_\u2661","8_\u2661","9_\u2661","10_\u2661","JACK_\u2661","QUEEN_\u2661","KING_\u2661","ACE_\u2661"]
cardListD =["2_\u25C6","3_\u25C6","4_\u25C6","5_\u25C6","6_\u25C6","7_\u25C6","8_\u25C6","9_\u25C6","10_\u25C6","JACK_\u25C6","QUEEN_\u25C6","KING_\u25C6","ACE_\u25C6"]
cardListC =["2_\u2663","3_\u2663","4_\u2663","5_\u2663","6_\u2663","7_\u2663","8_\u2663","9_\u2663","10_\u2663","JACK_\u2663","QUEEN_\u2663","KING_\u2663","ACE_\u2663"]
cardListS =["2_\u2660","3_\u2660","4_\u2660","5_\u2660","6_\u2660","7_\u2660","8_\u2660","9_\u2660","10_\u2660","JACK_\u2660","QUEEN_\u2660","KING_\u2660","ACE_\u2660"]
cardList = [cardListH,cardListD,cardListC,cardListS]
cardListPlayer, cardListComputer, cardListAll = [],[],[]
cardElemPlayer, cardElemComputer, cardElemAll = 0,0,0
playerChips, computerChips = 0,0 #initial score of player and computer outside of game loop
x, turn, round =0,0,0 #x = append history value of pairs; turn ensures player goes then computer goes; round increases after pair comparison (7 cards)
allCard,allList,playerList,playerCard,computerList,computerCard,pairsP,pairsC=[],[],[],[],[],[],[],[]

def cardGame(allList,allCard,cardElemAll,cardListAll,pairsP,pairsC,playerChips,playerList,playerCard,cardListPlayer,cardElemPlayer,computerChips,computerList,computerCard,cardListComputer,cardElemComputer,cardList,cardListH,cardListD,cardListC,cardListS,round,turn,x): #To force completion of game
    input("Press (D) to deal")

    #SUFFICIENT FOR 2 PLAYER POKER  
    if len(playerList) <=7:  
        if cardListH.count(cardListH[0]) != len(cardListH) and cardListD.count(cardListD[0]) != len(cardListD) and cardListC.count(cardListC[0]) != len(cardListC) and cardListS.count(cardListS[0]) != len(cardListS) and turn ==0:
            cardListPlayer = cardList[random.randint(0,3)] #card suit choice
            cardElemPlayer = random.randint(0,len(cardListPlayer)-1) #initial card value choice
            while cardListPlayer[cardElemPlayer]=="":
                cardListPlayer = cardList[random.randint(0,3)]
                cardElemPlayer = random.randint(0,len(cardListPlayer)-1) #removed card filter
            print(f"Player: {cardListPlayer[cardElemPlayer]}")
            playerList.append(cardElemPlayer)
            playerCard.append(cardListPlayer[cardElemPlayer][-1::]) #last list value [-1::]
            cardListPlayer[cardElemPlayer]=""
            cardListPlayer=0
            turn=1

    list.sort(playerList) #for straight and straight flush to work
    print(playerList)
    list.sort(playerCard)
    print(playerCard)
    #print(pairsP)

    if (len(playerList))==7:
        if((playerList[0]+4==playerList[1]+3==playerList[2]+2==playerList[3]+1==playerList[4] and playerCard[0]==playerCard[1]==playerCard[2]==playerCard[3]==playerCard[4]) or (playerList[1]+4==playerList[2]+3==playerList[3]+2==playerList[4]+1==playerList[5] and playerCard[1]==playerCard[2]==playerCard[3]==playerCard[4]==playerCard[5]) or (playerList[2]+4==playerList[3]+3==playerList[4]+2==playerList[5]+1==playerList[6] and playerCard[2]==playerCard[3]==playerCard[4]==playerCard[5]==playerCard[6])): #in-progress
            x=list(pairDictionary.keys())[7] #straight-flush
        elif(playerCard[0]==playerCard[1]==playerCard[2]==playerCard[3]==playerCard[4]) or (playerCard[1]==playerCard[2]==playerCard[3]==playerCard[4]==playerCard[5]) or (playerCard[2]==playerCard[3]==playerCard[4]==playerCard[5]==playerCard[6]):
            x=list(pairDictionary.keys())[6] #flush
        elif(playerList[0]+4==playerList[1]+3==playerList[2]+2==playerList[3]+1==playerList[4] or playerList[1]+4==playerList[2]+3==playerList[3]+2==playerList[4]+1==playerList[5] or playerList[2]+4==playerList[3]+3==playerList[4]+2==playerList[5]+1==playerList[6]):
            x=list(pairDictionary.keys())[5] #straight
        elif(playerList[0]==playerList[1]==playerList[2]==playerList[3]) or (playerList[1]==playerList[2]==playerList[3]==playerList[4]) or (playerList[2]==playerList[3]==playerList[4]==playerList[5]) or (playerList[3]==playerList[4]==playerList[5]==playerList[6]):
            x=list(pairDictionary.keys())[4] #4 of a kind
        elif(playerList[0]==playerList[1]==playerList[2]) or (playerList[1]==playerList[2]==playerList[3]) or (playerList[2]==playerList[3]==playerList[4]) or (playerList[3]==playerList[4]==playerList[5]) or (playerList[4]==playerList[5]==playerList[6]):
            x=list(pairDictionary.keys())[3] #3 of a kind
        elif(playerList[0]==playerList[1] and playerList[3]==playerList[4]) or (playerList[0]==playerList[1] and playerList[4]==playerList[5]) or (playerList[0]==playerList[1] and playerList[5]==playerList[6]): #in-progress, must scan through list and find highest pairs
            y=list(pairDictionary.keys())[2] #2pair
        elif(playerList[0]==playerList[1]) or (playerList[1]==playerList[2]) or (playerList[2]==playerList[3]) or (playerList[3]==playerList[4]) or (playerList[4]==playerList[5]) or (playerList[5]==playerList[6]):
            x=list(pairDictionary.keys())[1] #2 of a kind
        else:
            x=list(pairDictionary.keys())[0] #_high
        pairsP.append(x) #to display history of pairs
        print(pairsP)
    
    #SUFFICIENT FOR 2 PLAYER POKER
    if len(computerList) <=7:
        if cardListH.count(cardListH[0]) != len(cardListH) and cardListD.count(cardListD[0]) != len(cardListD) and cardListC.count(cardListC[0]) != len(cardListC) and cardListS.count(cardListS[0]) != len(cardListS) and turn ==1:
            cardListComputer= cardList[random.randint(0,3)] #card suit choice
            cardElemComputer = random.randint(0,len(cardListComputer)-1)
            while cardListComputer[cardElemComputer]=="":
                cardListComputer= cardList[random.randint(0,3)]
                cardElemComputer = random.randint(0,len(cardListComputer)-1) #removed card filter
            print(f"Computer: {cardListComputer[cardElemComputer]}")
            computerList.append(cardElemComputer)
            computerCard.append(cardListComputer[cardElemComputer][-1::]) #last list value [-1::]
            cardListComputer[cardElemComputer]=""
            cardListComputer=0
            turn=0
    
        #Card list that is used by both computer and player (2+5)
    #if len(playerList) <8 and len(computerList) <8:
    #if cardListH.count(cardListH[0]) != len(cardListH) and cardListD.count(cardListD[0]) != len(cardListD) and cardListC.count(cardListC[0]) != len(cardListC) and cardListS.count(cardListS[0]) != len(cardListS) and turn ==1:
    #    cardListAll = cardList[random.randint(0,3)] #card suit choice
    #    cardElemAll = random.randint(0,len(cardListAll)-1)
    #print(f"The flop: {cardListAll[cardElemAll]}")
    #allList.append(cardElemAll)
    #allCard.append(cardListAll[cardElemAll][-1::])
    #cardListAll[cardElemAll]=""
    #cardListAll=0
    #print(cardListAll)
    #playerList.append(cardElemAll)
    #playerCard.append(cardListPlayer[cardElemAll][-1::])
    #cardListPlayer[cardElemPlayer]=""
    #cardListPlayer=0
    #turn=1
    #computerList.append(cardElemAll)
    #computerCard.append(cardListComputer[cardElemAll][-1::])
    #cardListComputer[cardElemComputer]=""
    #cardListComputer=0
    #turn=0
    #print(allList)
    
    #POKER
    list.sort(computerList) #for more efficient pair finding to work
    print(computerList)
    list.sort(computerCard) #for flush to work
    print(computerCard)
    #print(pairsC)
    if (len(computerList))==7:
        if(computerList[0]+4==computerList[1]+3==computerList[2]+2==computerList[3]+1==computerList[4] and computerCard[0]==computerCard[1]==computerCard[2]==computerCard[3]==computerCard[4]):
            y=list(pairDictionary.keys())[7] #straight-flush
        elif(computerCard[0]==computerCard[1]==computerCard[2]==computerCard[3]==computerCard[4]) or (computerCard[1]==computerCard[2]==computerCard[3]==computerCard[4]==computerCard[5]) or (computerCard[2]==computerCard[3]==computerCard[4]==computerCard[5]==computerCard[6]):
            y=list(pairDictionary.keys())[6] #flush
        elif(computerList[0]+4==computerList[1]+3==computerList[2]+2==computerList[3]+1==computerList[4]) and (computerList[1]+4==computerList[2]+3==computerList[3]+2==computerList[4]+1==computerList[5]) or (computerList[2]+4==computerList[3]+3==computerList[4]+2==computerList[5]+1==computerList[6]):
            y=list(pairDictionary.keys())[5] #straight
        elif(computerList[0]==computerList[1]==computerList[2]==computerList[3]) or (computerList[1]==computerList[2]==computerList[3]==computerList[4]) or (computerList[2]==computerList[3]==computerList[4]==computerList[5]) or (computerList[3]==computerList[4]==computerList[5]==computerList[6]):
            y=list(pairDictionary.keys())[4] #4 of a kind
        elif(computerList[0]==computerList[1]==computerList[2]) or (computerList[1]==computerList[2]==computerList[3]) or (computerList[2]==computerList[3]==computerList[4]) or (computerList[3]==computerList[4]==computerList[5]) or (computerList[4]==computerList[5]==computerList[6]):
            y=list(pairDictionary.keys())[3] #3 of a kind
        elif(computerList[0]==computerList[1] and computerList[3]==computerList[4]) or (computerList[0]==computerList[1] and computerList[4]==computerList[5]) or (computerList[0]==computerList[1] and computerList[5]==computerList[6]): #in-progress, must scan through list and find highest pairs
            y=list(pairDictionary.keys())[2] #2pair
        elif(computerList[0]==computerList[1]) or (computerList[1]==computerList[2]) or (computerList[2]==computerList[3]) or (computerList[3]==computerList[4]) or (computerList[4]==computerList[5]) or (computerList[5]==computerList[6]):
            y=list(pairDictionary.keys())[1] #2 of a kind
            #to compare same pair values: 
            #1. find index of highest pair
            #2. find value of highest pair
            #3. compared player value of highest pair to computer value of highest pair
        else:
            y=list(pairDictionary.keys())[0] #_high
        pairsC.append(y) #to display history of pairs
        print(pairsC)

    #end round / shuffle       
    if (len(computerList))==7 and (len(playerList))==7:
        if pairDictionary[x]>pairDictionary[y]:
            playerChips+=1
            computerChips-=1
            print(f"PLAYER WON, {pairsP[-1::]} over {pairsC[-1::]}.")
            round +=1
        elif pairDictionary[x]<pairDictionary[y]:
            computerChips+=1
            playerChips-=1
            print(f"COMPUTER WON, {pairsC[-1::]} over {pairsP[-1::]}.")
            round +=1
        #No pair, high card sieve    
        elif pairDictionary[x]==0 and pairDictionary[y]==0 and playerList[-1::]>computerList[-1::]: #for "ace high, king high, etc. to work"
            playerChips+=1
            computerChips-=1
            print(f"PLAYER WON, {playerList[-1::].pop()} high.") 
            round +=1
        elif pairDictionary[x]==0 and pairDictionary[y]==0 and playerList[-1::]<computerList[-1::]: #for "ace high, king high, etc. to work"
            computerChips+=1
            playerChips-=1
            print(f"COMPUTER WON, {computerList[-1::].pop()} high.") 
            round +=1
        else:
            print("DRAW.")
            round +=1
        print(f"Round: {round}; Player chip total: {playerChips}; Computer chip total: {computerChips}\n")
        computerList,computerCard,playerList,playerCard=[],[],[],[] #ROUND RESET: reset round list for start of next round (shuffle)
        cardListH =["2_\u2661","3_\u2661","4_\u2661","5_\u2661","6_\u2661","7_\u2661","8_\u2661","9_\u2661","10_\u2661","JACK_\u2661","QUEEN_\u2661","KING_\u2661","ACE_\u2661"]
        cardListD =["2_\u25C6","3_\u25C6","4_\u25C6","5_\u25C6","6_\u25C6","7_\u25C6","8_\u25C6","9_\u25C6","10_\u25C6","JACK_\u25C6","QUEEN_\u25C6","KING_\u25C6","ACE_\u25C6"]
        cardListC =["2_\u2663","3_\u2663","4_\u2663","5_\u2663","6_\u2663","7_\u2663","8_\u2663","9_\u2663","10_\u2663","JACK_\u2663","QUEEN_\u2663","KING_\u2663","ACE_\u2663"]
        cardListS =["2_\u2660","3_\u2660","4_\u2660","5_\u2660","6_\u2660","7_\u2660","8_\u2660","9_\u2660","10_\u2660","JACK_\u2660","QUEEN_\u2660","KING_\u2660","ACE_\u2660"]
        cardList = [cardListH,cardListD,cardListC,cardListS] #ROUND RESET: reset card list for start of next round
    cardElemComputer,cardElemPlayer,cardElemAll=0,0,0 #CARD DRAW RESET: reset card elements for start of next card draw
    #print(cardList)

    cardGame(allList,allCard,cardElemAll,cardListAll,pairsP,pairsC,playerChips,playerList,playerCard,cardListPlayer,cardElemPlayer,computerChips,computerList,computerCard,cardListComputer,cardElemComputer,cardList,cardListH,cardListD,cardListC,cardListS,round,turn,x)
cardGame(allList,allCard,cardElemAll,cardListAll,pairsP,pairsC,playerChips,playerList,playerCard,cardListPlayer,cardElemPlayer,computerChips,computerList,computerCard,cardListComputer,cardElemComputer,cardList,cardListH,cardListD,cardListC,cardListS,round,turn,x)
