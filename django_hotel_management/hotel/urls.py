from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.home,name='hotel-home'),
    path('home/', views.home,name='hotel-home'),
    path('about/', views.about,name='hotel-about'),
]
