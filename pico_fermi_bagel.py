from random import randrange

comps_num = randrange(1, 10)

for i in range(2):
       myguess = int(input("Guess a number between 1 and 9: "))
       
       if myguess == comps_num:
              print("Fermi!")
       else:
              print("Bagels!")   


