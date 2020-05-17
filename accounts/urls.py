from django.urls import path, include
from . import views
urlpatterns = [
    path('', include('allauth.urls')),
    path('', views.login, name="login"),
    path('signUP/', views.signUP, name="signUP"),
    path('logout2/', views.logout2, name="logout2"),
]