import sys
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        
        print("ilk aşama")

        self.init_ui()


    def init_ui(self):
        self.yazı_alanı = QtWidgets.QLabel("Henüz Tıklanmadı")
        self.button = QtWidgets.QPushButton("Buraya Tıkla")
        self.say = 0

        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.button)
        v_box.addWidget(self.yazı_alanı)
        v_box.addStretch()

        h_box =QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.button.clicked.connect(self.click)
        self.show()

    def click(self):
        self.say+=1
        self.yazı_alanı.setText(str(self.say)+" Tıkladınız")

        


app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())


