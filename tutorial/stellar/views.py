from django.db import connection
from django.shortcuts import render
from .models import Introduction
# Create your views here.

def index(response):

    intros = Introduction.objects.all()

    return render(response, 'index.html', {'intros': intros})