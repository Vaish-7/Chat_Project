# this is similar to function of urls-- for websockets
from django.urls import path
from . import consumers

websocket_urlspatterns = [
    path('ws/<str:group_name>/', consumers.ChatConsumer.as_asgi()),
]