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
				exit_create = False

				with connect(credentials) as connection:
					with connection.cursor(cursor_factory=extras.DictCursor) as cur:
						try:
							while not exit_create:

								print('###\tList users - (return: CTRL + C)\n')

								try:
									query = 'SELECT * FROM Usuario'

									cur.execute(query)
									for pessoa in cur.fetchall():
										print('Login: '+pessoa[0])
										print('Nome: '+pessoa[1])
										print('Ciade natal: '+pessoa[2])
										print('#'*10)
									
									op_ = int(input('###\tDefina a operação (exit: CTRL + C):\n\t3 - Editar\n\t4 - Excluir\n'))
									if(op_ == 3):
										id_usuario = input('###\t Qual o Login do usuario que deseja editar?\t(exit: CTRL + C)\n')
										system('clear')
										try:
											query = 'SELECT * FROM Usuario WHERE Login = '+"'"+id_usuario+"'"
											
											cur.execute(query)
											for pessoa in cur.fetchall():
												print('Login: '+pessoa[0])
												print('Nome: '+pessoa[1])
												print('Cidade natal: '+pessoa[2])

										except Exception as e:
												print(e)

										op_interna = int(input('###\tDefina o campo a ser editado (exit: CTRL + C):\n\t1 - Nome\n\t2 - Cidade Natal\n'))
										if(op_interna == 1):
											nome_edit = input('Digite o novo nome\n')
											query = 'UPDATE Usuario SET Nome = '+"'"+nome_edit+"'"+' WHERE Usuario.Login = '+"'"+id_usuario+"'"
											try:
												cur.execute(query)
												system('clear')
												print('Nome alterado com sucesso\n')
											except Exception as e:
												print(e)

										elif(op_interna == 2):
											city_edit = input('Digite a nova Cidade Natal\n')
											query = 'UPDATE Usuario SET Cidade_natal = '+"'"+city_edit+"'"+' WHERE Usuario.Login = '+"'"+id_usuario+"'"
											try:
												cur.execute(query)
												system('clear')
												print('Cidade Natal alterada com sucesso\n')
											except Exception as e:
												print(e)

									elif(op_ == 4):
										id_usuario = input('###\t Qual o Login do usuario que deseja excluir?\n')

										try:
											query = 'DELETE FROM Usuario WHERE Login = '+"'"+id_usuario+"'"
											certeza_exclusao = input('###\t Tem certeza que deseja excluir o Usuario '+id_usuario+' (y/n)?\n')
											if(certeza_exclusao == 'y'):
												cur.execute(query)
												system('clear')
												print('Usuario excluido com sucesso!\n')
											else:
												print('Operação cancelada!\n')

										except Exception as e:
												print(e)
									
									next_op = input('###\t Deseja realizar mais alguma edição ou exclusão? (y/n)\n')
									if(next_op == 'y'):
										continue
									else:
										exit_create = True
										system('clear')
									
								except KeyboardInterrupt as e:
									exit_create = True
									system('clear')

								system('clear')
						except Exception as e:
							print(e)
							if input('Do you want to retry or leave? (r/l)\t') in 'Rr':
								exit_create = True
							system('clear')
		except KeyboardInterrupt as e:
			print('\rGood-bye!\n')
			exit = True