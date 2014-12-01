#/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# pythonFonctionParallelepipede.py
#
# Ecrivez un programme qui calcule le volume d'un parallelepipede rectangle dont sont
# fournis au depart la largeur, la hauteur et la profondeur.
#
# Copyright 2014 yves Mercadier <yves.mercadier@ac-montpellier.fr>
#
#specifications
#parametre :
# aucun
#retour :
# v un nombre reel representant la vitesse en miles
def entree():
#Les entrees du programme
 print ("Calcul du volume d'un parallelepipede.\n")
 v = float(input("Indiquez la vitesse en miles?"))
 return v
#specifications
#parametre :
# v un nombre reel reprsentant la vitese en miles
#retour
# k un nombre reel representant la vitesse en kilomètre/heure
# 
def metier(v):
#le calcul
 k= l*1,609
 return v
#specifications
#parametre :
# v un nombre reel representant la vitesse en miles
# aucun
def pourImpression(v):
#les sorties du programme
 print ("\nLa vitesse en kilomètre/heure est : "+str(v)+" kilomètreheure.")
print (" ---> Debut du programme.\n")
vitesse=entree()
vitesse=metier(vitesse)
pourImpression(vitesse)
print ("\n ---> Fin du programme.")
