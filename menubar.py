import sys 
from PyQt5.QtWidgets import QWidget,QApplication,QAction,qApp,QMainWindow

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()

        menubar = self.menuBar()

        dosya = menubar.addMenu("Dosya")
        duzenle = menubar.addMenu("Düzenle")

        dosya_ac = QAction("Dosya Aç",self)
        dosya_ac.setShortcut("Ctrl+O")

        dosya_kaydet = QAction("Dosya Kaydet",self)
        dosya_kaydet.setShortcut("Ctrl+S")

        cikis = QAction("Çıkış",self)
        cikis.setShortcut("Ctrl+Q")

        dosya.addAction(dosya_ac)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(cikis)

        ara_degistir = duzenle.addMenu("Ara ve Değiştir")

        ara = QAction("Ara",self)
        degistir = QAction("Değiştir",self)
        temizle = QAction("Temizle",self)

        ara_degistir.addAction(ara)
        ara_degistir.addAction(degistir)
        duzenle.addAction(temizle)

        cikis.triggered.connect(self.cikis_yap)

        self.setWindowTitle("Menu Bar")
        self.show()
        
    def cikis_yap(self):
        qApp.quit()



app = QApplication(sys.argv)
menubar= Menu()
sys.exit(app.exec_())

