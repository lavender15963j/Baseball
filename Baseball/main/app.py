from django.conf.urls import url, include
from core.application import Application
from django.contrib.auth.views import login, logout

from . import views 

class MainApplication(Application):
    name = 'main'

    def get_urls(self):
        urls = [
            url(r'^$', views.getHomeView, name='home'),
            url(r'^account/login/$', views.LoginView.as_view(), name="login"),
            url(r'^account/logout/$', views.LogoutView.as_view(), name="logout"),
            url(r'^account/register/$', views.RegisterView.as_view(), name="register"),
            url(r'^account/data/$', views.getMemberView, name='member'),
        ]
        return urls

application = MainApplication()
