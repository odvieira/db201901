#!/usr/bin/python3

from psycopg2 import connect
from os import system

def execute_query(parameter_list):
    return 0

def menu():

    if opt == 0:

        return 1

    credentials = \
        "dbname='1901EquipePGDR' user='1901EquipePGDR' host='200.134.10.32' password='793953'"
    with connect(credentials) as connection:
                with connection.cursor() as cur:
                    cur.execute(query)
    
    return 0

if __name__ == "__main__":
    exit = 0
    while 0 == exit:    
        exit = menu()

    return