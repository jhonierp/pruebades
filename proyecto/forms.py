from django import forms
from .models import PersonasNaturales

class PNatuForm(forms.ModelForm):
    class Meta:
        model=PersonasNaturales
        fields='__all__'
        
# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['username','email']

class RegistroAdminForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['username','email', 'rol']
        widgets = {
            'rol': forms.CheckboxInput(attrs={'checked': True}),  # Establece el valor predeterminado del campo de selección de roles como True
        }
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)