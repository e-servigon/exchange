# Generated by Django 4.0.6 on 2022-11-07 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0006_rename_file_to_upload_uploadfolder_file_to_upload'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_user', models.CharField(max_length=100)),
            ],
        ),
    ]
