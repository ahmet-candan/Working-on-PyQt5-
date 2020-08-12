"""import sys
from PyQt5 import QtWidgets
def Pencere():
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("Dombili alperrrrr")
    pencere.show()
    sys.exit(app.exec_())
Pencere()"""

import sys
from PyQt5 import QtWidgets,QtGui

def Pencere():

    app = QtWidgets.QApplication(sys.argv)

    #Pencere Oluşturma
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("Merhabaa")
    pencere.setGeometry(150,150,1000,500)

    #Text Oluşturma
    etiket1 = QtWidgets.QLabel(pencere)
    etiket1.setText("MERHABA BU İLK YAZI")
    etiket1.move(200,100)
    

    #Resim Ekleme
    etiket2 = QtWidgets.QLabel(pencere)
    etiket2.setPixmap(QtGui.QPixmap("osint_16_etkinlik.jpg"))
    etiket2.setGeometry(100,200,100,100)

    #Buton Oluşturma
    buton = QtWidgets.QPushButton(pencere)
    buton.setText("Giriş Butonu")
    buton.move(200,200)
    




    pencere.show()
    sys.exit(app.exec_())

Pencere()


