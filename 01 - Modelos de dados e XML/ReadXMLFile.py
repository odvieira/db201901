#!/usr/bin/python3

from xml.dom.minidom import parse
import xml.dom.minidom
from pandas import DataFrame

class Hero_DataFrame(DataFrame):
    def __init__(self):
        # Calls the base class DataFrame's Init method to inherit the class
        super(Hero_DataFrame, self).__init__(columns=["id", "name", "popularity", "alignment",
                                                    "gender", "height_m", "weight_kg", "hometown",
                                                    "intelligence", "strength", "speed",
                                                    "durability", "energy_Projection", "fighting_Skills"])

        # Initiates a countage of heroes in this structure
        self.counter = 0

        return

    def new_Hero_DataFrame_line(self, hero):
        self.at[self.counter, "id"] = hero.getAttribute("id")

        for atributo in self.columns:
            if not (atributo == "id"):
                self.at[self.counter, atributo] = hero.getElementsByTagName(atributo)[
                    0].firstChild.nodeValue

        self.counter += 1

        return

# Start of the main function
if __name__ == "__main__":
    # Open XML document using minidom parser
    domTree = xml.dom.minidom.parse("marvel_simplificado.xml")

    universe = domTree.documentElement

    if universe.hasAttribute("name"):
        print("Root element : %s" % universe.hasAttribute("name"))

    # Init the objects that will manage the data colletected from XML
    heroes_all = Hero_DataFrame()
    heroes_good = Hero_DataFrame()
    heroes_bad = Hero_DataFrame()

    # Get all the heroes in the universe
    heroes = universe.getElementsByTagName("hero")

    # Init Total Weight
    tot_wght = 0

    # Iterate over collected data
    for hero in heroes:
        if (hero.getElementsByTagName('alignment')[0].firstChild.nodeValue == "Good"):
            heroes_good.new_Hero_DataFrame_line(hero)

        elif(hero.getElementsByTagName("alignment")[0].firstChild.nodeValue == "Bad"):
            heroes_bad.new_Hero_DataFrame_line(hero)

        heroes_all.new_Hero_DataFrame_line(hero)

        tot_wght += int(hero.getElementsByTagName("weight_kg")
                        [0].firstChild.nodeValue)

    heroes_all.to_csv("dadosMarvel/herois.csv", index=False)
    heroes_good.to_csv("dadosMarvel/herois_good.csv", index=False)
    heroes_bad.to_csv("dadosMarvel/herois_bad.csv", index=False)

    print("\nMédia de peso dos heróis: %i kg" % (tot_wght / heroes_all.counter))

    print("Herois Bons/Maus: %i/%i" % (
        heroes_good.counter, heroes_bad.counter))

    hulk = heroes_all[heroes_all.name == 'Hulk']

    imc_hulk = float(hulk['weight_kg'].values[0]) / (float(
        hulk['height_m'].values[0]) * float(hulk['height_m'].values[0]))

    print("IMC do Hulk: %f" % imc_hulk)
