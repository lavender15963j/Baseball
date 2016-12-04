from django.conf.urls import url, include
from core.application import Application

from . import views 

class MainApplication(Application):
    name = 'main'

    def get_urls(self):
        urls = [
            url(r'^$', views.getHomeView, name='home'),
        ]
        return urls

application = MainApplication()
