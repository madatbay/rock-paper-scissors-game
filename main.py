import random

list = ['Rock','Paper','Scissors']
scoreA = 0
scoreG = 0

def score():
  print("Computer :", scoreA)
  print("You :", scoreG)

def checkTie():
  if ai == guess:
    return True

def checkWin():
  if guess==1:
    if ai == 3:
      return True
  if guess==2:
    if ai==1:
      return True
  if guess==3:
    if ai==2:
      return True

while scoreA != 3 and scoreG != 3:
    ai = random.randrange(1, 4)
    guess =int(input("\n1.Rock \n2.Paper \n3.Scissors\n It's your turn ( 1-3 ):"))
    print("\nComputer's choice: ", ai)
    print("Your choice : ", guess)
    if checkWin():
        print("""\n
               **********
        Woow...You won this round...
               *********
        \n""")
        scoreG +=1
        score()
    elif checkTie():
        print("""\n
             **********
        It's just a simple TIE!...
             **********
        \n""")
        score()
    else:
        print("""\n
             **********
        You lost this round!...
             **********
        \n""")
        scoreA +=1
        score()


print("\n Game over...")
if scoreG == 3:
  print("Congratulations... You won the game!")
else:
  print("Opsss.You lost...")