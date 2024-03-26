import random
plrchoice = input("please choose either rock , paper , scissors")
b = 0
a = random.randint(1,3)
botchoice = ""
if a == 1:
 botchoice = "rock"
if a == 2:
 bothoice = "paper"
if a == 3:
 botchoice = "scissors"
#------------------------------
if plrchoice == "rock":
  b = 1
if plrchoice == "paper":
  b = 2
if plrchoice == "scissors":
  b = 3

if plrchoice != "rock" or "paper" or "scissors":
    print("Not a valid input!")
elif plrchoice == "rock" or "paper" or "scissors":
   print("Bot's choice:", botchoice)
   print("  ")
   print("Your Choice:", plrchoice)
if a == 1 and b == 2:
  print("Player won!")
elif a == 2 and b == 3:
    print("Player won!")
elif a == 3 and b == 1:
    print("Player won!")
if a == 1 and b == 3:
    print("Bot won!")
if a == 2 and b == 1:
       print("Bot won!")
if a == 3 and b == 2:
       print("Bot won!")
if a == b:
       print("It's a tie!")
