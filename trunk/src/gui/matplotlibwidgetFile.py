# -*- coding: utf-8 -*-
'''
@author: 10873 Jorge Coveiro
@author: 12794 Carlos Rosário
@obs: Esta porção do código foi adquirida na internet,
atravéz de uma busca com o objectivo de incorporar um gráfico
realizado atravez do matplotlib, numa gui criada atravez de Qt4 Designer,
usando PyQt4
'''
from PyQt4 import QtGui
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas

from matplotlib.figure import Figure

class MplCanvas(FigureCanvas):
    '''
    Cria uma tela para o gráfico ser desenhado.
    Esta tela vai ser usada pelo matplotlibWidget
    '''
    def __init__(self):
        self.fig = Figure()
        self.ax1 = self.fig.add_subplot(111)
        self.ax2 = self.fig.add_subplot(111)
        self.ax3 = self.fig.add_subplot(111)
        
        self.ax1.set_ylabel(u'Número de inscritos')
        self.ax1.set_title(u'Número de inscritos/ano lectivo')
        
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self, QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


class matplotlibWidget(QtGui.QWidget):

    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.canvas = MplCanvas()
        self.vbl = QtGui.QVBoxLayout()
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)
