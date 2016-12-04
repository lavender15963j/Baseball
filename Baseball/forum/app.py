from django.conf.urls import url, include
from core.application import Application

from . import views 

class ForumApplication(Application):
    name = 'forum'

    def get_urls(self):
        urls = [
            url(r'^$', views.ForumListView.as_view(), name='forum'),
            url(r'^(?P<article>[\w-]*)/(?P<pk>\d+)/$', views.ForumArticleDetailView.as_view(), name='forum_article'),
        ]
        return urls

application = ForumApplication()