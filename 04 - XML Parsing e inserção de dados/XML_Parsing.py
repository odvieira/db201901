#!/usr/bin/python3

from xml.dom.minidom import parse
from urllib.request import urlopen
from pandas import DataFrame

class Person_DataFrame(DataFrame):
    def __init__(self):
        super(Person_DataFrame, self).__init__(columns=["uri", "name", "hometown", "birthdate"])

        self.counter = 0

        return

    def init_from_URL(self, url):
        domTree = parse(urlopen(url))

        persons = domTree.documentElement.getElementsByTagName("Person")

        for person in persons:
            self.new_Person_DataFrame_line(person)

        return

    def new_Person_DataFrame_line(self, person):

        for atributo in self.columns:
            self.at[self.counter, atributo] = person.getAttribute(atributo)

        self.counter += 1

        return

class AllLikesMusic_DataFrame(DataFrame):
    def __init__(self):
        super(AllLikesMusic_DataFrame, self).__init__(columns=["person", "rating", "bandUri"])

        self.counter = 0

        return

    def init_from_URL(self, url):
        domTree = parse(urlopen(url))

        allLikesMusic = domTree.documentElement.getElementsByTagName("LikesMusic")

        for likesMusic in allLikesMusic:
            self.new_AllLikesMusic_DataFrame_line(likesMusic)

        return


    def new_AllLikesMusic_DataFrame_line(self, likesMusic):

        for atributo in self.columns:
            self.at[self.counter, atributo] = likesMusic.getAttribute(atributo)

        self.counter += 1

        return

class AllLikesMovie_DataFrame(DataFrame):
    def __init__(self):
        super(AllLikesMovie_DataFrame, self).__init__(columns=["person", "rating", "movieUri"])

        self.counter = 0

        return

    def init_from_URL(self, url):
        domTree = parse(urlopen(url))

        allLikesMovie = domTree.documentElement.getElementsByTagName("LikesMovie")

        for likesMovie in allLikesMovie:
            self.new_AllLikesMovie_DataFrame_line(likesMovie)

        return


    def new_AllLikesMovie_DataFrame_line(self, likesMovie):

        for atributo in self.columns:
            self.at[self.counter, atributo] = likesMovie.getAttribute(atributo)

        self.counter += 1

        return

class AllKnows_DataFrame(DataFrame):
    def __init__(self):
        super(AllKnows_DataFrame, self).__init__(columns=["person", "colleague"])

        self.counter = 0

        return

    def init_from_URL(self, url):
        domTree = parse(urlopen(url))

        allKnows = domTree.documentElement.getElementsByTagName("Knows")

        for knows in allKnows:
            self.new_AllKnows_DataFrame_line(knows)

        return


    def new_AllKnows_DataFrame_line(self, allKnows):

        for atributo in self.columns:
            self.at[self.counter, atributo] = allKnows.getAttribute(atributo)

        self.counter += 1

        return

if __name__ == "__main__":
    
    persons = Person_DataFrame()
    persons.init_from_URL('http://dainf.ct.utfpr.edu.br/~gomesjr/BD1/data/person.xml')

    allLikesMusic = AllLikesMusic_DataFrame()
    allLikesMusic.init_from_URL('http://dainf.ct.utfpr.edu.br/~gomesjr/BD1/data/music.xml')

    allLikesMovie = AllLikesMovie_DataFrame()
    allLikesMovie.init_from_URL('http://dainf.ct.utfpr.edu.br/~gomesjr/BD1/data/movie.xml')

    allKnows = AllKnows_DataFrame()
    allKnows.init_from_URL('http://dainf.ct.utfpr.edu.br/~gomesjr/BD1/data/knows.xml')
