#!/usr/bin/python

from xml.dom.minidom import parse
import xml.dom.minidom
import pandas as pd

# Open XML document using minidom parser
DOMTree = xml.dom.minidom.parse("marvel_simplificado.xml")

universe = DOMTree.documentElement
if universe.hasAttribute("name"):
   print("Root element : %s" % universe.getAttribute("name"))

atributos = ["name","popularity","alignment","gender","height_m","weight_kg","hometown","intelligence","strength","speed","durability","energy_Projection","fighting_Skills"]
heroes_csv = pd.DataFrame(columns=atributos)
herois_good = pd.DataFrame(columns=atributos)
herois_bad = pd.DataFrame(columns=atributos)
# Get all the heroes in the universe
heroes = universe.getElementsByTagName("hero")
counter = 0
for hero in heroes:
    if(hero.getElementsByTagName("alignment")[0].firstChild.nodeValue == )
    for atributo in atributos:
        # print(hero.getElementsByTagName(atributo)[0].firstChild.nodeValue)
        if(atributo == "alignment"):

        heroes_csv.at[counter,atributo] = hero.getElementsByTagName(atributo)[0].firstChild.nodeValue
    counter+=1
heroes_csv.to_csv("dadosMarvel/herois.csv",sep=",",index_label="id")

# Print detail of each hero.
for hero in heroes:
   print("*****Hero*****")
   if hero.hasAttribute("id"):
      print("Id: %s" % hero.getAttribute("id"))

   name = hero.getElementsByTagName('name')[0]
   print("Name: %s" % name.childNodes[0].data)
