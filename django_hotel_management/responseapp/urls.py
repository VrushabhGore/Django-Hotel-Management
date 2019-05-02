
from django.urls import path
from django.contrib import admin

from responseapp import views as responseapp_views

urlpatterns = [
 path('', responseapp_views.responseform, name = 'response'),
 path('thankyou/', responseapp_views.responseform),

path('', admin.site.urls),
]
