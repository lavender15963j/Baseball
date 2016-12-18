#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from models import User
from django.contrib.auth.forms import UserCreationForm as _UserCreationForm

class UserCreationForm(_UserCreationForm):
    class Meta(_UserCreationForm.Meta):
        model = User
        fields = _UserCreationForm.Meta.fields