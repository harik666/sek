from . import views
from django.urls import path

app_name = "online"
urlpatterns = [
    # path('', views.fun_home, name="home"),
    path('about/', views.fun_about, name="about"),
    path('contact/', views.fun_contact, name="contact"),
    path('detail/', views.fun_detail, name="detail"),
    path('thanks/', views.fun_thanks, name="thanks"),
    path('calc/', views.fun_calc, name="calc"),
    # path('', views.fun_input, name="input"),
    path('', views.fun_index, name="index"),

]
