from io import UnsupportedOperation
from django import forms

from MusicPro.VistaEmpleados.models import Empleado
class LoginForm (forms.Form):
    class Meta: 
        model = Empleado
        fields= [ 'username','password']