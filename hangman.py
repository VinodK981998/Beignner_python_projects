from words import words
import random
import string

#filtering words which contains '-' and ' '
def word_selector():
  word=random.choice(words).strip()
  while('-' in word) or (' ' in word): word=random.choice(words).strip()
  #print(word, len(word))
  return(word.upper()) #uppercase

def current_status(word,guessed_letters):
  guessed_word='_ '*len(word)
  for pos,letter in enumerate(word):
    if letter in guessed_letters:
        guessed_word=guessed_word[:2*pos]+letter+' '+guessed_word[2*(pos+1):] #extra spaces to make word more readable
  print(guessed_word,end='       ')
      
  

#main body
if __name__=='__main__':
  word = word_selector()
  letters_in_word=set(word) #letters in word
  guessed_letters = set([]) #guessed letters
  alphabet=string.ascii_uppercase
  #current_status(word,guessed_letters)
  #print(word,guessed_letters)
  lives=6 #total chances
  correct_letters=0
  while((len(letters_in_word)!=correct_letters) and lives != 0):
    let=input('Enter the letter: ').upper()
    if (let not in alphabet): print('Enter valid letter')
    elif (let in guessed_letters): print('Already Guessed')
    else:
      if let not in letters_in_word: lives-=1
      guessed_letters.add(let)
      correct_letters=len([x for x in letters_in_word if x in guessed_letters ]) # 1st way
      current_word=current_status(word,guessed_letters)
      print('❤ '*lives)
  
    if lives==0 : print(f'you died \n the word was {word}')  