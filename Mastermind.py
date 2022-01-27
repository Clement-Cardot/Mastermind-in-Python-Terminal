import os
from random import randint

goal = randint(0000,9999)
a = goal // 1000
b = goal // 100 - a*10
c = goal // 10 - (a*100+b*10)
d = goal - (a*1000+b*100+c*10)
list_goal = [a,b,c,d]

result = ["_","_","_","_"]
Win = 0
i = 0
print(goal)
print(list_goal)
while Win == 0:
  data = int(input("Devinez ?"))
  w = data // 1000
  x = data // 100 - w*10
  y = data // 10 - (w*100 + x*10)
  z = data - (w*1000 + x*100 + y*10)
  list_data = [w,x,y,z]
  if(data == goal):
    print("Gagné !")
    Win = 1
    pass
  for number in list_data:
    for x in range(0,3):
      if(number == list_goal[x]):
        result[i] = "-"
      else:
        result[i] = "_"
    if(number == list_goal[i]):
      result[i] = "="
  i+=1
  print("Non, ",result)
        

os.system("pause")