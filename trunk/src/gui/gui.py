# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Fri Nov 16 18:26:00 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QSizePolicy
from PyQt4.QtCore import QSize
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as Canvas
from matplotlib.figure import Figure

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class MatplotlibWidget(Canvas):
    """
    MatplotlibWidget inherits PyQt4.QtGui.QWidget
    and matplotlib.backend_bases.FigureCanvasBase

    Options: option_name (default_value)
    -------
    parent (None): parent widget
    title (''): figure title
    xlabel (''): X-axis label
    ylabel (''): Y-axis label
    xlim (None): X-axis limits ([min, max])
    ylim (None): Y-axis limits ([min, max])
    xscale ('linear'): X-axis scale
    yscale ('linear'): Y-axis scale
    width (4): width in inches
    height (3): height in inches
    dpi (100): resolution in dpi
    hold (False): if False, figure will be cleared each time plot is called

    Widget attributes:
    -----------------
    figure: instance of matplotlib.figure.Figure
    axes: figure axes

    Example:
    -------
    self.widget = MatplotlibWidget(self, yscale='log', hold=True)
    from numpy import linspace
    x = linspace(-10, 10)
    self.widget.axes.plot(x, x**2)
    self.wdiget.axes.plot(x, x**3)
    """
    def __init__(self, parent=None, title='', xlabel='', ylabel='',
                 xlim=None, ylim=None, xscale='linear', yscale='linear',
                 width=4, height=3, dpi=100, hold=False):
        self.figure = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.figure.add_subplot(111)
        self.axes.set_title(title)
        self.axes.set_xlabel(xlabel)
        self.axes.set_ylabel(ylabel)
        if xscale is not None:
            self.axes.set_xscale(xscale)
        if yscale is not None:
            self.axes.set_yscale(yscale)
        if xlim is not None:
            self.axes.set_xlim(*xlim)
        if ylim is not None:
            self.axes.set_ylim(*ylim)
        self.axes.hold(hold)

        Canvas.__init__(self, self.figure)
        self.setParent(parent)

        Canvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        Canvas.updateGeometry(self)

    def sizeHint(self):
        w, h = self.get_width_height()
        return QSize(w, h)

    def minimumSizeHint(self):
        return QSize(10, 10)
        
#-----------------------------------------------------------


class Ui_Inscritos_2010_2011(object):
    def setupUi(self, Inscritos_2010_2011):
		
        Inscritos_2010_2011.setObjectName(_fromUtf8("Inscritos_2010_2011"))
        Inscritos_2010_2011.resize(800, 633)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icon/estig.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Inscritos_2010_2011.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(Inscritos_2010_2011)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.bar2d_button = QtGui.QPushButton(self.centralwidget)
        self.bar2d_button.setGeometry(QtCore.QRect(130, 530, 106, 35))
        self.bar2d_button.setToolTip(_fromUtf8(""))
        self.bar2d_button.setWhatsThis(_fromUtf8(""))
        self.bar2d_button.setObjectName(_fromUtf8("bar2d_button"))
        self.bar3d_button = QtGui.QPushButton(self.centralwidget)
        self.bar3d_button.setGeometry(QtCore.QRect(240, 530, 106, 35))
        self.bar3d_button.setObjectName(_fromUtf8("bar3d_button"))
        self.line_h_button = QtGui.QPushButton(self.centralwidget)
        self.line_h_button.setGeometry(QtCore.QRect(350, 530, 106, 35))
        self.line_h_button.setObjectName(_fromUtf8("line_h_button"))
        self.line_m_button = QtGui.QPushButton(self.centralwidget)
        self.line_m_button.setGeometry(QtCore.QRect(460, 530, 106, 35))
        self.line_m_button.setObjectName(_fromUtf8("line_m_button"))
        self.line_hm_button = QtGui.QPushButton(self.centralwidget)
        self.line_hm_button.setGeometry(QtCore.QRect(570, 530, 106, 35))
        self.line_hm_button.setObjectName(_fromUtf8("line_hm_button"))
        self.shell_frame = QtGui.QFrame(self.centralwidget)
        self.shell_frame.setGeometry(QtCore.QRect(10, 370, 781, 91))
        self.shell_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.shell_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.shell_frame.setObjectName(_fromUtf8("shell_frame"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 470, 761, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.escolha = QtGui.QLabel(self.centralwidget)
        self.escolha.setGeometry(QtCore.QRect(220, 490, 361, 25))
        self.escolha.setObjectName(_fromUtf8("escolha"))
        self.graphic_display = QtGui.QWidget(self.centralwidget)
        self.graphic_display.setGeometry(QtCore.QRect(10, 9, 781, 351))
        self.graphic_display.setObjectName(_fromUtf8("graphic_display"))
        '''
        '''
        
        '''
        '''
        Inscritos_2010_2011.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(Inscritos_2010_2011)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Inscritos_2010_2011.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(Inscritos_2010_2011)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 33))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFicheiro = QtGui.QMenu(self.menubar)
        self.menuFicheiro.setObjectName(_fromUtf8("menuFicheiro"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        Inscritos_2010_2011.setMenuBar(self.menubar)
        self.actionCreditos = QtGui.QAction(Inscritos_2010_2011)
        self.actionCreditos.setObjectName(_fromUtf8("actionCreditos"))
        self.actionAbout = QtGui.QAction(Inscritos_2010_2011)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionOpen = QtGui.QAction(Inscritos_2010_2011)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionExport_as = QtGui.QAction(Inscritos_2010_2011)
        self.actionExport_as.setObjectName(_fromUtf8("actionExport_as"))
        self.actionQuit = QtGui.QAction(Inscritos_2010_2011)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuFicheiro.addAction(self.actionOpen)
        self.menuFicheiro.addAction(self.actionExport_as)
        self.menuFicheiro.addAction(self.actionQuit)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFicheiro.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(Inscritos_2010_2011)
        QtCore.QMetaObject.connectSlotsByName(Inscritos_2010_2011)
        self.plot(self.mplwidget.axes)

    def retranslateUi(self, Inscritos_2010_2011):
        Inscritos_2010_2011.setWindowTitle(QtGui.QApplication.translate("Inscritos_2010_2011", "Análise de Inscritos no Ensino Superior", None, QtGui.QApplication.UnicodeUTF8))
        self.bar2d_button.setText(QtGui.QApplication.translate("Inscritos_2010_2011", "Barras 2D", None, QtGui.QApplication.UnicodeUTF8))
        self.bar3d_button.setText(QtGui.QApplication.translate("Inscritos_2010_2011", "Barras 3D", None, QtGui.QApplication.UnicodeUTF8))
        self.line_h_button.setText(QtGui.QApplication.translate("Inscritos_2010_2011", "Linhas H", None, QtGui.QApplication.UnicodeUTF8))
        self.line_m_button.setText(QtGui.QApplication.translate("Inscritos_2010_2011", "Linhas M", None, QtGui.QApplication.UnicodeUTF8))
        self.line_hm_button.setText(QtGui.QApplication.translate("Inscritos_2010_2011", "Linhas HM", None, QtGui.QApplication.UnicodeUTF8))
        self.escolha.setText(QtGui.QApplication.translate("Inscritos_2010_2011", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Purisa\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">Escolha o tipo de gráfico a visualizar:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFicheiro.setTitle(QtGui.QApplication.translate("Inscritos_2010_2011", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("Inscritos_2010_2011", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCreditos.setText(QtGui.QApplication.translate("Inscritos_2010_2011", "Creditos", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("Inscritos_2010_2011", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("Inscritos_2010_2011", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport_as.setText(QtGui.QApplication.translate("Inscritos_2010_2011", "Export As...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("Inscritos_2010_2011", "Quit", None, QtGui.QApplication.UnicodeUTF8))

	def plot(self, axes):
		x = linspace(-10, 10)
        axes.plot(x, x**2)
        axes.plot(x, x**3)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Inscritos_2010_2011 = QtGui.QMainWindow()
    ui = Ui_Inscritos_2010_2011()
    ui.setupUi(Inscritos_2010_2011)
    Inscritos_2010_2011.show()
    sys.exit(app.exec_())

