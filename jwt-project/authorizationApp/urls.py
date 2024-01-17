from django.urls import path
from . import views

urlpatterns  = [
    path('verifytoken/',views.authorizing,name="authorizing"),
    path('register/',views.registerUser,name="registerUser"),
    ]