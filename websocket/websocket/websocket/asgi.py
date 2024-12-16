"""
ASGI config for websocket project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from django.urls import path
from homeapp.consumers import *

from channels.routing import ProtocolTypeRouter, URLRouter
from homeapp import *

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websocket.settings')

application = get_asgi_application()


ws_patterns=[

    path('ws/test/',TestConsumer)

]

application = ProtocolTypeRouter({
    'websocket':URLRouter(ws_patterns)

})
