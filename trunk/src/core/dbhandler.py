# -*- coding: utf-8 -*-
'''
@author: 10873 Jorge Coveiro
@author: 12794 Carlos Rosário 
@last updated: 15-11-2012
@obs: CLASSE PARA ESCRITA E LEITURA NA BASE DE DADOS
'''

import csv
import sqlite3
from xlshandler import XlsHandler

class DbHandler:
	'''
	Trata de todas as operações envolvendo
	a base de dados
	'''
	def __init__(self, db):
		self.ESTABELECIMENTO = 0
		self.UNIDADE_ORGANICA = 1
		self.NIVEL_FORMACAO = 2
		self.CURSO = 3
		self.HOMENS = 5
		self.MULHERES = 6
		self.HOMENS_MULHERES = 7
		self.table_name = ''
		self.db=db
		self.anos = ["9596","9697","9798","9899","9900","0001","0102","0203","0304","0405","0506","0607","0708","0809","0910","1011"]
		self.totalH = [0 for i in range(16)]
		self.totalM = [0 for i in range(16)]
		self.totalHM = [0 for i in range(16)]
		

		self.conn=sqlite3.connect(self.db)
		pass
	
	def createTable(self, table_name):
		'''
		Cria uma tabela chamada table_name com os campos do ficheiro xls
		'''
		self.table_name = table_name
		cursor=self.conn.cursor()
		criatabela='''CREATE TABLE ''' + self.table_name + "(estabelecimento text, unidade_organica text, nivel_formacao text, curso text, "
		
		for ano in self.anos:
			'''
			Escreve os argumentos da tabela 
			"homens0001 number, mulheres0001 number, homens_mulheres0001 number"
			....até 1011
			'''
			if ano=="1011":
				criatabela += "homens" + ano + " number, mulheres" + ano + " number, homens_mulheres" + ano + ''' number)'''
			else:
				criatabela += "homens" + ano + " number, mulheres" + ano + " number, homens_mulheres" + ano + " number, "
			
		cursor.execute(criatabela)
		self.conn.commit()
		cursor.close()
			
	def writeToTable(self, xls_f):
		'''
		Insere valores do ficheiro xls nos campos da tabela
		'''
		cursor=self.conn.cursor()
		xls = XlsHandler(xls_f)
		rows = xls.readRows()
		tmp = ''
		for row in rows:
			'''
			Faz uma insercao dos valores de cada linha do ficheiro xls 
			para a base de dados
			'''
			homens=self.HOMENS
			mulheres=self.MULHERES
			homens_mulheres=self.HOMENS_MULHERES
			fim_linha=len(row)
			
			'''
			Insere os estabelecimentos e as
			unidades organicas em todas as linhas
			da base de dados
			'''			
			if row[self.ESTABELECIMENTO]=='':
				row[self.ESTABELECIMENTO]=e
			else:
				e=row[self.ESTABELECIMENTO]
			'''
			tmp == e (serve para imprimir as unidades organicas relativas
			a um estabelecimento "e"), porque há estabelecimentos sem unidade orgânica
			'''
			if (row[self.UNIDADE_ORGANICA] == '') & (tmp == e):
				row[self.UNIDADE_ORGANICA]=uo
			else:
				uo=row[self.UNIDADE_ORGANICA]
			tmp=e
			if (row[self.NIVEL_FORMACAO] == ''):
				row[self.NIVEL_FORMACAO] = nf
			else:
				nf = row[self.NIVEL_FORMACAO]
			instruction='''INSERT INTO ''' + self.table_name + " VALUES(\"" + str(row[self.ESTABELECIMENTO]) + "\", \"" + str(row[self.UNIDADE_ORGANICA]) + "\", \"" + str(row[self.NIVEL_FORMACAO]) + "\", \"" + str(row[self.CURSO]) + "\", "
			
			while(homens_mulheres < fim_linha):
				'''
				Percorre as colunas  do ficheiro xls. Se o valor for "-"
				é trocado por '', e concatena os valores à string instruction
				'''
				if row[homens]=='-':
					row[homens]=0
				if row[mulheres]=='-':
					row[mulheres]=0
				if row[homens_mulheres]=='-':
					row[homens_mulheres]=0
				
				
				instruction += str(row[homens]) + ", " + str(row[mulheres]) + ", " + str(row[homens_mulheres])
				
				if homens_mulheres == fim_linha-1:
					'''
					Se chegámos ao fim da linha do ficheiro xls
					então concatenamos à string instruction ")"
					para fecharmos a instrução.
					Se não continuamos a concatenar valores separados por ","
					'''
					instruction += ''')'''
					homens_mulheres+=homens+2
				else:
					instruction += ", "
					if row[homens_mulheres+1]=='':
						'''
						Aqui alteramos os indices
						Nota: Há uma coluna vazia no ficheiro xls por isso
						vamos ter de adicionar 2 em vez de 1 ao indice homens
						'''
						homens=homens_mulheres+2
						mulheres=homens+1
						homens_mulheres=mulheres+1
						pass
					else:
						homens=homens_mulheres+1
						mulheres=homens+1
						homens_mulheres=mulheres+1
		
			'''
			Finalmente executamos a instrucao por cada linha do xls
			'''
			cursor.execute(instruction)
			pass
		self.conn.commit()
		cursor.close()
		pass
	
	def dbToCsv(self, col_name, args):
		'''
		Escreve os dados args da coluna col_name num
		ficheiro .csv 
		'''
		cursor = self.conn.cursor()
		cursor2 = self.conn.cursor()
		csv_writer = csv.writer(open("results/estatisticas.csv", "w"))
		nome_colunas_topo = ["Estabelecimento", "Unidade Orgânica", "Nivel de Formação", "Curso"]
		nome_colunas_total = ['', '', '', '']
		nome_colunas_nf = ["Nível de Formação", '', '', '', "Número de Cursos"] 
		nome_colunas_inscritos_nf = ["Nível de Formação", '', '', ''] 
		
		#Ciclo que completa o array com os titulos das colunas das diferentes
		#secções do ficheiro csv
		for i in range(len(self.anos)):
			#Acrescenta o ano lectivo ao nome das tabelas no inicio do ficheiro
			nome_colunas_topo += ["Homens " + str(self.anos[i])]
			nome_colunas_topo += ["Mulheres " + str(self.anos[i])]
			nome_colunas_topo += ["Homens e Mulheres " + str(self.anos[i])]
			
			#Acrescenta o ano lectivo a nome_colunas_total para
			#apresentar por cima dos totais dos alunos inscritos ao longo
			#desses anos lectivos
			nome_colunas_total += ["Homens " + str(self.anos[i])]
			nome_colunas_total += ["Mulheres " + str(self.anos[i])]
			nome_colunas_total += ["Homens e Mulheres " + str(self.anos[i])]
			
			nome_colunas_inscritos_nf += ["Homens " + str(self.anos[i])]
			nome_colunas_inscritos_nf += ["Mulheres " + str(self.anos[i])] 
			nome_colunas_inscritos_nf += ["Homens e Mulheres " + str(self.anos[i])]
		
		csv_writer.writerow(nome_colunas_topo)
		#Procura na tabela table_name todos os resultados que
		#tenham table_name igual a args[0] e args[1], e escreve
		#os resultados no ficheiro estatisticas.csv
		cursor.execute("SELECT * FROM " + self.table_name + " WHERE " + col_name + " LIKE " + "'%" + args[0] + "%'" + " OR " + col_name + " LIKE " + "'%" + args[1] + "%'")
		for el in cursor:
			csv_writer.writerow([s.encode("utf-8") if isinstance(s,unicode) else s for s in el])
		csv_writer.writerow([])
		
		csv_writer.writerow(nome_colunas_total)
		
		#a_escrever vai conter a soma de todos os alunos(homens, mulheres, e ambos) 
		#em cada ano lectivo dos cursos seleccionados na linha "157"
		a_escrever = ['Total','','','']
		coluna = ['homens', 'mulheres', 'homens_mulheres']
		for ano in self.anos:
			for i in range (3):
				cursor.execute("SELECT SUM(" + coluna[i] + str(ano) + ") FROM " + self.table_name + " WHERE " + col_name + " LIKE '%" + args[0] + "%' OR " + col_name + " LIKE '%" + args[1] + "%'")	
				a_escrever.append(cursor.fetchone()[0])
		csv_writer.writerow(a_escrever)
		csv_writer.writerow([])
		
		csv_writer.writerow(nome_colunas_nf)
		#Escreve a quantidade de cursos por nível de formação
		cursor.execute("SELECT DISTINCT nivel_formacao FROM " + self.table_name + " WHERE " + col_name + " LIKE '%" + args[0] + "%' OR " + col_name + " LIKE '%" + args[1] + "%'")
		for nivel_formacao in cursor:
			a_escrever = [s.encode("utf-8") if isinstance(s, unicode) else s for s in nivel_formacao]
			a_escrever += ['','','']
				
			#cursor2 contem o numero de cursos por nivel de formacao == nivel_formacao 
			cursor2.execute("SELECT count(*) FROM " + self.table_name + " WHERE (nivel_formacao == '" + nivel_formacao[0].encode("utf-8") + "') AND ((curso LIKE '%" + args[0] + "%') OR (curso LIKE '%" + args[1] + "%'))")
			tmp = cursor2.fetchone()[0]
			a_escrever.append(tmp)
			csv_writer.writerow(a_escrever)	
		csv_writer.writerow([])
			
		csv_writer.writerow(nome_colunas_inscritos_nf)
		#Escreve a quantidade de alunos por nível de formação ao longo dos anos
		cursor.execute("SELECT DISTINCT nivel_formacao FROM " + self.table_name + " WHERE " + col_name + " LIKE '%" + args[0] + "%' OR " + col_name + " LIKE '%" + args[1] + "%'")
		for nivel_formacao in cursor:
			a_escrever = [s.encode("utf-8") if isinstance(s, unicode) else s for s in nivel_formacao]	
			for n in range (3):
				a_escrever.append('')
		
			for ano in self.anos:
				for i in range(3):
					cursor2.execute("SELECT SUM(" + coluna[i] + ano + ") FROM " + self.table_name + " WHERE (nivel_formacao == '" + nivel_formacao[0].encode("utf-8") + "') AND ((" + col_name + " LIKE '%" + args[0] + "%') OR (" + col_name + " LIKE '%" + args[1] + "%'))")
					a_escrever.append(cursor2.fetchone()[0])
			csv_writer.writerow(a_escrever)

		del csv_writer
