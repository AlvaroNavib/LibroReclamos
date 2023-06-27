from django import forms
from appReclamos.models import Registro

#Registro

class RegistroReclamo(forms.ModelForm):
    class Meta:
        model=Registro
        fields='__all__'
nombre=forms.CharField()
apellido=forms.CharField()  
fecha=forms.DateTimeField(widget=forms.DateTimeInput)
descripcion=forms.CharField()
mensaje=forms.CharField()


nombre.widget.attrs['class']='form-control'
apellido.widget.attrs['class']='form-control'
fecha.widget.attrs['class']='form-control datetimepicker-input'
descripcion.widget.attrs['class']='form-control'
mensaje.widget.attrs['class']='form-control'