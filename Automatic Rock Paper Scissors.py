import random
plrchoice = input("please choose either rock , paper , scissors") ---- burada oyuncu yani sizin girdiğiniz yazıyı alıyor. ( kağıt makas veya taş girmeniz beklenir )
b = 0
a = random.randint(1,3) -- a değişkenine rastgele 1 ve 3 arasında bir değer verecek. 1 ve 3 dahil.
botchoice = ""
if a == 1:
 botchoice = "rock"
if a == 2:
 bothoice = "paper"
if a == 3:
 botchoice = "scissors"
#------------------------------ Buralarda ise eğer komutları var. a bot'un girdiği yazıyı sayıya çevirir. b oyuncunun girdiği yazıyı sayıya çevirir.
if plrchoice == "rock":
  b = 1
if plrchoice == "paper":
  b = 2
if plrchoice == "scissors":
  b = 3


if plrchoice == "rock" or "paper" or "scissors":
   print("Bot's choice:", botchoice)
   print("  ")
   print("Your Choice:", plrchoice)   ----- burada oyuncunun yani sizin girdiğiniz yazıyı yazdırır ve botun rastgele hangisini seçtiğini de yazdırır. Daha sonra ise karşılaştırı. Örneğin: eğer oyuncu makas seçtiyse ve bot taş seçtiyse botun kazandığını ekrana yazdır
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
