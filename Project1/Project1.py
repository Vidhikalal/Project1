#project pig
import random
def roll():#Creting a function to generate random value 
    min_value=1
    max_value=6
    roll=random.randit(min_value,max_value)
    return roll

while True:
 players=input("Enter the number of player(1-4): ")
 if players.isdigit():
    players= int(players)
    if 2<= players <=4:
       break
    else:
        print("Must be between 2-4 players.")
 else:
       print("Invalid,try again.")

print(players)