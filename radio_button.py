import sys
from PyQt5.QtWidgets import QWidget,QApplication,QRadioButton,QLabel,QPushButton,QVBoxLayout

class Pencere(QWidget):
    def __init__(self):

        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.radio_yazısı = QLabel("Hangi Programlama Dilini Seçersin ?")
        self.python = QRadioButton("Python")
        self.php = QRadioButton("Php")
        self.java = QRadioButton("Java")
        self.buton =QPushButton("Onayala")
        self.yazi_alani = QLabel("")

        v_box = QVBoxLayout()
        v_box.addWidget(self.radio_yazısı)
        v_box.addWidget(self.python)
        v_box.addWidget(self.php)
        v_box.addWidget(self.java)
        v_box.addStretch()

        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.buton)

        self.setLayout(v_box)

        self.setWindowTitle("Radio Button")

        self.buton.clicked.connect(lambda : self.click(self.python.isChecked(),self.php.isChecked(),self.java.isChecked(),self.yazi_alani))

        self.show()

    def click(self,python,php,java,yazi_alani):
        if python:
            yazi_alani.setText("Python'u seçtiniz")
        if php:
            yazi_alani.setText("Php'yi seçtiniz")
        if java:
            yazi_alani.setText("Java'yı seçtiniz")


app = QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())



