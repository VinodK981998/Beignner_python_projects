#let the pc guess the number
# defining function for int inputs only (wrong input type handling)
# wrong feedback handling

import random

#defining a function to take positive int inputs only
def _input():
  number=''
  num=0
  while(number!='checked' or num<=0):
      if num<=0: print('Enter a postive number: ',end='')
      num=0 # to avoid asking for input twice incase of string input
      try:
          num=int(input())
          number='checked'
      except:
          print('Enter numbers only: ',end='')
          num=1 #to avoid asking for input twice here and if condition
          number='' #to avoid case when user enter negative number and then characters 
  return(num)

#RPS game
def play(x):
  player_score,computer_score=0,0
  while(max(player_score,computer_score)!=x):
    player=input("'r' for rock, 'p' for paper, 's' for scissor: ")
    computer=random.choice(['r','p','s'])
    #tie
    if player==computer: print(f'Tie. Current score is {player_score}-{computer_score}')
      #player won
    elif (player=='s' and computer=='p') or   (player=='r' and computer=='s') or (player=='p' and computer=='r'):
      player_score+=1
      print(f'You win. Current score is {player_score}-{computer_score}')
    elif (player=='p' and computer=='s') or   (player=='s' and computer=='r') or (player=='r' and computer=='p'):
      computer_score+=1
      print(f'You lost. Current score is {player_score}-{computer_score}')
    else: print('Give correct input')

  #final result
  if player_score==x: print(f'You won this match by {player_score}-{computer_score}')
  else: print(f'You lost this match by {player_score}-{computer_score}')

#main body
if __name__=='__main__':
  print('set the number of rounds needed to win the match')
  win_num=int(_input()) #int not necessary here as _input is returning int anyway
  play(win_num)