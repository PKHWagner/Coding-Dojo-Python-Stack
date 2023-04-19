import random
def magic_number_game():
  the_magic_number = random.randint(1,100)
  win = False
  while win == False:
    guess=int(input('guess the magic number->'))  
    if guess == the_magic_number:
      win = True
      print(f"You Win!")
    elif guess < the_magic_number:
      print(f"The Magic Number is between {guess} and 100")
      
    else: 
      guess > the_magic_number
      print(f"The Magic Number is between 1 and {guess}")
      
  return the_magic_number

print(magic_number_game())    




