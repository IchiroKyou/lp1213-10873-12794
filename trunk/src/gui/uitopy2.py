import os ,glob, re
from time import gmtime, strftime

dosyalar = []
siniflar = []
baslatici = "calisan"
anapencerehangisi = -1

for dosya in glob.glob("*.ui"):
    dosyalar.append(dosya)
    os.system("pyuic4 " + dosya + " -o " + dosya[0:(len(dosya)-3)] + ".py")
    print str(((glob.glob("*.ui")).index(dosya))+1) + ") " + dosya
print "\n" + str(len(dosyalar)) + " files converted"

for i in range(len(dosyalar)):
    f = open((dosyalar[i])[0:(len(dosya)-3)] + ".py", "r")
    metin = f.read()
    bas = re.search('class ', metin).end()
    son = re.search('\(', metin).start()
    f.seek(bas)
    siniflar.append(f.read(son-bas))
    if siniflar[i] == "Ui_MainWindow":
        anapencerhangisi = i
    f.close()

if os.path.isfile(baslatici + ".py") == 0:
    f = open(baslatici + ".py","a+")
    veri = "# -*- coding: utf-8 -*-\n\
# generated using 'uitopy' - mustafa yilmaz (penguen@linux.erciyes.edu.tr)\n"
    veri += "# " + strftime("%d %m %Y - %H:%M:%S", gmtime())
    veri += "\n\nimport sys\n\
from PyQt4 import QtCore, QtGui\n"
    for i in range(len(dosyalar)):
        veri += "from " + (dosyalar[i])[0:len(dosya)-3] + " import " + siniflar[i] + "\n\n"
    veri += "class StartQT4(QtGui.QMainWindow):\n\
    def __init__(self, parent=None):\n\
        QtGui.QWidget.__init__(self, parent)\n\
        self.ui = Ui_MainWindow()\n\
        self.ui.setupUi(self)\n\
        #QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL('clicked()'), self.fonksiyon)\n\
\n\n\n\
def main():\n\
    app = QtGui.QApplication(sys.argv)\n\
    program = StartQT4()\n\
    program.show()\n\
    sys.exit(app.exec_())\n\
\n\
if __name__ == '__main__':\n\
    main()\n"
    f.write(veri)
    f.close()

os.system("python " + baslatici + ".py")

