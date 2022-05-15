#let the pc guess the number
# defining function for int inputs only (wrong input type handling)
# wrong feedback handling

import random

#defining a function to take int inputs only
def _input():
  number=''
  while(number!='checked'):
      try:
          num=int(input())
          number='checked'
      except ValueError:
          print('Enter numbers only')
  return(num)

def Guess_pc(x):
  low,high=1,x
  feedback=''
  while feedback != 'c':
    try:
      guess=random.randint(low,high)
    except:
      return(print('Wrong feedbacks pls try again'))
    feedback=input(f'my guess is number {guess}, is it High(H), Low(L) or Correct(c): ').lower()
    if feedback=='h': high=guess-1
    elif feedback=='l': low=guess+1
    elif feedback!='c' : print('Wrong Input')
  print(f'correct guess is {guess}')

if __name__=='__main__':
  print('Enter higher bound: ',end='')
  high=_input()
  Guess_pc(high)
  
  
