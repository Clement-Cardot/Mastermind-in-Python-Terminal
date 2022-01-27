import os
from random import randint

a = randint(0,9)
b = randint(0,9)
c = randint(0,9)
d = randint(0,9)
reponse = a*1000+b*100+c*10+d  # Forme complète de la réponse
list_reponse = [a,b,c,d]
result = ["_","_","_","_"] #Réponse de la machine à l'utilisateur
Win = 0                    # Variable de Réussite
i = 0                      # variable d'incrémentation
print(reponse)
while Win == 0:
  data = int(input("Devinez ?")) # Forme complète de l'entrée utilisateur
  w = data // 1000
  x = data // 100 - w*10
  y = data // 10 - (w*100 + x*10)
  z = data - (w*1000 + x*100 + y*10)
  list_data = [w,x,y,z]         #Forme liste de l'entrée utilisateur
  if(data == reponse):
    print("Gagné !")
    Win = 1
    break
  for element in list_data:
    while y<4:
      if(element == list_reponse[y]):
        result[i] = "-"
        y=4
      else:
        result[i] = "_"
    if(element == list_reponse[i]):
      result[i] = "="
    i+=1
  print("Non, ",result)
        

os.system("pause")
