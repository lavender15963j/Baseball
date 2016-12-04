from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import DetailView, TemplateView

class IntroductionView(TemplateView):
    template_name = "team/introduction.html"

class ScheduleView(TemplateView):
    template_name = "team/schedule.html"

class RecordView(TemplateView):
    template_name = "team/record.html"

