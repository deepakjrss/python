import random
user_input= input("Enter a choice of :(rock,paper,scissors)")
possible_actions =["rock","paper","scissors"]
computer_action = random.choice(possible_actions)

#print user action and computer action

if user_input=="rock" and computer_action=="paper":
    print("you loose")

if user_input=="rock" and computer_action=="rock":
    print("it is a tie")
elif user_input=="scissors" and computer_action=="rock":
    print("user input won")
elif user_input=="rock" and computer_action=="scissors":
    print("computer has won")
elif user_input=="scissors" and computer_action=="paper":
    print("user input  won") 
elif user_input=="paper" and computer_action=="scissors":
    print("computer action is won")           
