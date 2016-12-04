from django.conf.urls import url, include
from core.application import Application

from . import views 

class TeamApplication(Application):
    name = 'team'

    def get_urls(self):
        urls = [
            url(r'^introduction/$', views.IntroductionView.as_view(), name='introduction'),
            url(r'^schedule/$', views.ScheduleView.as_view(), name='schedule'),
            url(r'^record/$', views.RecordView.as_view(), name='record'),
        ]
        return urls

application = TeamApplication()