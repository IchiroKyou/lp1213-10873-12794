# -*- coding: utf-8 -*-
'''
@author: 10873 Jorge Coveiro
@author: 12794 Carlos Rosário 
@date: 05-11-2012
@obs: DATABASE HANDLER
'''

import csv
import sqlite3

class DbHandler:
	'''
	Insere dados de csv para db
	'''
	def __init__(self, db):
		self.ESTABELECIMENTO = 0
		self.CURSO = 3
		self.HOMENS = 5
		self.MULHERES = 6
		self.HOMENS_MULHERES = 7

		self.conn=sqlite3.connect(db)
		pass
	
	def createTable(self, table_name):
		'''
		Cria uma tabela chamada table_name com os campos do ficheiro csv
		'''
		cursor=self.conn.cursor()
		criatabela='''CREATE TABLE ''' + table_name + "(estabelecimento text, curso text, "
		anos=["9596","9697","9798","9899","9900","0001","0102","0203","0304","0405","0506","0607","0708","0809","0910","1011"]
		
		for ano in anos:
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
			
	def writeToTable(self, table_name, csv_f):
		'''
		Insere valores do ficheiro csv nos campos da tabela
		'''
		cursor=self.conn.cursor()
		f=open(csv_f,'r')
		csv_r=csv.reader(f)

		for row in csv_r:
			'''
			Faz uma insercao dos valores de cada linha do ficheiro csv 
			para a base de dados
			'''
			homens=self.HOMENS
			mulheres=self.MULHERES
			homens_mulheres=self.HOMENS_MULHERES
			fim_linha=len(row)
			
			if row[self.ESTABELECIMENTO]=='':
				row[self.ESTABELECIMENTO]=b
			else:
				b=row[self.ESTABELECIMENTO]
				
			instruction='''INSERT INTO ''' + table_name + " VALUES(\"" + str(row[self.ESTABELECIMENTO]) + "\", \""+str(row[self.CURSO]) + "\", "
			
			while(homens_mulheres < fim_linha):
				'''
				Percorre as colunas  do ficheiro csv. Se o valor for "-"
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
					Se chegámos ao fim da linha do ficheiro csv
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
			Finalmente executamos a instrucao por cada linha do csv
			'''
			cursor.execute(instruction)
			pass
		
		self.conn.commit()
		cursor.close()
		f.close()
		pass
