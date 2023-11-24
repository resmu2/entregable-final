from PyQt5.QtCore import QObject
import pydicom
import matplotlib.pyplot as plt
class Modelo():
    def __init__(self):
        self._carpeta = 'c:/Users/David.R/Documents/entregable final/Circle of Willis'
    
    def picture_img(self, img):
        ds = pydicom.dcmread(self._carpeta+'/'+img)
        pixel_data = ds.pixel_array
        if (len(pixel_data.shape))==3:
            slice_index = pixel_data.shape[0] // 2
            selected_slice = pixel_data[slice_index, :, :]
            plt.imshow(selected_slice, cmap=plt.cm.bone)
        else:
            plt.imshow(pixel_data, cmap=plt.cm.bone)

    def Info(self,data):
        info = pydicom.dcmread(self._carpeta+'/'+data)
        nombre = info.PatientName
        ID = info.PatientID
        P_body = info.BodyPartExamined