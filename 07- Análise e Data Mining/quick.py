#!/usr/bin/env python3
from psycopg2 import extras, connect
import pandas.io.sql as psql

def create_transaction(credentials, query):
    try:
        with connect(credentials) as connection:
            print(psql.read_sql(query, connection))
    except Exception as e:
        raise(e)

if __name__ == "__main__":
    credentials = "dbname='1901EquipePGDR' user='1901EquipePGDR' host='200.134.10.32' password='793953'"

    q = [
        '''SELECT id, AVG(Nota), stddev(Nota)
    FROM   UsuarioAvaliaFilme
    GROUP BY id;''',
    '''
    SELECT id, AVG(Nota), stddev(Nota)
    FROM   UsuarioAvaliaArtistasMusicais
    GROUP BY id;
    ''',
    '''SELECT id, avg, Popularidade
    FROM UsuarioAvaliaArtistasMusicais u
    NATURAL JOIN RatingArtistasMusicais r
    NATURAL JOIN AvAM
    WHERE Popularidade > 1
    ORDER BY r.avg DESC;
    ''',
    '''SELECT id, avg, Popularidade
	FROM UsuarioAvaliaFilme u
	NATURAL JOIN RatingFilme r
	NATURAL JOIN AvF
	WHERE Popularidade > 1
	ORDER BY r.avg DESC;''',
    '''SELECT id, Popularidade
	FROM UsuarioAvaliaFilme u
	NATURAL JOIN RatingFilme r
	NATURAL JOIN AvF
    group by id, popularidade
	ORDER BY Popularidade DESC
	LIMIT 10;''',
    '''SELECT id, Popularidade
	FROM UsuarioAvaliaArtistasMusicais u
	NATURAL JOIN RatingArtistasMusicais r
	NATURAL JOIN AvAM
    group by id, popularidade
	ORDER BY Popularidade DESC
	LIMIT 10;''',
    '''select login, login_registrado, soma
	from DuplasSomadas
	where soma = (select max(soma) from Somados);''',
    '''select login_registrado, count(login_registrado) 
from conhecenormalizada natural join Gustavo 
group by login_registrado

union

select login_registrado, count(login_registrado) 
from conhecenormalizada natural join Rodrigo 
group by login_registrado

union

select login_registrado, count(login_registrado) 
from conhecenormalizada natural join pedro 
group by login_registrado

union

select login_registrado, count(login_registrado) 
from conhecenormalizada natural join daniel 
group by login_registrado''',
'''select popularidade NoPessoas, count(popularidade) NoFilmes 
from avf 
group by popularidade 
order by popularidade
''',
'''select conta NoFilmes, count(conta) NoPessoas 
from curtefilme 
group by conta 
order by conta'''

    ]

    for i, query in enumerate(q):
        try:
            print('\nCONSULTA %i\n\n' % i)
            create_transaction(credentials, query)
        except Exception as e:
            print(e)
