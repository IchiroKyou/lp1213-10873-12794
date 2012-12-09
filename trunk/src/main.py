# -*- coding: utf-8 -*-
'''
@author: 10873 Jorge Coveiro
@author: 12794 Carlos Rosário
@last updated: 08-12-2012
@obs: PROGRAMA PARA A ANALISE DE DADOS DE UM .XLS
'''
import sys
sys.path.append('core')
sys.path.append('dataplot')
sys.path.append('gui')
from dbhandler import DbHandler
from curso import Curso
from PlotGUI import *
import random


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
"""
def imprime(texto):
	texto = texto.toUtf8()
	print texto
"""
class GUIForm(QtGui.QDialog):

    def __init__(self, cursos, niveis_formacao, parent=None):
        self.cursos = cursos
        self.niveis_formacao = niveis_formacao
		
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self, cursos, niveis_formacao)
   
        #Envia o texto do item da comboBox seleccionado
        self.ui.graph_comboBox.activated[int].connect(self.PlotFunc)    

    def PlotFunc(self, val):
        if ((val < len(self.cursos) + 2) & (val > 1)): #2 sao os dois primeiros items da comboBox
            self.ui.widget.canvas.ax1.clear()
            self.ui.widget.canvas.ax2.clear()
            self.ui.widget.canvas.ax3.clear()
            
            self.ui.widget.canvas.ax1.set_ylabel(u'Número de inscritos')
            self.ui.widget.canvas.ax1.set_title(u'Número de inscritos/ano lectivo')
            self.ui.widget.canvas.ax1.plot(cursos[val-2].totalH)
            self.ui.widget.canvas.ax2.plot(cursos[val-2].totalM)
            self.ui.widget.canvas.ax3.plot(cursos[val-2].totalHM)
            self.ui.widget.canvas.ax1.legend('HMT')
            self.ui.widget.canvas.ax1.set_xticklabels( ('9596', '9798', '9900',
                                                        '0102', '0304', '0506',
		                                                '0708', '0910', '1112') )

        elif(val > len(self.cursos) + 2):
            self.ui.widget.canvas.ax1.clear()
            self.ui.widget.canvas.ax2.clear()
            self.ui.widget.canvas.ax3.clear()
            
            self.ui.widget.canvas.ax1.set_ylabel(u'Número de inscritos')
            self.ui.widget.canvas.ax1.set_title(u'Número de inscritos/ano lectivo')
            self.ui.widget.canvas.ax1.plot(niveis_formacao[val-len(self.cursos)-3].totalH)
            self.ui.widget.canvas.ax2.plot(niveis_formacao[val-len(self.cursos)-3].totalM)
            self.ui.widget.canvas.ax3.plot(niveis_formacao[val-len(self.cursos)-3].totalHM)
            self.ui.widget.canvas.ax1.legend('HMT')
            self.ui.widget.canvas.ax1.set_xticklabels( ('9596', '9798', '9900',
                                                        '0102', '0304', '0506',
		                                                '0708', '0910', '1112') )

        self.ui.widget.canvas.draw()
        

if __name__ == "__main__":
    db = DbHandler("database/Inscritos.sqlite3")
    db.createTable("inscritos")
    db.writeToTable("Inscritos_2010-2011.xls")
    db.dbToCsv("curso",["Computadores","Informática"])

    cursos = db.getInscritosCurso("curso", ["Computadores","Informática"])
    niveis_formacao = db.getInscritosNF()

    db.closeConnection()

    #Parte gráfica do programa
    app = QtGui.QApplication(sys.argv)
    myapp = GUIForm(cursos, niveis_formacao)
    myapp.show()
    sys.exit(app.exec_())
