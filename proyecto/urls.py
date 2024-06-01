from django.contrib import admin
from django.urls import path
from proyecto import views
from .views import inicio_sesion, list_templates, registro_usuario 

urlpatterns = [
    path('fun_home', views.fun_hom, name='home'),
    path('ahorros', views.fun_ahor,name='ahorros'),
    path('creditos', views.fun_credi,name='creditos'),
    path('registro_user', views.fun_re_us,name='registro_user'),
    path('registro_admin', views.fun_re_adm,name='registro_admin'),
    path('tabla_main', views.fun_tab_main,name='tabla_main'),
    path('tabla_edit', views.fun_tab_edit,name='tabla_edit'),
    path('tabla_edit_admin', views.fun_tab_edit_admin,name='tabla_edit_admin'),
    path('actualizar_campo/', views.actualizar_campo, name='actualizar_campo'),
    path('registros/', registro_usuario, name='registros'),
    path('registrosadmin/', views.fun_re_adm, name='registrosadmin'),
    path('registration/login.html', inicio_sesion, name='inicio_sesion'),
    path('user/', views.fun_visu, name='fun_visu'),
    path('informacion/', views.fun_infvisu, name='informacion'),
    path('registro_edit/<int:id>', views.fun_reg_edit,name='editar_usuario'),
    path('pg_admin/', views.fun_viadmin,name='pg_admin'),
    path('editar_admin/<int:id>', views.editar_admin,name='editar_admin'),
    path('list_templates/', list_templates, name='list_templates'),

]
