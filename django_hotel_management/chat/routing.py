from django.conf.urls import url
from django.urls import re_path

from .customers import ChatCustomer

websocket_urlpatterns = [
    re_path(r'^ws/chat/(?P<room_name>[^/]+)/$', ChatCustomer),
]
