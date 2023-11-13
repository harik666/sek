from . import views
from django.urls import path

urlpatterns = [
    path('register', views.fun_reg, name="reg"),
    path('login', views.fun_login, name="log"),
    path('logout', views.fun_logt, name="logt"),

]
