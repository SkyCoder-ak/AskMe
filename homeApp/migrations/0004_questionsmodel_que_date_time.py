# Generated by Django 3.0.5 on 2021-05-28 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeApp', '0003_auto_20210528_0924'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionsmodel',
            name='que_date_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
