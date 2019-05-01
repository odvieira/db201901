#!/usr/bin/env python3
from psycopg2 import extras, connect
import pandas.io.sql as psql
import matplotlib.pyplot as plt

def create_transaction(credentials, query):
    try:
        with connect(credentials) as connection:
            return psql.read_sql(query, connection)
            
    except Exception as e:
        raise(e)

if __name__ == "__main__":
    credentials = "dbname='1901EquipePGDR' user='1901EquipePGDR' host='200.134.10.32' password='793953'"

    q = [
        'select conta NoFilmes, count(conta) NoPessoas from curtefilme group by conta order by conta',
        'select popularidade NoPessoas, count(popularidade) NoFilmes from avf group by popularidade order by popularidade'
    ]

    try:
        tableFilme = (create_transaction(credentials, q[0]))
        print(tableFilme)

        x = []
        y = []

        for t in tableFilme.itertuples(index=False):
            x.append(t[0])
            y.append(t[1])

        plt.plot(x, y)
        plt.xlabel('No. de Filmes')
        plt.ylabel('No. de Pessoas')
        plt.show()
    except Exception as e:
        print(e)

    try:
        tableUsuario = (create_transaction(credentials, q[1]))
        print(tableUsuario)

        x = []
        y = []

        for t in tableUsuario.itertuples(index=False):
            x.append(t[0])
            y.append(t[1])

        plt.plot(x, y)
        plt.ylabel('No. de Filmes')
        plt.xlabel('No. de Pessoas')
        plt.show()
    except Exception as e:
        print(e)
