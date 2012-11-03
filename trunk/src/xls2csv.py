 #-*- coding: utf-8 -*-
'''
@author1: Jorge Coveiro, n10873
@author2: Carlos Rosario, n12794
@date 31-10-2012
@obs: CONVERSAO DE UM .XLS PARA .CSV
'''
import csv
import xlrd
from xlrd import open_workbook
from xlutils.copy import copy
import commands

def processarXLS1():
	'''
	Conversao normal através da linha de comandos
	'''
	commands.getstatusoutput('ssconvert Inscritos_2010-2011.xls Inscritos.csv -S')
	commands.getstatusoutput('rm Inscritos.csv.0')
	commands.getstatusoutput('rm Inscritos.csv.1')
	commands.getstatusoutput('rm Inscritos.csv.2')
	commands.getstatusoutput('rm Inscritos.csv.3')
	commands.getstatusoutput('rm Inscritos.csv.4')
	commands.getstatusoutput('rm Inscritos.csv.5')
	commands.getstatusoutput('rm Inscritos.csv.6')
	commands.getstatusoutput('rm Inscritos.csv.7')
	commands.getstatusoutput('rm Inscritos.csv.8')
	commands.getstatusoutput('rm Inscritos.csv.9')
	commands.getstatusoutput('rm Inscritos.csv.10')
	commands.getstatusoutput('rm Inscritos.csv.11')
	commands.getstatusoutput('rm Inscritos.csv.12')
	commands.getstatusoutput('rm Inscritos.csv.13')
	commands.getstatusoutput('rm Inscritos.csv.14')
	commands.getstatusoutput('rm Inscritos.csv.15')
	commands.getstatusoutput('rm Inscritos.csv.16')
	commands.getstatusoutput('rm Inscritos.csv.17')
	commands.getstatusoutput('rm Inscritos.csv.18')
	commands.getstatusoutput('rm Inscritos.csv.19')
	commands.getstatusoutput('rm Inscritos.csv.20')
	commands.getstatusoutput('rm Inscritos.csv.21')
	commands.getstatusoutput('rm Inscritos.csv.22')
	commands.getstatusoutput('rm Inscritos.csv.23')
	commands.getstatusoutput('rm Inscritos.csv.24')
	commands.getstatusoutput('rm Inscritos.csv.25')
	commands.getstatusoutput('rm Inscritos.csv.26')
	commands.getstatusoutput('rm Inscritos.csv.27')
	commands.getstatusoutput('rm Inscritos.csv.28')
	commands.getstatusoutput('rm Inscritos.csv.29')
	commands.getstatusoutput('rm Inscritos.csv.31')
	commands.getstatusoutput('rm Inscritos.csv.32')
	commands.getstatusoutput('mv Inscritos.csv.30 Inscritos.csv')

def processarXLS2():
	'''
	Conversao alternativa através de python-excel
	'''
    	rb = open_workbook('Inscritos_2010-2011.xls')
    	rs = rb.sheet_by_index(30)
    	wb = copy(rb)
    	wb.save('output.xls')