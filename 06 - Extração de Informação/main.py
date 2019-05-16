#!/usr/bin/env python3

from psycopg2 import extras, connect
from os import system
from bs4 import BeautifulSoup
import requests, xml.etree.cElementTree as ET
import urllib.request, json, wikipedia


if __name__ == "__main__":

	credentials = "dbname='1901EquipePGDR' user='1901EquipePGDR' host='200.134.10.32' password='793953'"

	with connect(credentials) as connection:
		with connection.cursor(cursor_factory=extras.DictCursor) as cur:
			# HEADER PARA PESQUISA EM INGLES
			headers = {"Accept-Language": "en-US, en;q=0.5"}
						
			query_artistas = 'SELECT * FROM ArtistasMusicais'
			cur.execute(query_artistas)
			# ORGANIZANDO ARTISTAS EM LISTA
			lista_artistas = []
			for artista_musical in cur.fetchall():
				if(artista_musical[0].isdigit()):
					continue
				lista_artistas.append(artista_musical[0])
			counter = 1
			total = len(lista_artistas)
			# CRIANDO XML E ITERANDO ARTISTAS
			xml_art = ET.Element("ArtistasMusicais")
			for nome_artista in lista_artistas:
				print('REALIZANDO BUSCA '+str(counter)+'/'+str(total)+' (ARTISTA): ' + nome_artista)

				url = requests.get("https://en.wikipedia.org/wiki/"+nome_artista,headers=headers)
				data = url.text

				soup = BeautifulSoup(data,"lxml")
				info_box_wiki = soup.findAll("table", {"class": "infobox"})
				
				if len(info_box_wiki) < 1:
					continue
				# NOME ARTISTA/GRUPO
				nome_banda = info_box_wiki[0].find("th").find(text=True)
				

				itunes_link = ''
				url_alt = "https://itunes.apple.com/search?term="+nome_banda.replace(' ','+')+"&entity=musicArtist"
				try:
					with urllib.request.urlopen(url_alt) as asd:
						data = json.loads(asd.read().decode())
						itunes_link = data['results'][0]['artistLinkUrl']
				except:
					itunes_link = ''

				
				origem = ''
				generos = ''

				for text in info_box_wiki[0].findAll("tr"):
					if len(text.findAll("td")) < 1:
						continue
					# CIDADE/PAIS DE ORIGEM
					if 'Origin' in str(text):
						cell_origin = text.findAll("td")
							
						for cell in cell_origin[0].contents:
							try:
								origem += cell.find(text=True)
							except:
								origem += cell
					# GENEROS MUSICAIS
					if 'Genres' in str(text):
						cell_genres = text.findAll("td")
						for cell in cell_genres[0].findAll("a"):
							if '[' and ']' in str(cell):
								continue
							try:
								generos += cell.find(text=True)+','
							except:
								generos += cell+','
						generos = generos[:-1]
				
				system('clear')
				counter+=1

				ET.SubElement(xml_art, "Artista", uri=nome_artista,nome=nome_banda,
							origem=origem,generos=generos,link_itunes=itunes_link)

			tree = ET.ElementTree(xml_art)
			tree.write("music.xml")
			# FIM MUSICAS
			# INICIO FILMES
			
			query_filmes = 'SELECT * FROM Filme'			
			cur.execute(query_filmes)
			# ORGANIZANDO FILMES EM LISTA
			lista_filmes = []
			for filme in cur.fetchall():
				if(filme[0].isdigit()):
					continue
				lista_filmes.append(filme[0])
			# CRIANDO XML E ITERANDO FILMES
			xml_mov = ET.Element("Filmes")
			counter = 1
			total = len(lista_filmes)
			for id_filme in lista_filmes:
				print('REALIZANDO BUSCA '+str(counter)+'/'+str(total)+' (FILME): ' + id_filme)
				# REQUEST IMDB
				url = requests.get('https://www.imdb.com/title/'+id_filme,headers=headers)				
				data = url.text
				soup = BeautifulSoup(data,"lxml")

				info_imdb = soup.findAll("div", {"class": "title_wrapper"})
				
				# NOME DO FILME
				nome = info_imdb[0].findAll("h1")
				nome = nome[0].find(text=True)
				####################################
				try:
					wiki_page = wikipedia.search(nome)[0]
					resumo_filme = wikipedia.page(title=wiki_page).summary
					resumo_filme = resumo_filme.replace('\n',' ')
				except:
					resumo_filme = ''
				####################################

				# GENEROS E LANCAMENTO
				gen_lan = info_imdb[0].findAll("a")
				lista_generos = []

				for link in gen_lan:
					if "genres" in str(link):
						lista_generos.append(link.find(text=True))
					elif 'releaseinfo' in str(link):
						data_lancamento = link.find(text=True)

				# DIRETOR(ES)
				info_diretor = soup.findAll("div", {"class": "credit_summary_item"})
				link_diretor = info_diretor[0].findAll("a")
				lista_diretores = []
				for link in link_diretor:
					if "name" in str(link):
						lista_diretores.append(link.find(text=True))
				
				genero = ''
				for x in lista_generos:
					genero = x+','
				genero = genero[:-1]

				diretor = ''
				for x in lista_diretores:
					diretor = x+','
				diretor = diretor[:-1]

				data_lancamento = data_lancamento.replace('(Brazil)','')
				system('clear')
				counter+=1
				ET.SubElement(xml_mov, "Filme", uri=id_filme,nome=nome,resumo=resumo_filme,
							diretor=diretor,generos=genero,data_lancamento=data_lancamento)

			tree = ET.ElementTree(xml_mov)
			tree.write("movie.xml")

			
				
				
