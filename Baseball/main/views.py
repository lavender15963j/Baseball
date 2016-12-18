#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic import TemplateView, RedirectView
from django.contrib.auth import logout as auth_logout, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.utils.http import is_safe_url

from game.models import Game
from forms import UserCreationForm

# Create your views here.

def getHomeView(request):
    return render(request, 'main/Home.html')

def getMemberView(request):
    return render(request, 'member.html')
    
class TeamView(ListView):
    context_object_name = 'games'
    template_name = 'Team.html'
    
    def get(self, request, *args, **kwargs):
        self.home = request.GET.get('home')
        self.away = request.GET.get('away')
        self.year = request.GET.get('year')
        return super(TeamView, self).get(request, *args, **kwargs)
        
    
    def get_queryset(self):
        teamName = {
            'E02': '中信兄弟',
            'L01': 'Lamigo',
            'A02': '義大',
            'B03': '統一7-ELEVEn',
        }
        
        if self.home or self.away or self.year:
            homeTeam = None
            awayTeam = None
            if self.home:
                homeTeam = teamName[self.home]
            if self.away:
                awayTeam = teamName[self.away]
            games = Game.objects.all().filter(home_team=homeTeam, away_team=awayTeam, y_game_no__contains=self.year).order_by('-date')
        else:
            games = Game.objects.all().order_by('-date')   
        return games
        
    def get_context_data(self, **kwargs):
        kwargs['home_team'] = self.home
        kwargs['away'] = self.away
        kwargs['year'] = self.year
        return super(TeamView, self).get_context_data(**kwargs)

class LoginView(TemplateView):
    template_name="registration/login.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('/')
        return super(LoginView, self).get(
            request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        redirect_to = request.POST.get(redirect_field_name,
                                   request.GET.get(redirect_field_name, ''))
        """
        redirect_to = '/'
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(redirect_to)
        ctx = self.get_context_data(form=form)
        return self.render_to_response(ctx)

    def get_context_data(self, form=None, *args, **kwargs):
        ctx = super(LoginView, self).get_context_data(*args, **kwargs)
        if form:
            ctx['form'] = form
        else:
            ctx['form'] = AuthenticationForm
        return ctx

class RegisterView(TemplateView):
    template_name="registration/register.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('/')
        return super(RegisterView, self).get(
            request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        redirect_to = request.POST.get(redirect_field_name,
                                   request.GET.get(redirect_field_name, ''))
        """
        redirect_to = '/'
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            return redirect("/account/login/")
        ctx = self.get_context_data(form=form)
        return self.render_to_response(ctx)

    def get_context_data(self, form=None, *args, **kwargs):
        ctx = super(RegisterView, self).get_context_data(*args, **kwargs)
        if form:
            ctx['form'] = form
        else:
            ctx['form'] = UserCreationForm
        return ctx

class LogoutView(RedirectView):
    url = '/'
    permanent = False

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        response = super(LogoutView, self).get(request, *args, **kwargs)
        return response




