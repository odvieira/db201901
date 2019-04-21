#!/usr/bin/env python3
from psycopg2 import extras, connect
import pandas.io.sql as psql

def create_transaction(credentials):
    try:
        with connect(credentials) as connection:
            print(psql.read_sql(input(), connection))
    except Exception as e:
        raise(e)

if __name__ == "__main__":
    credentials = "dbname='1901EquipePGDR' user='1901EquipePGDR' host='200.134.10.32' password='793953'"

    exit = False

    while not exit:
        print('\n############\nInsert a query below [ Ctrl+C to exit ]')
        try:
            create_transaction(credentials)
        except KeyboardInterrupt as e:
            print('\nGood-Bye!')
            exit = True
        except Exception as e:
            print(e)
