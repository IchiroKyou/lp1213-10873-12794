#-*- coding: utf-8 -*-
'''
@author: 10873 Jorge Coveiro
@author: 12794 Carlos Rosário 
@last updated: 15-11-2012
@obs: CLASSE PARA A LEITURA DE UM FICHEIRO .XLS
'''
import xlrd

class XlsHandler:
	'''
	Trata das operações com
	ficheiros xls
	'''
	def __init__(self, xls_f, starting_xls_row = 4, sheet_number = 30, irrelevant_nr_rows = 9):
		self.starting_xls_row=starting_xls_row
		self.sheet_number=sheet_number
		self.irelevant_rows=irrelevant_nr_rows
		self.book=xlrd.open_workbook(xls_f)
		self.sheet=self.book.sheet_by_index(self.sheet_number)
		self.rows=[]
		self.readRows()
		pass
		
	def readRows(self):
		'''
		Devolve um alista rows com as
		linhas relevantes do ficheiro xls
		'''
		for rown in range(self.starting_xls_row, self.sheet.nrows - self.irelevant_rows):
			self.rows.append([s.encode("utf-8") if isinstance(s,unicode) else s for s in self.sheet.row_values(rown)])
			pass
		return self.rows
