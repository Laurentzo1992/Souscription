from django.urls import path, include
from  . import views
from souscription.views import *


urlpatterns = [
    path('', views.home, name='home'),
    path('demande', views.demande, name='demande'),
    path('mon_espace', views.espace, name='espace'),
    
    path('createuser', views.createuser, name='createuser'),
    path('login_user', views.login_user, name='login_user'),
    path('logout_user', views.logout_user, name='logout_user'),
    
    path('login', views.Login, name='login'),
    
]