#!/usr/bin/python3

from psycopg2 import extras, connect
from parselib import Person_DataFrame, AllKnows_DataFrame, AllLikesMovie_DataFrame, AllLikesMusic_DataFrame

if __name__ == "__main__":
    credentials = "dbname='1901EquipePGDR' user='1901EquipePGDR' host='200.134.10.32' password='793953'"

    try: # Persons parse
        persons = Person_DataFrame()
        persons.init_from_URL(
            'http://dainf.ct.utfpr.edu.br/~gomesjr/BD1/data/person.xml')

        values = []
        login = ''
        name = ''
        hometown = ''

        for i in range(persons.counter):
            for attr in persons.columns:
                if attr == 'uri':
                    login = persons.at[i, attr].split(
                        'http://utfpr.edu.br/CSB30/2019/1/')
                if attr == 'name':
                    name = persons.at[i, attr]
                if attr == 'hometown':
                    hometown = persons.at[i, attr]

            values.append(tuple([login[1], name, hometown]))

        query = 'INSERT INTO Usuario (Login, Nome, Cidade_natal) VALUES (%s, %s, %s)'

        with connect(credentials) as connection:
            with connection.cursor(cursor_factory=extras.DictCursor) as cur:
                try:
                    # print(cur.mogrify(query, values[0]))
                    cur.executemany(query, values)
                except Exception as e:
                    print(e)
    except Exception as e:
        print(e)

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

        with connect(credentials) as connection:
            with connection.cursor(cursor_factory=extras.DictCursor) as cur:
                try:  # adding artistasmusicais Ids
                    lst = []
                    for v in values:
                        item = tuple([v[2]])
                        if item not in lst:
                            lst.append(item)

                    cur.executemany(
                        'INSERT INTO artistasmusicais (Id) VALUES (%s)', lst)
                except Exception as e:
                    print(e)

        query = 'INSERT INTO UsuarioAvaliaArtistasMusicais (Login, Nota, Id) VALUES (%s, %s, %s)'

        with connect(credentials) as connection:
            with connection.cursor(cursor_factory=extras.DictCursor) as cur:
                try:
                    lst = []
                    result = []
                    for v in values:
                        try:
                            item = tuple([v[0], v[2]])
                            if item not in lst:
                                lst.append(item)
                                result.append(tuple([v[0], v[1], v[2]]))
                        except Exception as e:
                            print(e)
                            continue

                    cur.executemany(query, lst)
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

        with connect(credentials) as connection:
            with connection.cursor(cursor_factory=extras.DictCursor) as cur:
                try:  # adding artistasmusicais Ids
                    lst = []
                    for v in values:
                        item = tuple([v[2]])
                        if item not in lst:
                            lst.append(item)

                    cur.executemany(
                        'INSERT INTO filme (Id) VALUES (%s)', lst)
                except Exception as e:
                    print(e)

        query = 'INSERT INTO UsuarioAvaliaFilme (Login, Nota, Id) VALUES (%s, %s, %s)'

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

            try:
                values.append(tuple([login[1], colleague[1]]))
            except Exception as e:
                print(e)
                continue

        query = 'INSERT INTO UsuarioRegistraConhecidoUsuario (Login, Login_registrado) VALUES (%s, %s)'

        with connect(credentials) as connection:
            with connection.cursor(cursor_factory=extras.DictCursor) as cur:
                try:
                    cur.executemany(query, values)
                except Exception as e:
                    print(e)

    except Exception as e:
        print(e)
