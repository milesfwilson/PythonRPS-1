import random


choices = ["rock", "paper", "scissors"]
playerScore = 0
computerScore = 0

while playerScore < 5 and computerScore < 5:
  playerInput = input("Rock, Paper, Scissors... ")
  computerInput = choices[random.randrange(0,3)]
  print("You: " + playerInput + " ||| Computer: " + computerInput)
  if playerInput == choices[0] and computerInput == choices[1]:
    computerScore += 1
  elif playerInput == computerInput:
    print("No Point")
  elif playerInput == choices[0] and computerInput == choices[2]:
    playerScore +=1
  elif playerInput == choices[1] and computerInput == choices[0]:
    playerScore +=1
  elif playerInput == choices[1] and computerInput == choices[2]:
    computerScore += 1
  elif playerInput == choices[2] and computerInput == choices[0]:
    computerScore +1
  elif playerInput == choices[2] and computerInput == choices[1]:
    playerScore += 1
  else: 
    print("Please Enter a Valid Choice")
  print(playerScore, computerScore)

if computerScore > playerScore:
  print("You lose!")
else: 
  print("You win!")

