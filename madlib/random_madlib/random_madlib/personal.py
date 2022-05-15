def madlib():
  Name = input('Name: ')
  Age = input('Age: ')
  College = input('College: ')

  madlib = f"Hello there {Name}. How are you doing?\n\
You will be {Age} years old this year.\n\
You are graduated from {College}"

  print(madlib)
if __name__=='__main__':
  madlib()
