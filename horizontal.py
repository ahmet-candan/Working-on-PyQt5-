import sys
from PyQt5 import QtWidgets

def Pencere():

    app = QtWidgets.QApplication(sys.argv)
    
    # 2 tane buton oluşturduk
    okay =QtWidgets.QPushButton("Giriş")
    cancel = QtWidgets.QPushButton("Çıkış")
    
    """horizontal box layout oluşturduk
    h_box = QtWidgets.QHBoxLayout()

    okay ve cancel butonlarını h_box'a ekledik
    h_box.addWidget(okay)
    h_box.addWidget(cancel)
    h_box.addStretch()

    #Veritical loayout oluşturduk
    v_box =QtWidgets.QVBoxLayout()

    # okay ve cancel butonlarını v_box'a ekledik
    v_box.addStretch()
    v_box.addWidget(okay)
    v_box.addWidget(cancel)
    

    pencere = QtWidgets.QWidget()

    # h_box u penceremize ekledik
    #pencere.setLayout(h_box)

    # v_box ı penceremize ekledik
    pencere.setLayout(v_box)"""

    #İç içe horizontal ve veritical
    h_box = QtWidgets.QHBoxLayout()
    # sola ayarladık
    h_box.addStretch()
    h_box.addWidget(okay)
    h_box.addWidget(cancel)
    

    v_box = QtWidgets.QVBoxLayout()
    #aşşağı aldık
    v_box.addStretch()
    v_box.addLayout(h_box)

    pencere = QtWidgets.QWidget()
    pencere.setLayout(v_box)

    pencere.setWindowTitle("Horizontal and Veritical")
    pencere.setGeometry(200,150,500,300)
    pencere.show()
    sys.exit(app.exec_())

Pencere()


