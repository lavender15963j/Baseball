from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import DetailView, TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class StatisticsView(TemplateView):
    template_name = "betting/statistics.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(StatisticsView, self).dispatch(*args, **kwargs)

class PredictionView(TemplateView):
    template_name = "betting/prediction.html"
