from PyQt5.QtWidgets import QMainWindow, QDialog
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi
import os

class Vista(QMainWindow):
    def __init__(self,ppal = None):
        super().__init__(ppal)
        loadUi('c:/Users/David.R/Documents/entregable final/ventana_login', self)
        self.setup()

    def setup(self):
        self.I_sesion.clicked.connect(self.abrirVentanaimg)
    
    def addControlador(self,c):
        self.__miCoordinador = c
    
    def controlador(self):
        return self.__miCoordinador
    
    def abrirVentanaimg(self):
        ventana_img = VentanaImg(self)
        self.hide()
        ventana_img.show()

class VentanaImg(QDialog):
    def __init__(self,ppal=None):
        super().__init__(ppal)
        loadUi("c:/Users/David.R/Documents/entregable final/ventana_img.ui",self)
        self.__ventana_login = ppal
        self.setup()

    def stup(self):
        self.comboBox.currentIndexChanged.connect(self.cargar)
        self.carpeta = 'c:/Users/David.R/Documents/entregable final/Circle of Willis'
        lista_archivos = os.listdir(self.carpeta)
        for archivo in lista_archivos:
            self.comboBox.addItem(archivo)
    
    def cargar(self):
        imagen = self.comboBox.currentText()
        self.__ventana_login.controlador().img(imagen)
        self.__ventana_login.controlador().info_P(imagen)