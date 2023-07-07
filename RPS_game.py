import random
def get_choice():
    player_choice = input("Enter your choice") 
    options = ["rock", "scissors", "paper"]
    computer_choice = random.choice(options)
    random.choice(computer_choice)
    choices = {"player": player_choice, "computer":  computer_choice}
    
    return choices  

def check_win(player, computer):
    print(f'Your chose {player} Computer chose {computer}')
    if player == computer:
        return "It´s a tie"
    if player == 'rock':
        if computer == 'scissors':
            return "Player wins"
        if computer == 'paper':
            return "Computer wins"
    if player == 'paper':
        if computer == 'rock':
            return "Player wins"
        if computer == 'scissors':
            return "Computer wins"
    if player == 'scissors':
        if computer == 'paper':
            return "Player wins"
        if computer == 'rock':
            return "Computer wins"
result = get_choice()
print(check_win(result["player"],result["computer"] ))