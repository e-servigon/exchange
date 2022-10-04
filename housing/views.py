from django.shortcuts import render
import requests, uuid, json
from .forms import * 
from .models import *
import requests, uuid, json
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
        # Add your key and endpoint
        key = "30bb7b15b98742389f3b2397f59218e6"
        endpoint = "https://api.cognitive.microsofttranslator.com"

        # Add your location, also known as region. The default is global.
        # This is required if using a Cognitive Services resource.
        location = "eastus"

        path = '/translate'
        constructed_url = endpoint + path

        params = {
            'api-version': '3.0',
            'from': 'es',
            'to': [request.POST.get('language_code_destiny')]
        }

        headers = {
            'Ocp-Apim-Subscription-Key': key,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4()),
            'Ocp-Apim-Subscription-Region': location
        }

        # You can pass more than one object in body.
        body = [{
            'text': request.POST.get('text_to_translate')
        }]

        translate = requests.post(constructed_url, params=params, headers=headers, json=body)
        response = translate.json()
        context['responsetranslate'] = response 
        print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))
    return render(request,'translate.html',context)


