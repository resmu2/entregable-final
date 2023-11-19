from PyQt5.QtWidgets import QMainWindow, QDialog
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi
import os

class Vista(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('c:/Users/David.R/Downloads/clasetaller2-main/clasetaller2-main/base.ui', self)
    
    def addControlador(self,c):
        self.__miCoordinador = c
    
    def abrirVentanaimg(self):
        ventana_img = VentanaImg(self)
        self.hide()
        ventana_img.show()

class VentanaImg(QDialog):
    pass