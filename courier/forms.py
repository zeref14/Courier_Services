from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields='__all__'
        exclude=['student']



class StudentForm(ModelForm):
    class Meta:
        model=Student
        fields='__all__'
        exclude=['room_no','user']



class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']
