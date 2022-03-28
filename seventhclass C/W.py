# import random
# from unittest import result
# user = input("Enter a choice (rock, paper, scissors): ")
# options = ["rock", "paper", "scissors"]
# comp = random.choice(options)

# print(f"\nYou chose {user}, computer chose {comp}.\n")

# if user == comp:
#     print(f"Both players selected {user}. It's a tie!")
# elif user == "rock":
#     if comp == "scissors":
#         print("Rock smashes scissors! You win!")
#     else:
#         print("Paper covers rock! You lose.")
# elif user == "paper":
#     if comp == "rock":
#         print("Paper covers rock! You win!")
#     else:
#         print("Scissors cuts paper! You lose.")
# elif user == "scissors":
#     if comp == "paper":
#         print("Scissors cuts paper! You win!")
#     else:
#         print("Rock smashes scissors! You lose.")



# import random

# Choices = [r, p, s]
# def check_winner(player_choice, com_choice):
#     if player_choice == "r" and com_choice=="s":
#         return "player wins"
#     elif player_choice == "p" and com_choice== "r":
#         return "player wins"
#     elif player_choice == "s" and com_choice== "p":
#         return "player wins"
#     elif player_choice == "s" and com_choice== "r":
#             return "computer wins"
#     elif player_choice == "r" and com_choice== "p":
#         return "computer wins"
#     elif player_choice == "p" and com_choice== "p":
#         return "computer wins"
#     else:
#         return "it's a tie!"

    
# print("welcome to rock, paper, scissors.\n enter R for Rock, P for Paper and S for Scissors.")

#     player_choice = input(">").lower()
#     com_choice = random.choice(choices)
#     if player_choice in random.choices:
#         result = check_winner(player_choice, com_choice)

#         print(result)
#         print(f"Computer selected {com_choice}")

#     else: 
#         print("Invalid Input")

import random
def game():
    a = (3,2,5,6,8,7)

    print(f"Select any number from {a}.\nWe hope it doesn't end in tears.")
    com_choice = random.choice(a)
    random.shuffle(a)
    print("Guess the number:")
    user_choice = int(input(">>"))

    if user_choice in a:
        if user_choice == com_choice:
            print("All power belongs to you comrade")
        else:
            print("Arhhh, comrade. Be like you go try again o.")
    else:
            print("Comrade no be so!")

while True:
    game()
    c = input("Continue?\n>")
    if c == "y":
        continue
    else:
        break
