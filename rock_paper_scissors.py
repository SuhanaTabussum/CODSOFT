import random
print("Rock Paper Scissors Game")
user_choice=input("Enter Rock,Paper,or Scissors:")
choices=["Rock","Paper","Scissors"]
computer_choice=random.choice(choices)
print("Computer chose:",computer_choice)
if user_choice not in choices:
    print("Invalid chooice! Please enter Rock,Paper, or Scissors")
elif user_choice==computer_choice:
    print("It is a tie!")
elif user_choice=="Rock" and computer_choice=="Scissors":
    print("You win!")
elif user_choice=="Paper" and computer_choice=="Rock":
    print("you win1")
elif user_choice=="Scissors" and computer_choice=="Paper":
    print("You win!")
else:
    print("Computer wins!")