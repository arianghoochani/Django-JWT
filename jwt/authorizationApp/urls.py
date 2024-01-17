from django.urls import path
from . import views

urlpatterns  = [
    path('verifytoken/',views.login,name="login"),
    path('register/',views.registerUser,name="registerUser"),
    ]