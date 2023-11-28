from getpass import getpass as input
import emoji
print(emoji.emojize("This is a game of :rock: and :paper: and :scissors:"))
print(emoji.emojize("R stands for Rock :rock:"))
print("P stands for Paper")
print(emoji.emojize("S stands for Scissors :scissors:"))
print()
possible_actions = ["R","P","S"]
print("Choose your action(R, P or S)")
print()
score_player1 = 0
score_player2 = 0
while True: 
  player1_action = input("Player1 > ")
  print()
  
  player2_action = input("Player2 > ")
  print()
  
  if(player1_action =="R"):
    if(player2_action =="R"):
      print("You both chose Rock, It's a tie!")
    elif(player2_action =="S"):
      print("Player1's Rock smashes Player2's Scissors! Player1 wins!")
      score_player1 += 1
      
    elif(player2_action =="P"):
      print("Player2's Paper smothers Player1's Rock! Player2 wins!")
      score_player2 += 1
      
  elif(player1_action =="P"):
    if(player2_action =="R"):
      print("Player1's Rock smothers Player2's Paper! Player1 wins!")
      score_player1 += 1
      
    
    elif(player2_action =="S"):
      print("Player2's Scissors will shred  Player1's Paper! Player2 wins!")
      score_player2 += 1
      
    elif(player2_action =="P"):
      print("Both chose Paper ! It's a tie! ")
  elif(player1_action =="S"):
    if(player2_action =="R"):
      print("Player2's Rock smashes Player1's Scissors! Player2 wins!")
      score_player2 += 1
      
    elif(player2_action =="P"):
      print("Player1's Scissors will shred Player2's Paper. Player1 wins!")
      score_player1 += 1
    elif(player2_action =="S"):
      print("Both chose Scissors, it's a Tie!")
      
    print("Player1 has", score_player1, "wins!")
  print("Player2 has", score_player2, "wins!")

  if score_player1 ==3 or score_player2 ==3:
    print("Thanks for playing!")
    exit()
  else:
    continue