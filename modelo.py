from PyQt5.QtCore import QObject
import pydicom
import matplotlib.pyplot as plt
class Modelo():
    def __init__(self):
        self._carpeta = 'c:/Users/David.R/Documents/entregable final/Circle of Willis'
        self.__usuario = 'medicoAnalitico'
        self.__contrasena = 'bio12345'
    
    def picture_img(self, img):
        ds = pydicom.dcmread(self._carpeta+'/'+img)
        pixel_data = ds.pixel_array