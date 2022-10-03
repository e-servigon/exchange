from django.shortcuts import render
import requests, uuid, json
from .forms import * 
from .models import *

# Create your views here.

def home(request):
    return render(request,'home.html',{})

def translate (request):
    translateform = TranslateTextsForm()
    context = {'translateform':translateform}

    if request.method == 'POST':

        translateform = TranslateTextsForm(request.POST)
        print(request.POST)
        print(request.POST.get('language_code_destiny'))
        print(request.POST.get('text_to_translate'))

    return render(request,'translate.html',context)


