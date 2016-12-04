#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic.list import ListView
from game.models import Game

# Create your views here.

def getHomeView(request):
    return render(request, 'main/Home.html')
    
def getBettingView(request):
    return render(request, 'Betting.html')
    
def getTeamView(request):
    return render(request, 'Team.html')
    
def getMemberView(request):
    return render(request, 'Member.html')
    
def getTalkView(request):
    return render(request, 'Talk.html')
    
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
