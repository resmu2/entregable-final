from PyQt5.QtWidgets import QApplication
from modelo import Modelo
from vista import Vista
import sys
class Controlador:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def img(self,imagen):
        return self.modelo.picture_img(imagen)
    
    def info_P(self,data):
        return self.modelo.Info(data)
    
    def autenticacion(self,user,password):
        return self.modelo.credenciales(user,password)
    
    def direccion(self,info):
        self.modelo.addcarpeta(info)

def main():
    app = QApplication(sys.argv)
    modelo = Modelo()
    vista = Vista()
    mi_controlador = Controlador(modelo,vista)
    vista.controlador(mi_controlador)
    vista.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()