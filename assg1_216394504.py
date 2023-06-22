#Joseph Ogunnupe 
#tjogunnupe@outlook.com 
#216-394-504
import random
round =1

# Will return a random number between 2-14. takes no param
def getCardValue():
   cards = random.randint (2, 14)
   return cards


#paramater is card value a number between 2-14. Will convert the integer to a string 
#Integers 2 to 9 are converted to "2" .. "9". | 10 to "T", 11 to "J", 12 to "Q", 13 to "K", and 14 to "A" 
#returns a string 
def getCardStr(cardValue):
    value="S"
    if cardValue <=9 & cardValue>=2:
        value=str(cardValue)
    elif cardValue ==10:
        value="T"
    elif cardValue ==11:
        value="J"
    elif cardValue ==12:
        value="Q"
    elif cardValue ==13:
        value="K"
    else: 
        value="A"
    return value


#Will repeatedly as the player  "High or Low (H/L)?:"
#Return: Depending on what is entered, return the string "HIGH" or the string"LOW"
def getHLGuess():
    HL=input('High or Low (H/L)?:')
    return HL


# Param is maximum -int. Maximum should be the players current number of points they have. 
# This will continually ask the player to input bet amount. Check to make sure the bet is between 1 and max. If it is less that 0 
#or over the max ask the player to enter it in again.
def getBetAmount(maximum):
    bet = int(input('Input bet amount:'))
    while bet<1 or bet>maximum:
        bet = int(input('Input bet amount:'))
    return bet

# Params card 1 and card 2 represent the integer values of the two cards. Param bet type is a string that is either high or low. 
# Depending on the bettype see if the palyer was correct.
# For example, if the betType was "HIGH" and Card1 > Card2, then the user was
#incorrect (False). Think carefully about all the cases for the player to be right or wrong.
#Return: return True or False (Boolean) depending on if the guess was right
def playerGuessCorrect(card1, card2, betType):
    truth = False
    #Loosing scenarios 
    if (card1<card2):
        if(betType == 'Low'):
            truth = False
    elif (card1>card2): 
        if(betType =='High'):
            truth =False
    #Winning Scenarios
    elif (card1>card2):
        if(betType == 'Low'):
            truth = True
    elif (card1<card2):
        if(betType =='High'):
            truth =True 
    elif (card1==card2):
        truth = False
    return truth

points = 100

while round<11:
    card=getCardValue()
    snake=getCardValue()
    print('---------------------------------------')
    print('OVERALL POINTS: ',points,' ROUND: ',round)
    print ('First card is a ', '[',snake, ']')
    guess=getHLGuess()
    print (guess)
    bet=getBetAmount(points)
    print(bet)
    print('Second card is a ', '[',card, ']' )
    print ('You bet ', guess, 'for ', bet)
    if(playerGuessCorrect(snake, card, guess) == True):
        print('YOU WON')
        points+=bet
        #if the bets are more than 500 exit the game 
    else:
        print('You Lost')
        points-=bet

    if (points=500):
        print('You have reached ', points, ' points in ',rounds, ' rounds' )
    elif (points==0):
        print('You have run out of points')
    elif (rounds=10 & point<500):
        print
    round+=1
