# Generated by Django 3.0.5 on 2021-05-26 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileApp', '0011_auto_20210526_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='age',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]
