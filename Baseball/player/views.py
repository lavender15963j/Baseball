from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import DetailView, TemplateView

class PlayerListView(TemplateView):
    template_name = "player/players.html"
