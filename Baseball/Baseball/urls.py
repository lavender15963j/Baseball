"""Baseball URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout

from main.app import application as main_app
from forum.app import application as forum_app
from betting.app import application as betting_app
from player.app import application as player_app
from team.app import application as team_app

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, name='logout'),

    url(r'', include(main_app.urls)),
    url(r'^forum/', include(forum_app.urls)),
    url(r'^betting/', include(betting_app.urls)),
    url(r'^player/', include(player_app.urls)),
    url(r'^team/', include(team_app.urls)),
]
