def madlib():
  Name = input('Name: ')
  sports = input('Fav sport: ')
  Actor = input('Fav Actor: ')

  madlib = f"Hello there {Name}. How are you doing?\n\
Your favorite sports is {sports} \n\
your favorite actor is {Actor}"

  print(madlib)

if __name__=='__main__':
  madlib()