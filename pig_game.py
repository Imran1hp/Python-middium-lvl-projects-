import random 

def dice_roll():
    roll = random.randint(1,6) 
    return roll

while True:
   players =input("Enter the number of players(2-4): ")

   if players.isdigit():
        players=int(players)
        if 2 <= players <=4:
            break
        else:
            print("Must be between 2 and 4 players")   
   else:
        print("Ivalid number of players")

print(f"{players} players are playing the game")

max_score =50
player_scores = [0 for _ in range(players)]


while max(player_scores)<max_score:

    for player_index in range(players):
        current_score =0
        print(f"Player{player_index +1}'s turn")
        print(f"Your total score is {player_scores[player_index]} \n")

        while True: 

            should_roll =input("would you like to roll the dice (y): ").lower()
            if should_roll.lower() !='y':
                break

            value =dice_roll()
            if value ==1:
                print("You rolled a 1! Turn done!")
                currnt_score = 0
                break
            else:
                current_score+=value
                print("you rolled a: ",value)    
            print("Your current score is ",current_score)
        
        player_scores[player_index] +=current_score
        print(f"Player{player_index +1} totalscore is {player_scores[player_index]}")
    
max_score =max_score(player_scores)

winning_player =player_scores.index(max_score)
print(f"Player{winning_player +1} wins with a score of {max_score}")
