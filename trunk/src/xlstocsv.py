#-*- coding: utf-8 -*-
'''
@author: 10873 Jorge Coveiro
@author: 12794 Carlos Rosário 
@date: 05-11-2012
@obs: PROGRAMA PARA A CONVERSAO DE UM .XLS PARA .CSV
'''

import xlrd
import csv
from csvunicode import UnicodeWriter
"""
from xlutils.copy import copy
import commands
"""

class XlsHandler:
	'''
	Escreve linhas relevantes de um ficheiro xls num ficheiro csv especificado
	'''
	def __init__(self, xls_f, csv_file, starting_xls_row = 4, sheet_number = 30, irrelevant_nr_rows = 9):
		self.starting_xls_row=starting_xls_row
		self.sheet_number=sheet_number
		self.irelevant_rows=irrelevant_nr_rows
		self.book=xlrd.open_workbook(xls_f)
		self.sheet=self.book.sheet_by_index(self.sheet_number)
		self.csv_f=open(csv_file, "w")
		self.u_csv_w=UnicodeWriter(self.csv_f)
		self.writeRows()
		pass
		
	def writeRows(self):
		'''
		Escreve linhas do ficheiro xls no ficheiro csv
		'''
		for rown in range(self.starting_xls_row, self.sheet.nrows - self.irelevant_rows):
			self.u_csv_w.writerow(self.sheet.row_values(rown))
			pass
		self.csv_f.close()
	"""
	def writeRows2(self):
		'''
		Converte ficheiro xls para csv e apaga as paginas nao necessarias
		'''
		commands.getstatusoutput('ssconvert Inscritos_2010-2011.xls Inscritos.csv -S')
		commands.getstatusoutput('mv Inscritos.csv.30 Inscritos.csv')
		commands.getstatusoutput('rm Inscritos.csv.*')
		pass
	"""
