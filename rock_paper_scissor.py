import random

emojis = {"r":"🌑","p":"📃","s":"✂️"}
game_opt = ["r","p","s"]

def get_user_choice():
    while True:
        user_choice = input("Rock, Paper or Scissor (r/p/s) : ").lower()
        if user_choice in game_opt:
            return user_choice
        else:
            print("Invalid Choice")

def display_choices(user_choice,computer_choice):
    print(f"You chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[computer_choice]}")



def determine_winner(user_choice,computer_choice):
    
        if user_choice == computer_choice:
                print("Tie !")
                
        elif ((user_choice == "r" and computer_choice == "s")or
            (user_choice == "p" and computer_choice == "r")or
            (user_choice == "s" and computer_choice == "p")):
                print("You Won !")
        else:
            print("You Lose !")
            
def play_game():            
    while True:
        user_choice = get_user_choice()
        
        computer_choice = random.choice(game_opt)
        
        display_choices(user_choice,computer_choice)
        determine_winner(user_choice,computer_choice)
                
        should_continue = input("Do you want to continue (y/n) : ").lower()
        if should_continue == "n":
            print("Thanks For Playing ")
            break
        
play_game()