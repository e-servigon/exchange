from django.shortcuts import render
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings
import requests, uuid
from .forms import * 
from .models import *

# Create your views here.

def home(request):
    return render(request,'home.html',{})

def error_404(request,exception):
    return render(request,'404.html',{})

def translate (request):
    translateform = TranslateTextsForm()
    context = {'translateform':translateform}

    if request.method == 'POST':

        translateform = TranslateTextsForm(request.POST)
        print(request.POST)
        print(request.POST.get('language_code_destiny'))
        print(request.POST.get('text_to_translate'))

        key = "dd50449a385c4850a52700aeb63cf2c5"
        endpoint = "https://api.cognitive.microsofttranslator.com"
        location = "eastus"

        path = '/translate'
        constructed_url = endpoint + path

        params = {
            'api-version': '3.0',
            'from': 'es',
            'to': request.POST.get('language_code_destiny')
        }

        headers = {
            'Ocp-Apim-Subscription-Key': key,
            'Content-type': 'application/json',
            'Ocp-Apim-Subscription-Region': location,
            'X-ClientTraceId': str(uuid.uuid4())
        }  

        body = [{
        'text': request.POST.get('text_to_translate')
        }]

        translate = requests.post(constructed_url, params=params, headers=headers, json=body)
        response = translate.json()
        print(response)
        context['responsetranslate'] = response
        translate_row = TranslateTexts.objects.create(language_code_origin='es', language_code_destiny= request.POST.get('language_code_destiny'), text_to_translate= request.POST.get('text_to_translate'), text_translated =response )
        translate_row.save()

    return render(request,'translate.html',context)


def sentiment (request):
    analizeform = AnalyzeTextsForm()
    context = {'analyzeform':analizeform}

    if request.method == 'POST':
        analizeform = AnalyzeTextsForm(request.POST)
        print(request.POST)
        print(request.POST.get('text_to_analyze'))

        credential = AzureKeyCredential("f98c4d09b876449c84312a0b10044eac")
        endpoint="https://dsccoglanguage.cognitiveservices.azure.com/"

        text_analytics_client = TextAnalyticsClient(endpoint, credential)

        documents = [
            request.POST.get('text_to_analyze')
        ]

        response = text_analytics_client.analyze_sentiment(documents, language="es")
        result = [doc for doc in response if not doc.is_error]

        print (result)

        for doc in result:
            print(f"Overall sentiment: {doc.sentiment}")
            print(
                f"Scores: positive={doc.confidence_scores.positive}; "
                f"neutral={doc.confidence_scores.neutral}; "
                f"negative={doc.confidence_scores.negative}\n"
            )

        context['sentimentresult'] = doc.sentiment
    return render(request,'sentiment.html',context)


def fileuploads (request):
    imageform = UploadFileForm()
    context = {'imageform':imageform}
    imagesgallery = uploadfolder.objects.all()
    context['imagegallery'] = imagesgallery
    if request.method == 'POST':
        imageform = UploadFileForm(request.POST, request.FILES)
        print(request.FILES)
        print(imageform.is_valid())
        print(imageform.errors)
        if imageform.is_valid():
            imageform.save()
        return render(request, 'fileupload.html',context)
    return render(request, 'fileupload.html',context)

def emails(request):
    emailform = SendEmailForm()
    context = {'emailform': emailform}

    if request.method == 'POST':
        print(request.POST.get('email_user'))
        context2 = {'email_user':request.POST.get('email_user')}
        email_to_send = request.POST.get('email_user')
        template = get_template('emailtemplate.html')
        content = template.render(context2)
        
        email = EmailMultiAlternatives(
            'aqui va el titulo del correo',
            'hola aqui va la descripcion del correo',
            settings.EMAIL_HOST_USER,
            [email_to_send],
        )

        email.attach_alternative(content,'text/html')
        email.send()
        return render(request, 'mail.html',context)
        

    return render(request, 'mail.html',context)
