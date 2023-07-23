from getpass import getpass as input
print
# Get info from players on if they want rock, paper, or scissors

PlayerOne = input ("Choose Either Rock Paper Or Scissor (r,p,s) and press enter to submit your choice. ")

PlayerTwo = input ("Choose Either Rock Paper Or Scissor (r,p,s) and press enter to submit your choice")

# Check the input (r,p,s)
if PlayerOne and PlayerTwo == ("r"):
  print()
  print ("The two rocks hit eachother, but they are both fine. Draw")
elif PlayerOne == ("r") and PlayerTwo == ("p"):
  print()
  print ("Paper covers the rock. Player 2 wins!")
elif PlayerOne == ("r") and PlayerTwo == ("s"):
  print()
  print ("Rock Breaks The Scissors. Player 1 wins!")
elif PlayerOne == ("p") and PlayerTwo == ("r"):
  print()
  print ("Paper covers the rock. Player 1 wins!")
elif PlayerOne == ("p") and PlayerTwo == ("p"):
  print()
  print ("Paper tries to fight with paper, but it fails. Draw")
elif PlayerOne == ("p") and PlayerTwo == ("s"):
  print()
  print ("Ouch! Paper gets cut by scissor. Player 2 wins!")
elif PlayerOne == ("s") and PlayerTwo == ("p"):
  print()
  print ("We never knew what happened to paper. Player 1 wins!")
elif PlayerOne == ("s") and PlayerTwo == ("s"):
  print()
  print ("Scissor tries to cut scissor but its no use. Draw!")
  print()
  print ("Paper covers the rock. Player 1 wins!")
else:
  print ("bruh enter in the correct input (r,p,s) not anything else. Restart the game to play.")
