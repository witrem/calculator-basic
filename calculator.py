import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__() #main form, qmainwindow'dan alındığı için önce onu inite etmemiz lazım

        self.setWindowTitle('Calculator')
        self.setGeometry(200,200,500,400)
        self.initUI()

    def initUI(self):
        self.lbl_sayi1 = QtWidgets.QLabel(self)
        self.lbl_sayi1.setText('SAYI 1:')
        self.lbl_sayi1.move(50,30)

        self.txt_sayi1 = QtWidgets.QLineEdit(self)
        self.txt_sayi1.move(150,30)
        self.txt_sayi1.resize(200,32)

        self.lbl_sayi2 = QtWidgets.QLabel(self)
        self.lbl_sayi2.setText('SAYI 2:')
        self.lbl_sayi2.move(50,80)

        self.txt_sayi2 = QtWidgets.QLineEdit(self)
        self.txt_sayi2.move(150,80)
        self.txt_sayi2.resize(200,32)

        self.btn_topla = QtWidgets.QPushButton(self)
        self.btn_topla.setText('Topla') 
        self.btn_topla.move(150,130)
        self.btn_topla.clicked.connect(self.hesaplama)

        self.btn_çıkar = QtWidgets.QPushButton(self)
        self.btn_çıkar.setText('Çıkar') 
        self.btn_çıkar.move(150,180)
        self.btn_çıkar.clicked.connect(self.hesaplama)

        self.btn_bölme = QtWidgets.QPushButton(self)
        self.btn_bölme.setText('Bölme') 
        self.btn_bölme.move(150,220)
        self.btn_bölme.clicked.connect(self.hesaplama)

        self.btn_çarpma = QtWidgets.QPushButton(self)
        self.btn_çarpma.setText('Çarpma') 
        self.btn_çarpma.move(150,260)
        self.btn_çarpma.clicked.connect(self.hesaplama)

        self.lbl_sonuç = QtWidgets.QLabel(self)
        self.lbl_sonuç.setText('SONUÇ:')
        self.lbl_sonuç.resize(200,32)
        self.lbl_sonuç.move(150,310)


    def hesaplama(self):
        sender = self.sender().text() #butona referans verecek ve ona göre bir fonksiyon çağıracaktır
        result = 0
        if sender == 'Topla':
            result = int(self.txt_sayi1.text()) + int(self.txt_sayi2.text())
        elif sender == 'Çıkar':
            result = int(self.txt_sayi1.text()) - int(self.txt_sayi2.text())
        elif sender == 'Bölme':
            if self.txt_sayi2.text() == '0':
                result =  "zero division error"
            else:
                result = int(self.txt_sayi1.text()) / int(self.txt_sayi2.text())
        elif sender == 'Çarpma':
            result = int(self.txt_sayi1.text()) * int(self.txt_sayi2.text())
        
        
        self.lbl_sonuç.setText('SONUÇ : ' + str(result))
        
            
     
def app():
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())

app() 