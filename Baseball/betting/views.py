from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import DetailView, TemplateView

class StatisticsView(TemplateView):
    template_name = "betting/statistics.html"

class PredictionView(TemplateView):
    template_name = "betting/prediction.html"
