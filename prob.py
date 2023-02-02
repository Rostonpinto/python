import random

ticket_lottery = random.sample(range(1, 20), k=7)

print("Provide 7 numbers from 1 to 20 (one by one- separated by spacebars):")
ticket_input = list(map(int, input().split()))

tl = sorted(ticket_lottery)
ti = sorted(ticket_input)

points = 0
for number in ti:
   if number in tl:
       points +=1

print("Lottery numbers are: {}".format(tl))
print("       You selected: {} and got {} points".format(ti, points))

if (points < 3):
   print("       Thank you for trying!".format(points))
if (points == 3):
   print("       Your prize is £20. Congrats!")
if (points == 4):
   print("       Your prize is £40. Congrats!")
if (points == 5):
   print("       Your prize is £100. Congrats!")
if (points == 6):
   print("       Your prize is £10000. Congrats!")
if (points == 7):
   print("       Your prize is £1000000. Congrats!")
