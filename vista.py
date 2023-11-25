from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QMainWindow, QDialog, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi
import os

class Vista(QMainWindow):
    def __init__(self,ppal = None):
        super().__init__(ppal)
        
        loadUi('c:/Users/David.R/Documents/entregable final/Ventana_Login.ui', self)
        self.setup()

    def setup(self):
        self.I_sesion.clicked.connect(self.validar)

    def controlador(self,co):
        self.__miCoordinador = co
    
    def abrirVentanaimg(self):
        ventana_img = VentanaImg(self)
        ventana_img.addcontrolador(self.__miCoordinador)
        self.hide()
        ventana_img.show()
    
    def validar(self):
        user = self.name.text()
        password = self.ingreso.text()
        if self.__miCoordinador.autenticacion(user,password) == True:
            self.abrirVentanaimg()
        else:
            error_login = Error_login(self)
            error_login.show()

class VentanaImg(QDialog):
    def __init__(self,ppal=None):
        super().__init__(ppal)
        loadUi("c:/Users/David.R/Documents/entregable final/Ventana_Img.ui",self)
        self.__ventana_login = ppal
        self.setup()

    def addcontrolador(self,c):
        self.__miCoordinador = c

    def setup(self):
        self.slider.valueChanged.connect(self.cargar)
        self.v_ruta.clicked.connect(self.carpeta)
        self.graficadora = MplCanvas(self.c_imagen,width=5, height=4, dpi=100)
        self.organizador.addWidget(self.graficadora)
        self.salir.clicked.connect(self.cerrar)
    
    def cargar(self):
        try:
            corte_imagen = self.slider.value()
            self.graficadora.graficar(self.__miCoordinador.img(corte_imagen))
            self.info.setText(self.__miCoordinador.info_P(corte_imagen))
            self.n_img.setText(os.listdir(self.ruta_d)[corte_imagen])
        except:
            ventana_error = Error_img(self)
            ventana_error.show()

    def carpeta(self):
        try:
            self.ruta_d = QFileDialog.getExistingDirectory(self,"Cargar Carpeta","")
            self.__miCoordinador.direccion(self.ruta_d)
            self.slider.setMinimum(0)
            self.slider.setMaximum(len(os.listdir(self.ruta_d)))
        except:
            ventana_error = Error_ruta(self)
            ventana_error.show()
    
    def cerrar(self):
        self.__ventana_login.show()
        self.hide()
    
class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super().__init__(self.fig)
    
    def graficar(self,array):
        self.axes.imshow(array)
        self.draw()
        # if (len(array.shape))==3:
        #     slice_index = pixel_data.shape[0] // 2
        #     selected_slice = array[slice_index, :, :]
        #     plt.imshow(selected_slice, cmap=plt.cm.bone)
        # else:
        #     plt.imshow(pixel_data, cmap=plt.cm.bone)

class Error_ruta(QDialog):
    def __init__(self,ppal=None):
        super().__init__(ppal)
        loadUi("c:/Users/David.R/Documents/entregable final/error_ruta.ui",self)
        self.setup()

    def setup(self):
        self.aceptar.clicked.connect(self.cerrar)
    
    def cerrar(self):
        self.hide()
    
class Error_img(QDialog):
    def __init__(self,ppal=None):
        super().__init__(ppal)
        loadUi("c:/Users/David.R/Documents/entregable final/error_img.ui",self)
        self.setup()

    def setup(self):
        self.aceptar.clicked.connect(self.cerrar)
    
    def cerrar(self):
        self.hide()
    
class Error_login(QDialog):
    def __init__(self,ppal=None):
        super().__init__(ppal)
        loadUi("c:/Users/David.R/Documents/entregable final/error_login.ui",self)
        self.setup()

    def setup(self):
        self.aceptar.clicked.connect(self.cerrar)
        
    def cerrar(self):
        self.hide()