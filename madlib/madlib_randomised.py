#using string concatenation
from random_madlib import hobbies, personal
import random

if __name__=='__main__':
  question = random.choice([hobbies, personal])
  question.madlib()
  