from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from .models import *

from .forms import *


def index(request):
    return render(request, 'index.html')

def Hist_2015_1(request):
    item = Hist_voo2015.objects.all()
    context = {
        'item': item,
        'header': 'Historico 2015 Janeiro',
    }
    return render(request, 'hist2015.html', context)

def Hist_2015_2(request):
    item = Hist_voo2015_2.objects.all()
    context = {
        'item': item,
        'header': 'Historico 2015 Fevereiro',
    }
    return render(request, 'hist2015.html', context)


def Hist_2015_3(Hist_2015_1):
    pass
    context = {
        'header': 'Historico 2015 Março',
    }
    return render(Hist_2015_1, 'hist2015.html', context)

def Hist_2015_4(Hist_2015_1):
    pass
    context = {
        'header': 'Historico 2015 Abril',
    }
    return render(Hist_2015_1, 'hist2015.html', context) 

def Hist_2015_5(Hist_2015_1):
    pass
    context = {
        'header': 'Historico 2015 Maio',
    }
    return render(Hist_2015_1, 'hist2015.html', context) 

def Hist_2015_6(Hist_2015_1):
    pass
    context = {
        'header': 'Historico 2015 junho',
    }
    return render(Hist_2015_1, 'hist2015.html', context) 
def Hist_2015_7(Hist_2015_1):
    pass
    context = {
        'header': 'Historico 2015 Julho',
    }
    return render(Hist_2015_1, 'hist2015.html', context) 
def Hist_2015_8(Hist_2015_1):
    pass
    context = {
        'header': 'Historico 2015 Agosto',
    }
    return render(Hist_2015_1, 'hist2015.html', context) 
def Hist_2015_9(Hist_2015_1):
    pass
    context = {
        'header': 'Historico 2015 Setembro',
    }
    return render(Hist_2015_1, 'hist2015.html', context) 
def Hist_2015_10(Hist_2015_1):
    pass
    context = {
        'header': 'Historico 2015 Outubro',
    }
    return render(Hist_2015_1, 'hist2015.html', context) 
def Hist_2015_11(Hist_2015_1):
    pass
    context = {
        'header': 'Historico 2015 Novembro',
    }
    return render(Hist_2015_1, 'hist2015.html', context) 
def Hist_2015_12(Hist_2015_1):
    pass
    context = {
        'header': 'Historico 2015 Dezembro',
    }
    return render(Hist_2015_1, 'hist2015.html', context) 


def Hist_2016_1(request):
    item = Hist_voo2016.objects.all()
    context = {
        'item': item,
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
    item = Hist_voo2017.objects.all()
    context = {
        'item': item,
        'header': 'Historico 2017 Janeiro',
    }
    return render(request, 'hist2017.html', context)