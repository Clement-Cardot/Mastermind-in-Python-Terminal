# -*- coding: utf-8 -*-
import os
from random import randint
#Definitions des variables
list_goal = []
answer = ""
list_answer = []
list_result = ["","","",""]
Win = 0
jouer = True
correct = False
End = False
compteur = 0
#Fin de Definitions des Variables
# Règles du Mastermind
def Rules():
	print()
	print(" ", "Bienvenue Dans MasterMind V 3.0, Voici les règles :")
	print("   ", "1) L'ordinateur va choisir une combinaison de 4 chiffres")
	print("   ", "2) Vous Avez 12 Essaies pour la trouver")
	print("   ", "3) A chacune de vos propositions, l'ordinateur va vous donner un information sur les chiffres que vous avez entré :")
	print("      ", "a) Si votre chiffre est à la bonne place l'ordinateur répond =")
	print("      ", "b) Si votre chiffre n'est pas à la bonne place mais existe dans la combinaison l'ordinateur répond -")
	print("      ", "c) Si votre chiffre n'est pas dans la combinaison l'ordinateur répond _")
	print("   ", "4) Une fois la partie terminé, appuyé sur Y pour recommencer ou n pour Quitter")
	print()
# Fonction qui créé le nombre aléatoire
def random():
	global list_goal
	list_goal = []

	for i in range(0,4):
		list_goal.append(randint(0,9)) 

# Fonction qui gère les réponse du joueur
def user():
	global correct
	correct = False
	global answer
	global list_answer

	while correct == False:
		list_answer = []
		print("Devinez ?")
		answer = input()
		i=0

		for char in answer:
			list_answer.append(ord(char)-48)
			if ord(char)-48 < 0 or ord(char)-48 > 9:
				correct = False
				break
		if len(list_answer) != 4:
			print("Saisie incorrect, veuillez recommencer !")
			correct = False

		elif len(list_answer) == 4:
			correct = True

# Fonction qui compare les deux valeurs des fonctions précédentes
def comparaison():
	global list_answer
	global list_result
	global list_goal
	global Win

	if list_answer == list_goal:
		Win = 1

	else:
		i = 0

		for element in list_answer:

			if (element in list_goal) == True:
				list_result[i] = "-"

			else:
				list_result[i] = "_"

			if element == list_goal[i]:
				list_result[i] = "="

			i = i+1		
#Fonction qui répond au joueur
def reponse():
	global End
	global list_result

	if Win == 1:
		print("Gagné")
		End = 1

	else:
		print("Non, ",list_result[0],list_result[1],list_result[2],list_result[3]) 

#Fonction qui fixe le nombre d'essaie
def count():
	global compteur
	compteur += 1

	if compteur == 12:
		End = True
		print("Nombre d'essaies maximum atteint !")

# Partie Graphique **************************************************************************************************************************************************************************************
a = u"\u2588"
b = u"\u25A0"
print()
print("************************************************************************************************************************") 
print("              ",2*a,"    ",2*a,  "    ",2*a, "    ",5*a,   ""       ,7*a ,  "", 5*a , ""    , 5*a     , "  ",2*a,"    ",2*a  , "", 5*a , "", 2*a," ",a,  "", 3*a)
print("              ",a,a,"  ",a,a,    "   ",a,"",a,"  ",a, "        "     , a,  "   ",a  , "    ", a,"  ",a, " ",a,a,"  ",a,a     , "  ", a , "  ",a,a, "",a ,"",a,"",2*a)
print("              ",a,"",a,"",a,"",a,"  ",a+4*b+a,"  " ,5*a,    "   "      , a,"   ",5*a, "", 5*a         , "  ",a,"",a,"",a,"",a, "  ", a , "  ",a,"",a,a  ,"",a," ",a)
print("              ",a," ",2*a," ",a, " ",a,"    ",a,"      ",a,  "  "     ,a,  "   ",a  , "    ", a,"  ",a, " ",a," ",2*a," ",a  , "  ", a , "  ",a," ",2*a ,"",a,"",2*a)
print("              ",a,"      ",a,    "",a,"      ",a,"",5*a,    "   "      ,a, "   ",5*a, "", a,"   ",a   , "",a,"      ",a      , "", 5*a , "",a, "  ",a,   "", 3*a)
print()
print("***********************************************************************************************************************")
print(" ", "Made by Clément Cardot -- ESEO 2019")
print()
print()
# FIN Partie Graphique **********************************************************************************************************************************************************************************

if __name__ == '__main__':
	print("Voulez-vous lire les règles ? Y/n")

	if input() == "Y":
		Rules()

	while jouer == True:
		random()
			  
		while End == False :
			user()
			comparaison()
			reponse()
			count()
		print("Voulez-vous rejouer ? Y/n")
		again = input()

		if again == "n":
			jouer = False

		elif again == "Y":
			jouer = True
			Win = 0

		End = False
	print("   ", "A la prochaine ;)")
os.system("pause")