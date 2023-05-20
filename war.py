#WAR card game - highest card wins
#goal poker, percentage chance of winning - for multiple picks make draw card function and place before turn trigger, decrease code
import random #import the random module to generate random numbers

print("Welcome to the card game! Whoever has the highest card wins")
cardListH =["2_\u2661","3_\u2661","4_\u2661","5_\u2661","6_\u2661","7_\u2661","8_\u2661","9_\u2661","10_\u2661","JACK_\u2661","QUEEN_\u2661","KING_\u2661","ACE_\u2661"]
cardListD =["2_\u25C6","3_\u25C6","4_\u25C6","5_\u25C6","6_\u25C6","7_\u25C6","8_\u25C6","9_\u25C6","10_\u25C6","JACK_\u25C6","QUEEN_\u25C6","KING_\u25C6","ACE_\u25C6"]
cardListC =["2_\u2663","3_\u2663","4_\u2663","5_\u2663","6_\u2663","7_\u2663","8_\u2663","9_\u2663","10_\u2663","JACK_\u2663","QUEEN_\u2663","KING_\u2663","ACE_\u2663"]
cardListS =["2_\u2660","3_\u2660","4_\u2660","5_\u2660","6_\u2660","7_\u2660","8_\u2660","9_\u2660","10_\u2660","JACK_\u2660","QUEEN_\u2660","KING_\u2660","ACE_\u2660"]
cardList = [cardListH,cardListD,cardListC,cardListS]
cardListPlayer, cardListComputer = [],[]
cardElemPlayer, cardElemComputer = 0,0
choiceC, choiceP =0,0

playerPoints = 0 #initial score of player and computer outside of game loop
computerPoints = 0

choiceP = random.randint(0,3) #initial cardList choice, suit choice - PLAYER
choiceC = random.randint(0,3)
x, turn, round =0,0,0
#using these functions will not allow score area to compare card element values
#def filterP(turn,x,cardList,choiceP,choiceC,playerPoints,computerPoints,cardListPlayer,cardElemPlayer,cardListComputer,cardElemComputer,cardListH,cardListD,cardListC,cardListS,round):
#    cardElemPlayer = random.randint(0,len(cardListPlayer)-1) #initial card value choice
#    while cardListPlayer[cardElemPlayer]=="":
#        cardListComputer= cardList[random.randint(0,3-x)]
#        cardElemPlayer = random.randint(0,len(cardListPlayer)-1) #removed card filter
#    print(f"Player: {cardListPlayer[cardElemPlayer]}")
#    cardListPlayer[cardElemPlayer]=""
#    cardListPlayer=0
#    choiceP=0
#    return turn,x,cardList,choiceP,choiceC,playerPoints,computerPoints,cardListPlayer,cardElemPlayer,cardListComputer,cardElemComputer,cardListH,cardListD,cardListC,cardListS,round

#def filterC(turn,x,cardList,choiceP,choiceC,playerPoints,computerPoints,cardListPlayer,cardElemPlayer,cardListComputer,cardElemComputer,cardListH,cardListD,cardListC,cardListS,round):
#    cardElemComputer = random.randint(0,len(cardListComputer)-1)
#    while cardListComputer[cardElemComputer]=="":
#        cardListComputer= cardList[random.randint(0,3-x)]
#        cardElemComputer = random.randint(0,len(cardListComputer)-1) #removed card filter
#    print(f"Computer: {cardListComputer[cardElemComputer]}")
#    cardListComputer[cardElemComputer]=""
#    cardListComputer=0
#    choiceC=0
#    return turn,x,cardList,choiceP,choiceC,playerPoints,computerPoints,cardListPlayer,cardElemPlayer,cardListComputer,cardElemComputer,cardListH,cardListD,cardListC,cardListS,round


def cardGame(turn,x,cardList,choiceP,choiceC,playerPoints,computerPoints,cardListPlayer,cardElemPlayer,cardListComputer,cardElemComputer,cardListH,cardListD,cardListC,cardListS,round): #To force completion of game
    input("Press (D) to deal")
    
    if cardListH.count(cardListH[0]) == len(cardListH) and cardListD.count(cardListD[0]) == len(cardListD) and cardListC.count(cardListC[0]) == len(cardListC) and cardListS.count(cardListS[0]) != len(cardListS) and turn==0:
        cardList=[cardListS]
        cardListPlayer = cardList[0]
        cardElemPlayer = random.randint(0,len(cardListPlayer)-1) #initial card value choice
        while cardListPlayer[cardElemPlayer]=="":
            cardListPlayer = cardList[0]
            cardElemPlayer = random.randint(0,len(cardListPlayer)-1) #removed card filter
        print(f"Player: {cardListPlayer[cardElemPlayer]}")
        cardListPlayer[cardElemPlayer]=""
        cardListPlayer=0
        choiceP=0
        turn=1
    elif cardListH.count(cardListH[0]) == len(cardListH) and cardListC.count(cardListC[0]) == len(cardListC) and cardListS.count(cardListS[0]) == len(cardListS) and cardListD.count(cardListD[0]) != len(cardListD) and turn==0:
        cardList=[cardListD]
        cardListPlayer = cardList[0]
        cardElemPlayer = random.randint(0,len(cardListPlayer)-1) #initial card value choice
        while cardListPlayer[cardElemPlayer]=="":
            cardListPlayer = cardList[0]
            cardElemPlayer = random.randint(0,len(cardListPlayer)-1) #removed card filter
        print(f"Player: {cardListPlayer[cardElemPlayer]}")
        cardListPlayer[cardElemPlayer]=""
        cardListPlayer=0
        choiceP=0
        turn=1
    elif cardListH.count(cardListH[0]) == len(cardListH) and cardListS.count(cardListS[0]) == len(cardListS) and cardListD.count(cardListD[0]) == len(cardListD) and cardListC.count(cardListC[0]) != len(cardListC) and turn ==0:
        cardList=[cardListC]
        cardListPlayer = cardList[0]
        cardElemPlayer = random.randint(0,len(cardListPlayer)-1) #initial card value choice
        while cardListPlayer[cardElemPlayer]=="":
            cardListPlayer = cardList[0]
            cardElemPlayer = random.randint(0,len(cardListPlayer)-1) #removed card filter
        print(f"Player: {cardListPlayer[cardElemPlayer]}")
        cardListPlayer[cardElemPlayer]=""
        cardListPlayer=0
        choiceP=0
        turn=1
    elif cardListD.count(cardListD[0]) == len(cardListD) and cardListC.count(cardListC[0]) == len(cardListC) and cardListS.count(cardListS[0]) == len(cardListS) and cardListH.count(cardListH[0]) != len(cardListH) and turn==0:
        cardList=[cardListH]
        cardListPlayer = cardList[0]
        cardElemPlayer = random.randint(0,len(cardListPlayer)-1) #initial card value choice
        while cardListPlayer[cardElemPlayer]=="":
            cardListPlayer = cardList[0]
            cardElemPlayer = random.randint(0,len(cardListPlayer)-1) #removed card filter
        print(f"Player: {cardListPlayer[cardElemPlayer]}")
        cardListPlayer[cardElemPlayer]=""
        cardListPlayer=0
        choiceP=0
        turn=1

    elif cardListH.count(cardListH[0]) == len(cardListH) and cardListD.count(cardListD[0]) == len(cardListD)and turn ==0:
        cardList=[cardListC,cardListS]
        x=2
        choiceP = random.randint(0,3-x)
        cardListPlayer= cardList[choiceP]
        cardElemPlayer = random.randint(0,len(cardListPlayer)-1) #initial card value choice
        while cardListPlayer[cardElemPlayer]=="":
            cardListPlayer = cardList[random.randint(0,3-x)]
            cardElemPlayer = random.randint(0,len(cardListPlayer)-1) #removed card filter
        print(f"Player: {cardListPlayer[cardElemPlayer]}")
        cardListPlayer[cardElemPlayer]=""
        cardListPlayer=0
        choiceP=0
        turn=1
    elif cardListH.count(cardListH[0]) == len(cardListH) and cardListC.count(cardListC[0]) == len(cardListC) and turn==0:
        cardList=[cardListD,cardListS]
        x=2
        choiceP = random.randint(0,3-x)
        cardListPlayer= cardList[choiceP]
        cardElemPlayer = random.randint(0,len(cardListPlayer)-1) #initial card value choice
        while cardListPlayer[cardElemPlayer]=="":
            cardListPlayer = cardList[random.randint(0,3-x)]
            cardElemPlayer = random.randint(0,len(cardListPlayer)-1) #removed card filter
        print(f"Player: {cardListPlayer[cardElemPlayer]}")
        cardListPlayer[cardElemPlayer]=""
        cardListPlayer=0
        choiceP=0
        turn=1
    elif cardListH.count(cardListH[0]) == len(cardListH) and cardListS.count(cardListS[0]) == len(cardListS) and turn ==0:
        cardList=[cardListD,cardListC]
        x=2
        choiceP = random.randint(0,3-x)
        cardListPlayer= cardList[choiceP]
        cardElemPlayer = random.randint(0,len(cardListPlayer)-1) #initial card value choice
        while cardListPlayer[cardElemPlayer]=="":
            cardListPlayer = cardList[random.randint(0,3-x)]
            cardElemPlayer = random.randint(0,len(cardListPlayer)-1) #removed card filter
        print(f"Player: {cardListPlayer[cardElemPlayer]}")
        cardListPlayer[cardElemPlayer]=""
        cardListPlayer=0
        choiceP=0
        turn=1
    elif cardListD.count(cardListD[0]) == len(cardListD) and cardListC.count(cardListC[0]) == len(cardListC) and turn ==0:
        cardList=[cardListH,cardListS]
        x=2
        choiceP = random.randint(0,3-x)
        cardListPlayer= cardList[choiceP]
        cardElemPlayer = random.randint(0,len(cardListPlayer)-1) #initial card value choice
        while cardListPlayer[cardElemPlayer]=="":
            cardListPlayer = cardList[random.randint(0,3-x)]
            cardElemPlayer = random.randint(0,len(cardListPlayer)-1) #removed card filter
        print(f"Player: {cardListPlayer[cardElemPlayer]}")
        cardListPlayer[cardElemPlayer]=""
        cardListPlayer=0
        choiceP=0
        turn=1
    elif cardListD.count(cardListD[0]) == len(cardListD) and cardListS.count(cardListS[0]) == len(cardListS) and turn ==0:
        cardList=[cardListH,cardListC]
        x=2
        choiceP = random.randint(0,3-x)
        cardListPlayer= cardList[choiceP]
        cardElemPlayer = random.randint(0,len(cardListPlayer)-1) #initial card value choice
        while cardListPlayer[cardElemPlayer]=="":
            cardListPlayer = cardList[random.randint(0,3-x)]
            cardElemPlayer = random.randint(0,len(cardListPlayer)-1) #removed card filter
        print(f"Player: {cardListPlayer[cardElemPlayer]}")
        cardListPlayer[cardElemPlayer]=""
        cardListPlayer=0
        choiceP=0
        turn=1
    elif cardListC.count(cardListC[0]) == len(cardListC) and cardListS.count(cardListS[0]) == len(cardListS) and turn==0:
        cardList=[cardListH,cardListD]
        x=2
        choiceP = random.randint(0,3-x)
        cardListPlayer= cardList[choiceP]
        cardElemPlayer = random.randint(0,len(cardListPlayer)-1) #initial card value choice
        while cardListPlayer[cardElemPlayer]=="":
            cardListPlayer = cardList[random.randint(0,3-x)]
            cardElemPlayer = random.randint(0,len(cardListPlayer)-1) #removed card filter
        print(f"Player: {cardListPlayer[cardElemPlayer]}")
        cardListPlayer[cardElemPlayer]=""
        cardListPlayer=0
        choiceP=0
        turn=1

    elif cardListH.count(cardListH[0]) == len(cardListH) and turn ==0:
        cardList=[cardListD,cardListC,cardListS]
        x=1
        choiceP = random.randint(0,3-x)
        cardListPlayer= cardList[choiceP]
        cardElemPlayer = random.randint(0,len(cardListPlayer)-1) #initial card value choice
        while cardListPlayer[cardElemPlayer]=="":
            cardListPlayer = cardList[random.randint(0,3-x)]
            cardElemPlayer = random.randint(0,len(cardListPlayer)-1) #removed card filter
        print(f"Player: {cardListPlayer[cardElemPlayer]}")
        cardListPlayer[cardElemPlayer]=""
        cardListPlayer=0
        choiceP=0
        turn=1

    elif cardListD.count(cardListD[0]) == len(cardListD) and turn ==0:
        cardList=[cardListH,cardListC,cardListS]
        x=1
        choiceP = random.randint(0,3-x)
        cardListPlayer= cardList[choiceP]
        cardElemPlayer = random.randint(0,len(cardListPlayer)-1) #initial card value choice
        while cardListPlayer[cardElemPlayer]=="":
            cardListPlayer = cardList[random.randint(0,3-x)]
            cardElemPlayer = random.randint(0,len(cardListPlayer)-1) #removed card filter
        print(f"Player: {cardListPlayer[cardElemPlayer]}")
        cardListPlayer[cardElemPlayer]=""
        cardListPlayer=0
        choiceP=0
        turn=1
    elif cardListD.count(cardListD[0]) == len(cardListC) and turn ==0:
        cardList=[cardListH,cardListD,cardListS]
        x=1
        choiceP = random.randint(0,3-x)
        cardListPlayer= cardList[choiceP]
        cardElemPlayer = random.randint(0,len(cardListPlayer)-1) #initial card value choice
        while cardListPlayer[cardElemPlayer]=="":
            cardListPlayer = cardList[random.randint(0,3-x)]
            cardElemPlayer = random.randint(0,len(cardListPlayer)-1) #removed card filter
        print(f"Player: {cardListPlayer[cardElemPlayer]}")
        cardListPlayer[cardElemPlayer]=""
        cardListPlayer=0
        choiceP=0
        turn=1
    elif cardListS.count(cardListS[0]) == len(cardListS) and turn ==0:
        cardList=[cardListH,cardListD,cardListC]
        x=1
        choiceP = random.randint(0,3-x)
        cardListPlayer= cardList[choiceP]
        cardElemPlayer = random.randint(0,len(cardListPlayer)-1) #initial card value choice
        while cardListPlayer[cardElemPlayer]=="":
            cardListPlayer = cardList[random.randint(0,3-x)]
            cardElemPlayer = random.randint(0,len(cardListPlayer)-1) #removed card filter
        print(f"Player: {cardListPlayer[cardElemPlayer]}")
        cardListPlayer[cardElemPlayer]=""
        cardListPlayer=0
        choiceP=0
        turn=1
    elif cardListH.count(cardListH[0]) != len(cardListH) and cardListD.count(cardListD[0]) != len(cardListD) and cardListC.count(cardListC[0]) != len(cardListC) and cardListS.count(cardListS[0]) != len(cardListS) and turn ==0:
        cardListPlayer = cardList[random.randint(0,3)] #card suit choice
        cardElemPlayer = random.randint(0,len(cardListPlayer)-1) #initial card value choice
        while cardListPlayer[cardElemPlayer]=="":
            cardListPlayer = cardList[random.randint(0,3)]
            cardElemPlayer = random.randint(0,len(cardListPlayer)-1) #removed card filter
        print(f"Player: {cardListPlayer[cardElemPlayer]}")
        cardListPlayer[cardElemPlayer]=""
        cardListPlayer=0
        choiceP=0
        turn=1



    if cardListH.count(cardListH[0]) == len(cardListH) and cardListD.count(cardListD[0]) == len(cardListD) and cardListC.count(cardListC[0]) == len(cardListC) and cardListS.count(cardListS[0]) != len(cardListS) and turn==1:
        cardList=[cardListS]
        x=3
        cardListComputer = cardList[0]
        cardElemComputer = random.randint(0,len(cardListComputer)-1)
        while cardListComputer[cardElemComputer]=="":
            cardListComputer= cardList[random.randint(0,3-x)]
            cardElemComputer = random.randint(0,len(cardListComputer)-1) #removed card filter
        print(f"Computer: {cardListComputer[cardElemComputer]}")
        cardListComputer[cardElemComputer]=""
        cardListComputer=0
        choiceC=0
        turn=0
    elif cardListH.count(cardListH[0]) == len(cardListH) and cardListC.count(cardListC[0]) == len(cardListC) and cardListS.count(cardListS[0]) == len(cardListS) and cardListD.count(cardListD[0]) != len(cardListD) and turn==1:
        cardList=[cardListD]
        x=3
        cardListComputer = cardList[0]
        cardElemComputer = random.randint(0,len(cardListComputer)-1)
        while cardListComputer[cardElemComputer]=="":
            cardListComputer= cardList[random.randint(0,3-x)]
            cardElemComputer = random.randint(0,len(cardListComputer)-1) #removed card filter
        print(f"Computer: {cardListComputer[cardElemComputer]}")
        cardListComputer[cardElemComputer]=""
        cardListComputer=0
        choiceC=0
        turn=0
    elif cardListH.count(cardListH[0]) == len(cardListH) and cardListS.count(cardListS[0]) == len(cardListS) and cardListD.count(cardListD[0]) == len(cardListD) and cardListC.count(cardListC[0]) != len(cardListC) and turn ==1:
        cardList=[cardListC]
        x=3
        cardListComputer = cardList[0]
        cardElemComputer = random.randint(0,len(cardListComputer)-1)
        while cardListComputer[cardElemComputer]=="":
            cardListComputer= cardList[random.randint(0,3-x)]
            cardElemComputer = random.randint(0,len(cardListComputer)-1) #removed card filter
        print(f"Computer: {cardListComputer[cardElemComputer]}")
        cardListComputer[cardElemComputer]=""
        cardListComputer=0
        choiceC=0
        turn=0
    elif cardListD.count(cardListD[0]) == len(cardListD) and cardListC.count(cardListC[0]) == len(cardListC) and cardListS.count(cardListS[0]) == len(cardListS) and cardListH.count(cardListH[0]) != len(cardListH) and turn==1:
        cardList=[cardListH]
        x=3
        cardListComputer = cardList[0]
        cardElemComputer = random.randint(0,len(cardListComputer)-1)
        while cardListComputer[cardElemComputer]=="":
            cardListComputer= cardList[random.randint(0,3-x)]
            cardElemComputer = random.randint(0,len(cardListComputer)-1) #removed card filter
        print(f"Computer: {cardListComputer[cardElemComputer]}")
        cardListComputer[cardElemComputer]=""
        cardListComputer=0
        choiceC=0
        turn=0

    elif cardListH.count(cardListH[0]) == len(cardListH) and cardListD.count(cardListD[0]) == len(cardListD) and turn==1:
        cardList=[cardListC,cardListS]
        x=2
        choiceC = random.randint(0,3-x)
        cardListComputer= cardList[choiceC]
        cardElemComputer = random.randint(0,len(cardListComputer)-1) #initial card value choice
        while cardListComputer[cardElemComputer]=="":
            cardListComputer= cardList[random.randint(0,3-x)]
            cardElemComputer = random.randint(0,len(cardListComputer)-1) #removed card filter
        print(f"Computer: {cardListComputer[cardElemComputer]}")
        cardListComputer[cardElemComputer]=""
        cardListComputer=0
        choiceC=0
        turn=0
    elif cardListH.count(cardListH[0]) == len(cardListH) and cardListC.count(cardListC[0]) == len(cardListC) and turn ==1:
        cardList=[cardListD,cardListS]
        x=2
        choiceC = random.randint(0,3-x)
        cardListComputer= cardList[choiceC]
        cardElemComputer = random.randint(0,len(cardListComputer)-1) #initial card value choice
        while cardListComputer[cardElemComputer]=="":
            cardListComputer= cardList[random.randint(0,3-x)]
            cardElemComputer = random.randint(0,len(cardListComputer)-1) #removed card filter
        print(f"Computer: {cardListComputer[cardElemComputer]}")
        cardListComputer[cardElemComputer]=""
        cardListComputer=0
        choiceC=0
        turn=0
    elif cardListH.count(cardListH[0]) == len(cardListH) and cardListS.count(cardListS[0]) == len(cardListS) and turn ==1:
        cardList=[cardListD,cardListC]
        x=2
        choiceC = random.randint(0,3-x)
        cardListComputer= cardList[choiceC]
        cardElemComputer = random.randint(0,len(cardListComputer)-1) #initial card value choice
        while cardListComputer[cardElemComputer]=="":
            cardListComputer= cardList[random.randint(0,3-x)]
            cardElemComputer = random.randint(0,len(cardListComputer)-1) #removed card filter
        print(f"Computer: {cardListComputer[cardElemComputer]}")
        cardListComputer[cardElemComputer]=""
        cardListComputer=0
        choiceC=0
        turn=0
    elif cardListD.count(cardListD[0]) == len(cardListD) and cardListC.count(cardListC[0]) == len(cardListC) and turn==1:
        cardList=[cardListH,cardListS]
        x=2
        choiceC = random.randint(0,3-x)
        cardListComputer= cardList[choiceC]
        cardElemComputer = random.randint(0,len(cardListComputer)-1) #initial card value choice
        while cardListComputer[cardElemComputer]=="":
            cardListComputer= cardList[random.randint(0,3-x)]
            cardElemComputer = random.randint(0,len(cardListComputer)-1) #removed card filter
        print(f"Computer: {cardListComputer[cardElemComputer]}")
        cardListComputer[cardElemComputer]=""
        cardListComputer=0
        choiceC=0
        turn=0
    elif cardListD.count(cardListD[0]) == len(cardListD) and cardListS.count(cardListS[0]) == len(cardListS) and turn ==1:
        cardList=[cardListH,cardListC]
        x=2
        choiceC = random.randint(0,3-x)
        cardListComputer= cardList[choiceC]
        cardElemComputer = random.randint(0,len(cardListComputer)-1) #initial card value choice
        while cardListComputer[cardElemComputer]=="":
            cardListComputer= cardList[random.randint(0,3-x)]
            cardElemComputer = random.randint(0,len(cardListComputer)-1) #removed card filter
        print(f"Computer: {cardListComputer[cardElemComputer]}")
        cardListComputer[cardElemComputer]=""
        cardListComputer=0
        choiceC=0
        turn=0
    elif cardListC.count(cardListC[0]) == len(cardListC) and cardListS.count(cardListS[0]) == len(cardListS) and turn ==1:
        cardList=[cardListH,cardListD]
        x=2
        choiceC = random.randint(0,3-x)
        cardListComputer= cardList[choiceC]
        cardElemComputer = random.randint(0,len(cardListComputer)-1) #initial card value choice
        while cardListComputer[cardElemComputer]=="":
            cardListComputer= cardList[random.randint(0,3-x)]
            cardElemComputer = random.randint(0,len(cardListComputer)-1) #removed card filter
        print(f"Computer: {cardListComputer[cardElemComputer]}")
        cardListComputer[cardElemComputer]=""
        cardListComputer=0
        choiceC=0
        turn=0

    elif cardListH.count(cardListH[0]) == len(cardListH) and turn ==1:
        cardList=[cardListD,cardListC,cardListS]
        x=1
        choiceC = random.randint(0,3-x)
        cardListComputer= cardList[choiceC]
        cardElemComputer = random.randint(0,len(cardListComputer)-1) #initial card value choice
        while cardListComputer[cardElemComputer]=="":
            cardListComputer= cardList[random.randint(0,3-x)]
            cardElemComputer = random.randint(0,len(cardListComputer)-1) #removed card filter
        print(f"Computer: {cardListComputer[cardElemComputer]}")
        cardListComputer[cardElemComputer]=""
        cardListComputer=0
        choiceC=0
        turn=0
    elif cardListD.count(cardListD[0]) == len(cardListD) and turn ==1:
        cardList=[cardListH,cardListC,cardListS]
        x=1
        choiceC = random.randint(0,3-x)
        cardListComputer= cardList[choiceC]
        cardElemComputer = random.randint(0,len(cardListComputer)-1) #initial card value choice
        while cardListComputer[cardElemComputer]=="":
            cardListComputer= cardList[random.randint(0,3-x)]
            cardElemComputer = random.randint(0,len(cardListComputer)-1) #removed card filter
        print(f"Computer: {cardListComputer[cardElemComputer]}")
        cardListComputer[cardElemComputer]=""
        cardListComputer=0
        choiceC=0
        turn=0
    elif cardListC.count(cardListC[0]) == len(cardListC) and turn ==1:
        cardList=[cardListH,cardListD,cardListS]
        x=1
        choiceC = random.randint(0,3-x)
        cardListComputer= cardList[choiceC]
        cardElemComputer = random.randint(0,len(cardListComputer)-1) #initial card value choice
        while cardListComputer[cardElemComputer]=="":
            cardListComputer= cardList[random.randint(0,3-x)]
            cardElemComputer = random.randint(0,len(cardListComputer)-1) #removed card filter
        print(f"Computer: {cardListComputer[cardElemComputer]}")
        cardListComputer[cardElemComputer]=""
        cardListComputer=0
        choiceC=0
        turn=0
    elif cardListS.count(cardListS[0]) == len(cardListS) and turn ==1:
        cardList=[cardListH,cardListD,cardListC]
        x=1
        choiceC = random.randint(0,3-x)
        cardListComputer= cardList[choiceC]
        cardElemComputer = random.randint(0,len(cardListComputer)-1) #initial card value choice
        while cardListComputer[cardElemComputer]=="":
            cardListComputer= cardList[random.randint(0,3-x)]
            cardElemComputer = random.randint(0,len(cardListComputer)-1) #removed card filter
        print(f"Computer: {cardListComputer[cardElemComputer]}")
        cardListComputer[cardElemComputer]=""
        cardListComputer=0
        choiceC=0
        turn=0
    elif cardListH.count(cardListH[0]) != len(cardListH) and cardListD.count(cardListD[0]) != len(cardListD) and cardListC.count(cardListC[0]) != len(cardListC) and cardListS.count(cardListS[0]) != len(cardListS) and turn ==1:
        cardListComputer= cardList[random.randint(0,3)] #card suit choice
        x=0
        cardElemComputer = random.randint(0,len(cardListComputer)-1)
        while cardListComputer[cardElemComputer]=="":
            cardListComputer= cardList[random.randint(0,3-x)]
            cardElemComputer = random.randint(0,len(cardListComputer)-1) #removed card filter
        print(f"Computer: {cardListComputer[cardElemComputer]}")
        cardListComputer[cardElemComputer]=""
        cardListComputer=0
        choiceC=0
        turn=0

    #PLAYER VS. COMPUTER
    if(cardElemPlayer)>(cardElemComputer):
        playerPoints+=1
    elif(cardElemPlayer)<(cardElemComputer):
        computerPoints+=1
    else:
        print("DEAL AGAIN.")
    print(f"Player points: {playerPoints} Computer points: {computerPoints}")
    round +=1
    print("Round: " + str(round))
    cardElemComputer=0
    cardElemPlayer=0
    choiceP = random.randint(0,3-x)
    choiceC = random.randint(0,3-x)
    print(cardList)

    if round ==26:
        if playerPoints>computerPoints:
            print("PLAYER WON.") 
        elif playerPoints<computerPoints:
            print("COMPUTER WON.") 
        else:
            print("DRAW.")

    cardGame(turn,x,cardList,choiceC,choiceP,playerPoints,computerPoints,cardListPlayer,cardElemPlayer,cardListComputer,cardElemComputer,cardListH,cardListD,cardListC,cardListS,round)

cardGame(turn,x,cardList,choiceC,choiceP,playerPoints,computerPoints,cardListPlayer,cardElemPlayer,cardListComputer,cardElemComputer,cardListH,cardListD,cardListC,cardListS,round)
