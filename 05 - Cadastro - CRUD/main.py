#!/usr/bin/env python3

from psycopg2 import extras, connect
from os import system

if __name__ == "__main__":

    credentials = \
        "dbname='1901EquipePGDR' user='1901EquipePGDR' host='200.134.10.32' password='793953'"
    
    exit = False
    
    while not exit:
        try:
            op = int(input('###\tDefina a operação (exit: CTRL + C):\n\t1 - Create\n\t2 - Read\n'))
            system('clear')

            if op == 1:
                exit_create = False

                with connect(credentials) as connection:
                    with connection.cursor(cursor_factory=extras.DictCursor) as cur:
                        try:
                            while not exit_create:

                                print('###\tCreate users - (return: CTRL + C)\n')

                                try:
                                    login = input('Login:\t\t')
                                    name = input('Nome:\t\t')
                                    hometown = input('Cidade Natal:\t')

                                    query = \
                                        'INSERT INTO Usuario (Login, Nome, Cidade_natal) VALUES (%s, %s, %s)'                                

                                    if input(\
                                        'Confirm query (y/n)\t:\n\tINSERT INTO Usuario (Login, Nome, Cidade_natal) VALUES (%s, %s, %s)'\
                                            % (login, name, hometown)) in 'Yy':
                                        cur.execute(query, tuple([login, name, hometown]))
                                    
                                    input('\nDone!\n\nPRESS ENTER TO CREATE ANOTHER OR CTRL + C TO RETURN')
                                    
                                except KeyboardInterrupt as e:
                                    exit_create = True
                                    system('clear')

                                system('clear')
                        except Exception as e:
                            print(e)
                            if input('Do you want to retry or leave? (r/l)\t') in 'Rr':
                                exit_create = True
                            system('clear')
            elif op == 2:
                pass
        except KeyboardInterrupt as e:
            print('\rGood-bye!\n')
            exit = True