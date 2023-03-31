import random

#紙牌常數
SUIT_TUPLE=('Spades','Hearts','Clubs','Diamonds')
RANK_TUPLE=('Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King')

NCARDS=8

#傳入一個排組 並從排組中拿到一張隨機的牌
def getCard(deckListIn):
    thisCard=deckListIn.pop() #抽出一張隨機的牌
    return thisCard

#洗牌
def shuffle(deckListIn):
    deckListOut=deckListIn.copy() #原始牌組
    random.shuffle(deckListOut)   #洗牌
    return deckListOut

#主程式
if __name__ == '__main__':
    print('Welcome to Higher or Lower!')
    print('You have to choose whether the next card to be shown will be higher or lower than the current card.')
    print('Right decision earn 20 points;wrong decision lose 15 points.')
    print('You have 50 point at the beginning. Good Luck!')
    print()

    startingDeckList=[]
    for suit in SUIT_TUPLE:
        for thisValue, rank in enumerate(RANK_TUPLE):
            cardDict = {'rank':rank,'suit':suit,'value':thisValue+1}
            startingDeckList.append(cardDict)
    score=50
while True:
    print()
    gameDecklist=shuffle(startingDeckList)
    currentCardDict=getCard(gameDecklist)
    currentCardRank=currentCardDict['rank']
    currentCardSuit=currentCardDict['suit']
    currentCardValue=currentCardDict['value']
    print('starting card is :',currentCardRank+' of '+currentCardSuit+'. Enter q to quit.')
    print()
    answer=input('Will the next card be higher or lower than the ' +currentCardRank+' of '+currentCardSuit+' ? (enter h or l): ').lower()
    for cardNumber in range(0,NCARDS):
        anser=answer.casefold()
        nextCardDict=getCard(gameDecklist)
        nextCardRank=currentCardDict['rank']
        nextCardSuit=currentCardDict['suit']
        nextCardValue=currentCardDict['value']        

    if answer =='h':
        print('Next card is:', nextCardRank+' of '+nextCardSuit)
        if nextCardValue > currentCardValue:
            print('You got it right, it was higher')
            score=score+20
            print('Your score is:', score)
        else:
            print('Sorry, it was not higher')
            score=score-15
            print('Your score is:', score)
        currentCardDict=nextCardDict
        currentCardValue=nextCardValue
    elif answer =='l':
        print('Next card is:', nextCardRank+' of '+nextCardSuit)
        if nextCardValue < currentCardValue:
            print('You got it right, it was higher')
            score=score+20
            print('Your score is:', score)
        else:
            print('Sorry, it was not higher')
            score=score-15
            print('Your score is:', score)
        currentCardDict=nextCardDict
        currentCardValue=nextCardValue
    elif answer =='q':
        break
    else:
        print()
        print('Enter q to quit.')    
print('Your score is:', score)        
print('OK bye') 
