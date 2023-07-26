
import json




healthRate=100;
healthRate1=100;
healthRate2=100;

def create_character(name):

    att = input("Please enter attack value");
    defe = input("Please enter defence value");
    
    Character = {'Name': name, 'Attack':att, 'Defence': defe, 'Health': healthRate}
    print(json.dumps(Character, indent = 4))
    

def create_opponents():
  
    opp1=input("Please enter a name for your first opponent");
    att1=input("Please enter an attack value for "+opp1);
    defe1=input("Please enter the defence value for "+opp1);

    opp2=input("Please enter a name for your second opponent");
    att2=input("Please enter an attack value for "+opp2);
    defe2=  input("Please enter the defence value for "+opp2);  


    Opponent_1 = {'Name': opp1, 'Attack':att1, 'Defence': defe1, 'Health': healthRate1}
    Opponent_2 = {'Name': opp2, 'Attack':att2, 'Defence': defe2, 'Health': healthRate2}
    print(json.dumps(Opponent_1, indent = 4))
    print(json.dumps(Opponent_2, indent = 4))
  

def battle(player, opponent):
    """
    This function simulates a battle between the player and an opponent. 
    It should return a dictionary with three keys: 'player', 'opponent', and 'outcome'. 
    'player' and 'opponent' should map to the names of the player and opponent. 
    'outcome' should map to a string that says "Player won" if the player won the battle, 
    and "Player lost" otherwise.
    """
    # Implement your code here
    pass

    AttcPlayer = player.get("Attack")
    AttcOpp =opponent.get("Attack")
    DefePlayer = player.get("Defence")
    DefeOpp=opponent.get("Defence")
    game_log ={}

    while healthRate1 & healthRate2 & healthRate !=0 :
        if(AttcPlayer>DefeOpp):
           Decrease= AttcPlayer-DefeOpp
        opponent.get("Health")-Decrease
        outcome = "player won the war"
        if(AttcOpp>DefePlayer):
           Decrease= AttcOpp-DefePlayer
        player.get("Health")-Decrease 
        outcome = "opponent won the war"
    fort = open("demofile3.txt", "w")
    fort.append(outcome)

def save_log_entry(entry):
    """
    This function saves a battle outcome to the "game_log.txt" file. 
    The 'entry' parameter is a dictionary representing a battle outcome, 
    which is returned by the `battle` function.
    """
    # Implement your code here
    pass

def play_game():
    """
    This function implements the game play. 
    It creates a player, creates opponents, 
    have the player battle the opponents one by one, 
    and save the outcome of each battle and the war using the `save_log_entry` function.
    """
   
play_game()
create_character('James')
create_opponents()