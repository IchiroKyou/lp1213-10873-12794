# -*- coding: utf-8 -*-
# generated using 'uitopy' - mustafa yilmaz (penguen@linux.erciyes.edu.tr)
# 16 11 2012 - 16:46:36

import sys
from PyQt4 import QtCore, QtGui
from gui import Ui_Inscritos_2010_2011

class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL('clicked()'), self.fonksiyon)



def main():
    app = QtGui.QApplication(sys.argv)
    program = StartQT4()
    program.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
