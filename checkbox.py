import sys

from PyQt5.QtWidgets import QWidget, QApplication, QCheckBox,QLabel,QPushButton,QVBoxLayout

class Pencere(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.checkbox = QCheckBox("Pythonu seviyor musun ?")
        self.yazı_alanı = QLabel("")
        self.button =QPushButton("Buraya Tıkla")

        v_box = QVBoxLayout()
        v_box.addWidget(self.checkbox)
        v_box.addWidget(self.yazı_alanı)
        v_box.addWidget(self.button)

        self.setLayout(v_box)

        self.setWindowTitle("Check Box")

        self.button.clicked.connect(lambda : self.click(self.checkbox.isChecked(), self.yazı_alanı))

        self.show()
    
    def click(self,checkbox,yazı_alani):
        if checkbox:
            yazı_alani.setText("Çok güzel seviyorsun")
        else:
            yazı_alani.setText("Neden sevmiyorsun")

app = QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())


