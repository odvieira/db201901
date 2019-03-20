#!/usr/bin/python

from xml.dom.minidom import parse
import xml.dom.minidom
import pandas as pd

atributos = ["id","name","popularity","alignment","gender","height_m","weight_kg","hometown","intelligence","strength","speed","durability","energy_Projection","fighting_Skills"]

def new_csv_line(index,dataFrame,hero):
	dataFrame.at[index,"id"] = hero.getAttribute("id")
	for atributo in atributos:
		if not (atributo=="id"):
			dataFrame.at[index,atributo] = hero.getElementsByTagName(atributo)[0].firstChild.nodeValue

	return dataFrame

# Open XML document using minidom parser
DOMTree = xml.dom.minidom.parse("marvel_simplificado.xml")

universe = DOMTree.documentElement
if universe.hasAttribute("name"):
   print("Root element : %s" % universe.getAttribute("name"))

heroes_csv = pd.DataFrame(columns=atributos)
herois_good = pd.DataFrame(columns=atributos)
herois_bad = pd.DataFrame(columns=atributos)

# Get all the heroes in the universe
heroes = universe.getElementsByTagName("hero")
counter = 0
counter_good = 0
counter_bad = 0

for hero in heroes:
	if(hero.getElementsByTagName("alignment")[0].firstChild.nodeValue == "Good"):
		new_csv_line(counter_good,herois_good,hero)
		counter_good += 1
	elif(hero.getElementsByTagName("alignment")[0].firstChild.nodeValue == "Bad"):
		new_csv_line(counter_bad,herois_bad,hero)
		counter_bad +=1
	
	new_csv_line(counter,heroes_csv,hero)
	counter+=1

heroes_csv.to_csv("dadosMarvel/herois.csv", index=False)
herois_good.to_csv("dadosMarvel/herois_good.csv", index=False)
herois_bad.to_csv("dadosMarvel/herois_bad.csv", index=False)
