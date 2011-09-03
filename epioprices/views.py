#-*- coding: utf-8 -*-
from django.views.generic.list import ListView
from epioprices.models import Deployment

class HomeView(ListView):
    model = Deployment
