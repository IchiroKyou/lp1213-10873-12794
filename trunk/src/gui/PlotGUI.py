# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PlotGUI_Final.ui'
#
# Created: Sat Dec  8 16:04:04 2012
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!
'''
Funções que foram modificadas:
setupUi : + 2 argumentos (cursos e niveis_formacao)
		  + 2 ciclos para preenchimento da combo box
'''
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog, cursos, niveis_formacao):
        self.Dialog = Dialog
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(693, 545)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icon/estig.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.widget = matplotlibWidget(self.Dialog) #Widget que vai conter os gráficos
        self.widget.setGeometry(QtCore.QRect(9, 9, 671, 361))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.graph_comboBox = QtGui.QComboBox(Dialog)
        self.graph_comboBox.setGeometry(QtCore.QRect(50, 430, 591, 31))
        self.graph_comboBox.setObjectName(_fromUtf8("graph_comboBox"))
        self.graph_comboBox.addItem(_fromUtf8("")) # item_index == 0, "Escolha um gráfico"
        self.graph_comboBox.addItem(_fromUtf8("")) # item_index == 1, "- - Por curso - -"
        self.graph_comboBox.setItemText(1, _fromUtf8(" - - Por curso - -"))
        
        #Adiciona items à combo box, correspondentes aos cursos existentes
        #com Computadores ou Informática no nome
        item_index = 2;
        for curso in cursos:
            self.graph_comboBox.addItem(_fromUtf8(""))
            self.graph_comboBox.setItemText(item_index, _fromUtf8(curso.nome))
            item_index += 1
         
        #Adiciona items à combo box, correspondentes aos cursos existentes
        #com Computadores ou Informática no nome
        self.graph_comboBox.addItem(_fromUtf8("")) # item_index == item_index, "- - Por nivel de formação - -"
        self.graph_comboBox.setItemText(item_index, _fromUtf8(" - - Por nivel de formação - -"))
        for nf in niveis_formacao:
            item_index += 1
            self.graph_comboBox.addItem(_fromUtf8(""))
            self.graph_comboBox.setItemText(item_index, _fromUtf8(nf.nome))
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Projecto em Python", None, QtGui.QApplication.UnicodeUTF8))
        self.graph_comboBox.setItemText(0, QtGui.QApplication.translate("Dialog", "Escolha o gráfico", None, QtGui.QApplication.UnicodeUTF8))
        
from matplotlibwidgetFile import matplotlibWidget
