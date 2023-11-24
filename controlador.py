from PyQt5.QtWidgets import QApplication
from modelo import Modelo
from vista import Vista
import sys
class Controlador:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def img(self,imagen):
        self.modelo.picture_img(imagen)
    
    def info_P(self,data):
        self.modelo.Info(data)

def main():
    app = QApplication(sys.argv)
    modelo = Modelo()
    vista = Vista()
    mi_controlador = Controlador(modelo,vista)
    Vista(mi_controlador)
    vista.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()