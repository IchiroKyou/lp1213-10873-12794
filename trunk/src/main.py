# -*- coding: utf-8 -*-
'''
@author: 10873 Jorge Coveiro
@author: 12794 Carlos Rosário
@last updated: 03-12-2012
@obs: PROGRAMA PARA A ANALISE DE DADOS DE UM .XLS
'''
import sys
from PyQt4 import QtCore, QtGui
sys.path.append('core')
sys.path.append('dataplot')
sys.path.append('gui')
from myui import *
from matplot_bars import *
from dbhandler import DbHandler
from curso import Curso

db = DbHandler("database/Inscritos.sqlite3")
db.createTable("inscritos")
db.writeToTable("Inscritos_2010-2011.xls")
db.dbToCsv("curso",["Computadores","Informática"])

cursos = db.getInscritosCurso("curso", ["Computadores","Informática"])
niveis_formacao = db.getInscritosNF()

db.closeConnection()

app = QtGui.QApplication(sys.argv)
MainWindow = QtGui.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())


