from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Define una clase que extienda UserAdmin para personalizar la apariencia del modelo en el panel de administración
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'rol']

# Registra el modelo CustomUser con la clase CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)
