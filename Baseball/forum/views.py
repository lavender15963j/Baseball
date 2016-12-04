from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import DetailView, TemplateView

class ForumListView(ListView):
    template_name = 'forum/forum.html'

    def get_queryset(self):
        return []

class ForumArticleDetailView(ListView):
    template_name = "forum/forum_article.html"

    def get_queryset(self):
        return []
