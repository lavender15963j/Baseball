#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.


class Game(models.Model):
    y_game_no = models.CharField(max_length=30, unique=True)
    
    stadium = models.CharField(max_length=30)
    date = models.DateTimeField()
    
    away_team = models.CharField(max_length=30)
    away_team_score = models.IntegerField()
    
    home_team = models.CharField(max_length=30)
    home_team_score = models.IntegerField()
    
    win_team = models.CharField(max_length=30)
    
    def __str__(self):
        return self.y_game_no