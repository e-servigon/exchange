# Generated by Django 4.0.6 on 2022-10-04 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0002_sentimenttexts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sentimenttexts',
            name='sentiment_result',
        ),
    ]
