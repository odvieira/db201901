#!/usr/bin/python3

from xml.dom.minidom import parse
from urllib.request import urlopen
from pandas import DataFrame
from psycopg2 import extras, connect

class Person_DataFrame(DataFrame):
    def __init__(self):
        super(Person_DataFrame, self).__init__(
            columns=["uri", "name", "hometown", "birthdate"])

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
        super(AllLikesMusic_DataFrame, self).__init__(
            columns=["person", "rating", "bandUri"])

        self.counter = 0

        return

    def init_from_URL(self, url):
        domTree = parse(urlopen(url))

        allLikesMusic = domTree.documentElement.getElementsByTagName(
            "LikesMusic")

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
        super(AllLikesMovie_DataFrame, self).__init__(
            columns=["person", "rating", "movieUri"])

        self.counter = 0

        return

    def init_from_URL(self, url):
        domTree = parse(urlopen(url))

        allLikesMovie = domTree.documentElement.getElementsByTagName(
            "LikesMovie")

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
        super(AllKnows_DataFrame, self).__init__(
            columns=["person", "colleague"])

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
    credentials = "dbname='1901EquipePGDR' user='1901EquipePGDR' host='200.134.10.32' password='793953'"

    # try: # Persons parse
    #     persons = Person_DataFrame()
    #     persons.init_from_URL(
    #         'http://dainf.ct.utfpr.edu.br/~gomesjr/BD1/data/person.xml')

    #     values = []
    #     login = ''
    #     name = ''
    #     hometown = ''

    #     for i in range(persons.counter):
    #         for attr in persons.columns:
    #             if attr == 'uri':
    #                 login = persons.at[i, attr].split(
    #                     'http://utfpr.edu.br/CSB30/2019/1/')
    #             if attr == 'name':
    #                 name = persons.at[i, attr]
    #             if attr == 'hometown':
    #                 hometown = persons.at[i, attr]

    #         values.append(tuple([login[1], name, hometown]))

    #     query = 'INSERT INTO Usuario (Login, Nome, Cidade_natal) VALUES (%s, %s, %s)'

    #     with connect(credentials) as connection:
    #         with connection.cursor(cursor_factory=extras.DictCursor) as cur:
    #             try:
    #                 # print(cur.mogrify(query, values[0]))
    #                 cur.executemany(query, values)
    #             except Exception as e:
    #                 print(e)
    # except Exception as e:
    #     print(e)

    try:  # All likes Music
        allLikesMusic = AllLikesMusic_DataFrame()
        allLikesMusic.init_from_URL(
            'http://dainf.ct.utfpr.edu.br/~gomesjr/BD1/data/music.xml')

        values = []
        login = ''
        rating = 0
        bandaUri = ''

        for v in allLikesMusic.itertuples(index=False):
            login = v[0].split('http://utfpr.edu.br/CSB30/2019/1/')
            rating = v[1].split("'")
            bandaUri = v[2].split("https://en.wikipedia.org/wiki/")

            values.append(tuple([login[1], int(rating[0]), bandaUri[1]]))

        query = query = 'INSERT INTO UsuarioAvaliaArtistasMusicais (Login, Nota, Id) VALUES (%s, %s, %s)'

        with connect(credentials) as connection:
            with connection.cursor(cursor_factory=extras.DictCursor) as cur:
                try:
                    
                    cur.executemany(query, values)
                except Exception as e:
                    print(e)

    except Exception as e:
        print(e)

    try:  # All likes Movie
        allLikesMovie = AllLikesMovie_DataFrame()
        allLikesMovie.init_from_URL(
            'http://dainf.ct.utfpr.edu.br/~gomesjr/BD1/data/movie.xml')

        values = []
        login = ''
        rating = 0
        movieUri = ''

        for v in allLikesMovie.itertuples(index=False):
            login = v[0].split('http://utfpr.edu.br/CSB30/2019/1/')
            rating = v[1].split("'")
            movieUri = v[2].split("http://www.imdb.com/title/")

            values.append(tuple([login[1], int(rating[0]), movieUri[1]]))

        query = query = 'INSERT INTO UsuarioAvaliaFilme (Login, Nota, Id) VALUES (%s, %s, %s)'

        with connect(credentials) as connection:
            with connection.cursor(cursor_factory=extras.DictCursor) as cur:
                try:
                    cur.executemany(query, values)
                except Exception as e:
                    print(e)

    except Exception as e:
        print(e)

    try:  # All Knows
        allKnows = AllKnows_DataFrame()
        allKnows.init_from_URL(
            'http://dainf.ct.utfpr.edu.br/~gomesjr/BD1/data/knows.xml')

        values = []
        login = ''
        colleague = ''

        for v in allKnows.itertuples(index=False):
            login = v[0].split('http://utfpr.edu.br/CSB30/2019/1/')
            colleague = v[1].split('http://utfpr.edu.br/CSB30/2019/1/')

            values.append(tuple([login[1], colleague[1]]))

        query = query = 'INSERT INTO UsuarioRegistraConhecidoUsuario (Login, Login_registrado) VALUES (%s, %s)'

        with connect(credentials) as connection:
            with connection.cursor(cursor_factory=extras.DictCursor) as cur:
                try:
                    cur.executemany(query, values)
                except Exception as e:
                    print(e)

    except Exception as e:
        print(e)
