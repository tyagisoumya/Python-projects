import random
options = ("rock" , "paper" , "scissors")
player = None
computer = random.choice(options)

running = True

while running:



   while player not in options:
      player = input("Enter a choice (rock , paper , scissors):")
   print(f"Player: {player}")
   print(f"Computer: {computer}")

   if player == computer:
    print("It's a tie!")
   elif player == "rock" and computer == "scissors":
    print("You win!")
   elif player == "paper" and computer == "rock":
    print("You win!")
   elif player == "scissors" and computer == "paper":
    print("You win!")
   else:
    print("You lose!")

   play_again =  input("Play again? (y/n): ").lower() 
   if not play_again == "y":
       running = False
print("Thanks for playing!")
