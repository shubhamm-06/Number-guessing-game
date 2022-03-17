# ********************Number Guessing Game************************** 
#                    ----------------------
#                                                                  Date : Saturday 13/11/2021 
#                                                                  Time : 10:15:00 AM



import random
L1 = random.randint(1,5)

def level1(num1):
  
    if num1 == L1:
        print("You guessed the corrrect number!")
    else:
     print("Guess again")

def hint(L1):
    if L1 == 1:
        print("Multiply or Divide me with any number, I will alwas give equal result . \n Who am I? \n*******************************************************************")
    elif L1 == 2 :
        print("I am smallest even number \n**************************** ")
    elif L1 == 3 :
        print("I can give you a bronze medal")
    elif L1 == 4:
        print("Square of me half of 32")
    elif L1 == 5:
        print("Multiply me with any number i will always give out 5 or zero as the last digit \n*********************************************************************")

def point():
    pass




b = hint(L1)
a = int(input("Guess the number :\n"))
c = level1(a)
hint(L1)
a1 = int(input("Guess the number :\n"))
c1 = level1(a1)


