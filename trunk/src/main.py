# -*- coding: utf-8 -*-
'''
@author: 10873 Jorge Coveiro
@author: 12794 Carlos Rosário
@last updated: 15-11-2012
@obs: PROGRAMA PARA A ANALISE DE DADOS DE UM .XLS
'''
import sys
sys.path.append('core')
sys.path.append('dataplot')
sys.path.append('gui')
from matplot_bars import *
from dbhandler import DbHandler
from curso import Curso

db = DbHandler("database/Inscritos.sqlite3")
db.createTable("inscritos")
db.writeToTable("Inscritos_2010-2011.xls")
db.dbToCsv("curso",["Computadores","Informática"])
cursos = db.getInscritos("curso",["Computadores","Informática"])

desenhaGraphBars(cursos, 1)

db.closeConnection()

