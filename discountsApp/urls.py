from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signIn, name='signIn'),
    path('signup/', views.signUp, name='signUp'),
    path('forgotpassword/', views.forgotPassword)
]
