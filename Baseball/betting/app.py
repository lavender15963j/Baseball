from django.conf.urls import url, include
from core.application import Application

from . import views 

class BettingApplication(Application):
    name = 'betting'

    def get_urls(self):
        urls = [
            url(r'^statistics/$', views.StatisticsView.as_view(), name='statistics'),
            url(r'^prediction/$', views.PredictionView.as_view(), name='prediction'),
        ]
        return urls

application = BettingApplication()