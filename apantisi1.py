import random
q=v=okk=0
host=bin=[]
def main():
 host=[]
 bin=[]
 def bingo(a, b):
  shared = []
  for num in a:
   if num in b:
    shared.append(num)
  if len(shared)==5 :
   print "BINGO"
   print "The player with the numbers:",a,"won the game."
   bin.append(5)
 players = 100*[5*[0]]
 def user(array):
  for i in range(100):
   array[i]=random.sample(range(1, 80), 5)
 user(players)
 from random import randint
 for _ in range(80):
   if 5 in bin:
    break
   x = randint(1, 80)
   print x
   host.append(x)
   for i in range(100):
    bingo(players[i],host)
 global v
 v=len(host)
while q<1000:
 okk+=v
 q+=1
 main()
else :
 okk+=v
 mo=float(okk/1000)
 print ("\n")
 print "The average ammount of numbers announced per game until theres a bingo in a game with 100 players for 1000 games is.."
 print ("\n")
 print "MESOS OROS / AVERAGE :  ",mo,"  NUMBERS ANNOUNCED PER GAME"