# -*- coding: utf-8 -*-
'''
@author: 10873 Jorge Coveiro
@author: 12794 Carlos Rosário 
@date: 05-11-2012
@obs: PROGRAMA PARA A ANALISE DE DADOS DE UM .XLS
'''

from xlstocsv import XlsHandler
from dbhandler import DbHandler


xlsconv=XlsHandler("Inscritos_2010-2011.xls","Inscritos.csv")

csvdb=DbHandler("Inscritos.sqlite3")
csvdb.createTable("inscritos")
csvdb.writeToTable("inscritos", "Inscritos.csv")
