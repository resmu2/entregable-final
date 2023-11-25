from PyQt5.QtCore import QObject
import pydicom
import matplotlib.pyplot as plt
import os
class Modelo():
    def __init__(self):
        self._carpeta = 'c:/Users/David.R/Documents/entregable final/Circle of Willis'
    
    def picture_img(self, img):
        ds = pydicom.dcmread(self._carpeta+'/'+ os.listdir(self._carpeta)[img])
        pixel_data = ds.pixel_array
        return pixel_data

    def Info(self,data):
        info = pydicom.dcmread(self._carpeta+'/'+os.listdir(self._carpeta)[data])
        nombre = info.PatientName
        ID = info.PatientID
        P_body = info.BodyPartExamined
        return f'Nombre del paciente: {nombre}\nId del paciente: {ID}\nParte del cuerpo: {P_body}'
    
    def credenciales(self,user,password):
        if user == 'medicoAnalitico' and password == 'bio12345':
            return True
        return False
    
    def addcarpeta(self,carpeta):
        self._carpeta = carpeta