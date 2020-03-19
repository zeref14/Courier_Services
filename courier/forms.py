from django.forms import ModelForm
from .models import *

class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields='__all__'
        exclude=['student']



class StudentForm(ModelForm):
    class Meta:
        model=Student
        fields='__all__'
        exclude=['room_no']
