from django.db import models

# Create your models here.

class TranslateTexts(models.Model):
    TYPE_LANGUAGE_CHOICE = [('en', 'english'), ('fr', 'france'), ('de', 'deutch')]
    language_code_origin = models.CharField(max_length=2)
    language_code_destiny = models.CharField(max_length=2, choices=TYPE_LANGUAGE_CHOICE)
    text_to_translate = models.CharField(max_length=255)
    text_translated = models.CharField(max_length=255)

    def __str__ (self):
        return 'el texto traducido es %s %s' % (self.language_code_destiny, self.text_translated)

class UploadFoto(models.Model):
    image_to_upload=models.ImageField(upload_to='')
