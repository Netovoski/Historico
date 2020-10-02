from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from .models import Hist_voo2015, Hist_voo2016, Hist_voo2017

from .forms import *


def index(request):
    return render(request, 'index.html')

def Hist_2015_1(request):
    items = Hist_voo2015.objects.all()
    context = {
        'items': items,
        'header': 'Historico 2015 Janeiro',
    }
    return render(request, 'hist2015.html', context)

def Hist_2015_2(Hist_2015_1):
    pass
    context = {
        'header': 'Historico 2015 Fevereiro',
    }
    return render(Hist_2015_1, 'hist2015.html', context)


def Hist_2015_3(Hist_2015_1):
    pass
    context = {
        'header': 'Historico 2015 Março',
    }
    return render(Hist_2015_1, 'hist2015.html', context)

def Hist_2016_1(request):
    items = Hist_voo2016.objects.all()
    context = {
        'items': items,
        'header': 'Historico 2016 Janeiro',
    }
    return render(request, 'hist2016.html', context)


def Hist_2016_2(Hist_2016_1):
    pass
    context = {
        'header': 'Historico 2016 Fervereiro',
    }
    return render(Hist_2016_1, 'hist2016.html', context)

def Hist_2016_3(Hist_2016_1):
    pass
    context = {
        'header': 'Historico 2016 Março',
    }
    return render(Hist_2016_1, 'hist2016.html', context)

def Hist_2017_1(request):
    items = Hist_voo2017.objects.all()
    context = {
        'items': items,
        'header': 'Historico 2017 Janeiro',
    }
    return render(request, 'hist2017.html', context)