#guess the number
import random

def Guess(x):
  y=int(input('Guess the number: '))
  if x==y: print('Correct Guess')
  elif x<y: 
    print('Guess is high. Guess again') 
    Guess(x)
  else: 
    print('Guess is low. Guess again')
    Guess(x)
  

if __name__=='__main__':
  n=int(input('Upper Limit for the number: '))
  x=random.randint(1,n)
  print(x)
  Guess(x)


#Altn soln
import random

def Guess2(x):
  random_number=random.randint(1,x)
  guess=0 #random no. will never be zero
  while(random_number != guess):
    guess=int(input(f'guess the number btw 1 and {x}: '))
    if(guess>random_number): print('Guess is High Guess again') 
    elif(guess<random_number): print('Guess is low Guess again')
  print(f'correct guess. The number was {random_number}')

Guess2(int(input('Higher Limit: ')))