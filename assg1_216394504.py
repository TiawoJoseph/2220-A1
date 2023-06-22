#Joseph Ogunnupe 
#tjogunnupe@outlook.com 
#216-394-504

round =0

while (round<10){
points = 100;
cards = random.randint (1, 100)
}



# Will return a random number between 2-14. takes no param
getCardValue()

#paramater is card value a number between 2-14. Will convert the integer to a string 
#Integers 2 to 9 are converted to "2" .. "9". | 10 to "T", 11 to "J", 12 to "Q", 13 to "K", and 14 to "A" 
#returns a string 
getCardStr(cardValue)


#Will repeatedly as the player  "High or Low (H/L)?:"
#Return: Depending on what is entered, return the string "HIGH" or the string"LOW"
getHLGuess()


# Param is maximum -int. Maximum should be the players current number of points they have. 
# This will continually ask the player to input bet amount. Check to make sure the bet is between 1 and max. If it is less that 0 
#or over the max ask the player to enter it in again.
getBetAmount(maximum)

# Params card 1 and card 2 represent the integer values of the two cards. Param bet type is a string that is either high or low. 
# Depending on the bettype see if the palyer was correct.
# For example, if the betType was "HIGH" and Card1 > Card2, then the user was
#incorrect (False). Think carefully about all the cases for the player to be right or wrong.
#Return: return True or False (Boolean) depending on if the guess was right
playerGuessCorrect(card1, card2, betType)