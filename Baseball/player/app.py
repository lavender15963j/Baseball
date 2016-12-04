from django.conf.urls import url, include
from core.application import Application

from . import views 

class PlayerApplication(Application):
    name = 'player'

    def get_urls(self):
        urls = [
             url(r'^$', views.PlayerListView.as_view(), name='players'),
        ]
        return urls

application = PlayerApplication()