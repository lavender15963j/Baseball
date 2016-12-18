from django.conf.urls import url, include
from core.application import Application
from django.contrib.auth.views import login, logout

from . import views 

class MainApplication(Application):
    name = 'main'

    def get_urls(self):
        urls = [
            url(r'^$', views.getHomeView, name='home'),
            url(r'^accounts/login/$', views.LoginView.as_view(), name="login"),
            url(r'^accounts/logout/$', views.LogoutView.as_view(), name="logout"),
            url(r'^accounts/register/$', views.RegisterView.as_view(), name="register"),
            url(r'^accounts/data/$', views.getMemberView, name='member'),
        ]
        return urls

application = MainApplication()
